"""
This file contains the Flask application, routing, and logic for login
and the desperation index.
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import os
import csv
from datetime import datetime
from dotenv import load_dotenv
import random


# --- Flask App Initialization ---
app = Flask(__name__)
# Set a secret key for session management.
# In a real application, use a strong, randomly generated key from environment variables.
#app.secret_key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4na9' # IMPORTANT: Change this for production!

# Load environment variables from .env file
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

# --- File Paths ---
USERS_FILE = 'users.csv'
DESPERATION_RESULTS_FILE = 'desperation_results.csv'
JOB_RESPONSES_FILE = 'job_responses.csv' # New file for job interaction data
EXIT_SURVEY_RESULTS_FILE = 'exit_survey_results.csv' # New file for exit survey data

# Data directory for job postings
DATA_DIR = 'data'
AI_REFINED_FAKE_JOBS_FILE = os.path.join(DATA_DIR, 'llm_refined_30_fake_job_postings.csv')
MANUALLY_COLLECTED_REAL_JOBS_FILE = os.path.join(DATA_DIR, 'cleaned_real_jobs.csv')

# --- Global Data Storage (for simplicity in this small app) ---
# Load users from CSV
users_df = pd.DataFrame()
if os.path.exists(USERS_FILE):
    users_df = pd.read_csv(USERS_FILE)
else:
    print(f"WARNING: {USERS_FILE} not found. Please create it.")
    # Create a dummy DataFrame if the file doesn't exist to prevent errors
    users_df = pd.DataFrame(columns=['username', 'password', 'group'])

# Ensure the desperation results CSV exists with headers
if not os.path.exists(DESPERATION_RESULTS_FILE):
    with open(DESPERATION_RESULTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'user_id', 'group', 'q1_answer', 'q2_answer', 'q3_answer', 'q4_answer', 'q5_answer', 'desperation_score'])

# Ensure job responses CSV exists with headers
if not os.path.exists(JOB_RESPONSES_FILE):
    with open(JOB_RESPONSES_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'timestamp', 'user_id', 'group', 'job_id', 'job_index_in_set',
            'is_scam_response', 'scam_reason_text', 'applied_clicked', 'link_interacted',
            'time_on_job_page_seconds' # New metric to track
        ])

# Ensure exit survey results CSV exists with headers
if not os.path.exists(EXIT_SURVEY_RESULTS_FILE):
    with open(EXIT_SURVEY_RESULTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'user_id', 'group', 'jobs_interacted_range', 'low_interaction_reasons', 'low_interaction_other_reason'])

# --- Job Data Loading and Preparation ---
all_jobs_df = pd.DataFrame()
JOB_DATA_COLUMNS = [
    'job_id','job_title', 'job_description', 'company_name', 'is_scam_job', # Essential for the study
    # 'location', 'employment_type', 'raw_description', 'source_platform', 'original_url', 'collection_date', 'notes' # Other columns from schema, can be loaded if needed for display/analysis
]

try:
    fake_jobs = pd.read_csv(AI_REFINED_FAKE_JOBS_FILE)
    real_jobs = pd.read_csv(MANUALLY_COLLECTED_REAL_JOBS_FILE)

    # Ensure essential columns are present, fill missing with NaN
    for col in JOB_DATA_COLUMNS:
        if col not in fake_jobs.columns:
            fake_jobs[col] = pd.NA
        if col not in real_jobs.columns:
            real_jobs[col] = pd.NA

    # Select and reorder columns to ensure consistency
    fake_jobs = fake_jobs[JOB_DATA_COLUMNS]
    real_jobs = real_jobs[JOB_DATA_COLUMNS]

    all_jobs_df = pd.concat([fake_jobs, real_jobs], ignore_index=True)
    print(f"Loaded {len(fake_jobs)} fake jobs and {len(real_jobs)} real jobs.")
    print(f"Total jobs loaded: {len(all_jobs_df)}")

    # Assign jobs to sets (15 for Group A, 15 for Groups B, C, D)
    # This assumes you have at least 15 fake and 15 real jobs to draw from for each set.
    # For simplicity, let's create two sets of 15 jobs each, ensuring a mix.
    # You'll need to adjust this logic if your total job count is different or you want a specific real/fake ratio.
    
    # Ensure enough jobs for both sets
    if len(all_jobs_df) < 30:
        raise ValueError("Not enough job postings to create two sets of 15. Need at least 30 total jobs.")

    # Separate real and fake jobs for balanced sampling
    all_real_jobs = all_jobs_df[all_jobs_df['is_scam_job'] == False].copy()
    all_fake_jobs = all_jobs_df[all_jobs_df['is_scam_job'] == True].copy()

    if len(all_real_jobs) < 15 or len(all_fake_jobs) < 15:
        raise ValueError("Need at least 15 real and 15 fake jobs to create balanced sets.")

    # Randomly sample for set A (e.g., 7 fake, 8 real)
    job_set_A_fake = all_fake_jobs.sample(n=7, random_state=42)
    job_set_A_real = all_real_jobs.sample(n=8, random_state=42)
    job_set_A = pd.concat([job_set_A_fake, job_set_A_real], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
    job_set_A['job_id'] = job_set_A['job_id'].astype(str) # Ensure job_id is string

    # Remaining jobs for set BCD (e.g., 8 fake, 7 real - from those not in set A)
    remaining_fake_jobs = all_fake_jobs.drop(job_set_A_fake.index)
    remaining_real_jobs = all_real_jobs.drop(job_set_A_real.index)

    job_set_BCD_fake = remaining_fake_jobs.sample(n=8, random_state=42)
    job_set_BCD_real = remaining_real_jobs.sample(n=7, random_state=42)
    job_set_BCD = pd.concat([job_set_BCD_fake, job_set_BCD_real], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
    job_set_BCD['job_id'] = job_set_BCD['job_id'].astype(str) # Ensure job_id is string

    # Store these sets globally for access by the session
    app.config['JOB_SETS'] = {
        'A': job_set_A.to_dict(orient='records'),
        'BCD': job_set_BCD.to_dict(orient='records')
    }
    print("Job sets prepared for groups A and BCD.")

except FileNotFoundError as e:
    print(f"ERROR: Job data file not found: {e}. Please ensure '{DATA_DIR}' exists and contains '{AI_REFINED_FAKE_JOBS_FILE}' and '{MANUALLY_COLLECTED_REAL_JOBS_FILE}'.")
    app.config['JOB_SETS'] = {'A': [], 'BCD': []} # Initialize empty to prevent further errors
except ValueError as e:
    print(f"ERROR: Not enough jobs or imbalance for sets: {e}")
    app.config['JOB_SETS'] = {'A': [], 'BCD': []}


# --- Desperation Index Questions and Scoring ---
# Define the questions for the desperation index
DESPERATION_QUESTIONS = [
    "Are you urgently seeking a new job?",
    "Does your current financial/life situation urgently depend on finding a new job soon?",
    "Are you willing to accept a job that is not your ideal role?",
    "Do you feel pressure to secure employment quickly?",
    "Are you likely to overlook minor red flags in a job posting if the pay is good?"
]

# --- Exit Survey Questions ---
JOBS_INTERACTED_RANGES = ["Less than 5", "5-10", "11-15"]
LOW_INTERACTION_REASONS = [
    "Roles were not a fit",
    "Salaries too low",
    "I got bored or tired",
    "Technical issues",
    "Other"
]

# Scoring for Likert scale (e.g., 1-5 where 5 is most desperate/high risk)
# We'll map answers to scores (e.g., 'Strongly Disagree': 0, 'Disagree': 5, 'Neutral': 10, 'Agree': 15, 'Strongly Agree': 20)
# This mapping will be handled in the POST request.

# --- Routes ---

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    GET: Displays the login form.
    POST: Processes login credentials.
    """
    if request.method == 'GET': # Only clear session on GET request to login page
        session.clear()
        print("DEBUG: GET / - Session explicitly cleared.")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists and password matches
        user_match = users_df[(users_df['username'] == username) & (users_df['password'] == password)]

        if not user_match.empty:
            # Store user info in session
            session['user_id'] = username
            session['group'] = user_match['group'].iloc[0] # Get the assigned group
            # Initialize interacted_job_ids as a list for JSON serialization
            session['interacted_job_ids'] = []
            print(f"User {username} logged in. Assigned to group: {session['group']}")
            return redirect(url_for('desperation_index'))
        else:
            print(f"DEBUG: Login failed for user {username}.")
            return render_template('login.html', error="Invalid username or password.")
    print(f"DEBUG: Displaying login page. Current session: {session.get('user_id')}")
    return render_template('login.html', error=None)

@app.route('/desperation_index', methods=['GET', 'POST'])
def desperation_index():
    """
    Handles the desperation index questionnaire.
    GET: Displays the questions.
    POST: Processes answers and stores results.
    """
    print(f"DEBUG: Entering desperation_index route. Session user_id: {session.get('user_id')}")
    if 'user_id' not in session:
        print("DEBUG: User not in session, redirecting to login from desperation_index.")
        return redirect(url_for('login')) # Redirect to login if not authenticated

    if request.method == 'POST':
        user_id = session['user_id']
        group = session['group']
        timestamp = datetime.now().isoformat()

        answers = {}
        desperation_score = 0
        score_mapping = {
            'Strongly Disagree': 0,
            'Disagree': 5,
            'Neutral': 10,
            'Agree': 15,
            'Strongly Agree': 20
        }

        for i, question_text in enumerate(DESPERATION_QUESTIONS):
            question_key = f'q{i+1}'
            answer = request.form.get(question_key)
            answers[question_key] = answer
            desperation_score += score_mapping.get(answer, 0) # Add score, default to 0 if answer not found

        # Store results in CSV
        with open(DESPERATION_RESULTS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp, user_id, group,
                answers.get('q1'), answers.get('q2'), answers.get('q3'), answers.get('q4'), answers.get('q5'),
                desperation_score
            ])
        print(f"Desperation index submitted for user {user_id} (Score: {desperation_score}).")

        # Initialize interacted_job_ids for tracking which jobs a user *has* interacted with (for disabling buttons)
        session['interacted_job_ids'] = [] #set()
        print(f"DEBUG: Session state BEFORE redirect to job_display: user_id={session.get('user_id')}, group={session.get('group')}, interacted_job_ids={session.get('interacted_job_ids')}")
        return redirect(url_for('job_display'))
    
    # GET request: Display the form
    questions_with_index = list(enumerate(DESPERATION_QUESTIONS))
    print(f"DEBUG: Displaying desperation_index form for user {session.get('user_id')}.")
    return render_template('desperation_index.html', questions=questions_with_index)

@app.route('/job_display', methods=['GET', 'POST'])
def job_display():
    """
    Displays all job postings for the user's group as a scrollable board.
    Dynamically adds scam indicator based on group.
    """
    print(f"DEBUG: Entering job_display route. Current session: user_id={session.get('user_id')}, job_index={session.get('current_job_index')}")
    if 'user_id' not in session: # or 'current_job_index' not in session:
        print("DEBUG: Session missing user_id or current_job_index in job_display, redirecting to login.")
        return redirect(url_for('login'))

    user_id = session['user_id']
    group = session['group']
    #current_job_index = session['current_job_index']

    # Determine which job set to use based on group
    if group == 'A':
        job_set = app.config['JOB_SETS']['A']
    else: # Groups B, C, D
        job_set = app.config['JOB_SETS']['BCD']

    # Deep copy to avoid modifying the global app.config directly
    jobs_for_display = [job.copy() for job in job_set]

    # Retrieve interacted_job_ids as a set for efficient lookups
    current_interacted_ids = set(session.get('interacted_job_ids', []))

    # --- Dynamic Scam Information Logic ---
    for job in jobs_for_display:
        is_scam = job.get('is_scam_job', False) # Default to False if missing

        # Group A: Show "Is this a scam?" question
        job['show_scam_question'] = (group == 'A')
        
        # Group B: Dynamic Scam Risk Score
        if group == 'B':
            if is_scam:
                job['scam_risk_score'] = random.randint(58, 89) # High risk for fake jobs
            else:
                job['scam_risk_score'] = random.randint(1, 5)   # Low risk for real jobs
        else:
            job['scam_risk_score'] = None # Not applicable for other groups

        # Group C: Dynamic Scam Sign (Green/Red)
        if group == 'C':
            job['scam_sign_color'] = 'green' if not is_scam else 'red'
            job['scam_sign_text'] = 'Legitimate Job' if not is_scam else 'Potential Scam Risk'
        else:
            job['scam_sign_color'] = None
            job['scam_sign_text'] = None

        # Group D: Dynamic Scam Warning Text
        if group == 'D':
            if is_scam:
                job['scam_warning_text'] = "WARNING: This posting contains elements consistent with common scam patterns. Proceed with extreme caution."
            else:
                job['scam_warning_text'] = "There is always a risk of scam in job postings, proceed with caution."
        else:
            job['scam_warning_text'] = None
            
        # Add a flag to track if this job has been interacted with in the current session
        #job['interacted'] = job['job_id'] in session.get('interacted_job_ids', set())

        # Check if job has been interacted with in the current session (for disabling individual buttons)
        job['interacted'] = job['job_id'] in current_interacted_ids

    print(f"DEBUG: Displaying job board for user {user_id} in group {group}. Total jobs: {len(jobs_for_display)}")
    print(f"DEBUG: Sample job (first) after processing: {jobs_for_display[0] if jobs_for_display else 'No jobs'}")

    return render_template(
        'job_board.html',
        jobs=jobs_for_display, # Pass the entire list of processed jobs
        user_group=group,
        #total_jobs_in_set=len(job_set)
    )

@app.route('/record_job_interaction', methods=['POST'])
def record_job_interaction():
    """
    AJAX endpoint to record user interactions with individual job tiles.
    """
    print(f"DEBUG: Entering record_job_interaction route. Session user_id: {session.get('user_id')}")
    if 'user_id' not in session:
        print("DEBUG: User not in session for record_job_interaction, returning 401.")
        return jsonify(success=False, message="Not logged in"), 401

    user_id = session['user_id']
    group = session['group']
    timestamp = datetime.now().isoformat()

    data = request.get_json() # Get JSON data from the AJAX request
    job_id = str(data.get('job_id'))
    interaction_type = data.get('interaction_type') # e.g., 'is_scam_yes', 'is_scam_no', 'applied', 'link_clicked'
    
    # --- UPDATED: Handle scam_reason_text as a list of reasons ---
    scam_reason_list = data.get('scam_reason_text', [])
    if isinstance(scam_reason_list, list):
        scam_reason_text = ", ".join(scam_reason_list) # Store as comma-separated string
    else: # Fallback if it's somehow not a list
        scam_reason_text = str(scam_reason_list).strip()
    # --- END UPDATED ---
    time_on_page_seconds = data.get('time_on_page_seconds', 0)

    # Find the job_index_in_set for the current job_id
    job_set_for_user = app.config['JOB_SETS']['A'] if group == 'A' else app.config['JOB_SETS']['BCD']
    job_index_in_set = -1

    # --- Debugging: Print job_ids for comparison ---
    print(f"DEBUG: Received job_id from frontend: '{job_id}' (type: {type(job_id)})")
    # Collect all job_ids in the user's set for debugging
    all_set_job_ids = [job_item.get('job_id') for job_item in job_set_for_user]
    print(f"DEBUG: Job IDs in user's set: {all_set_job_ids}")
    # --- End Debugging ---

    for idx, job_item in enumerate(job_set_for_user):
        # Ensure comparison is between strings
        if str(job_item.get('job_id')) == job_id:
            job_index_in_set = idx
            break
    
    if job_index_in_set == -1:
        print(f"ERROR: Job ID {job_id} not found in user's job set.")
        return jsonify(success=False, message="Job not found"), 400

    # Retrieve, modify, and store interacted_job_ids as a list
    interacted_job_ids_list = session.get('interacted_job_ids', [])
    if job_id not in interacted_job_ids_list: # Check if already in list to avoid duplicates
        interacted_job_ids_list.append(job_id)
    session['interacted_job_ids'] = interacted_job_ids_list # Store back the list

    # Log the interaction
    with open(JOB_RESPONSES_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            user_id,
            group,
            job_id,
            job_index_in_set,
            'yes' if interaction_type == 'is_scam_yes' else ('no' if interaction_type == 'is_scam_no' else ''), # is_scam_response
            scam_reason_text, # Will now be comma-separated string of reasons
            'yes' if interaction_type == 'applied' else 'no', # applied_clicked
            'yes' if interaction_type == 'link_clicked' else 'no', # link_interacted
            time_on_page_seconds
        ])
    print(f"DEBUG: Recorded interaction '{interaction_type}' for job {job_id} by user {user_id}.")
    print(f"DEBUG: Current interacted_job_ids in session: {session['interacted_job_ids']}")

    return jsonify(success=True)

@app.route('/exit_survey', methods=['GET', 'POST'])
def exit_survey():
    """
    Handles the post-study exit survey.
    GET: Displays the survey questions.
    POST: Processes answers and stores results.
    """
    print(f"DEBUG: Entering exit_survey route. Session user_id: {session.get('user_id')}")
    if 'user_id' not in session:
        print("DEBUG: User not in session, redirecting to login from exit_survey.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = session['user_id']
        group = session['group']
        timestamp = datetime.now().isoformat()

        jobs_interacted_range = request.form.get('jobs_interacted_range')
        low_interaction_reasons = request.form.getlist('low_interaction_reasons') # getlist for multiple checkboxes
        low_interaction_other_reason = request.form.get('low_interaction_other_reason', '').strip()

        # Convert list of reasons to a comma-separated string for CSV
        low_interaction_reasons_str = ", ".join(low_interaction_reasons)

        with open(EXIT_SURVEY_RESULTS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                user_id,
                group,
                jobs_interacted_range,
                low_interaction_reasons_str,
                low_interaction_other_reason
            ])
        print(f"DEBUG: Exit survey submitted for user {user_id}.")
        return redirect(url_for('thank_you'))

    # GET request: Display the form
    return render_template(
        'exit_survey.html',
        jobs_interacted_ranges=JOBS_INTERACTED_RANGES,
        low_interaction_reasons=LOW_INTERACTION_REASONS
    )

@app.route('/thank_you')
def thank_you():
    """
    Placeholder for the final thank you page.
    """
    print(f"DEBUG: Entering thank_you route. Session user_id: {session.get('user_id')}")
    session.clear() # Clear session after study completion
    print("DEBUG: Session cleared.")
    return "Thank you for participating! We will follow up via email. (Day 4)"


@app.route('/logout')
def logout():
    """
    Logs out the user by clearing the session.
    """
    print(f"DEBUG: Logging out user. Session user_id before clear: {session.get('user_id')}")
    session.pop('user_id', None)
    session.pop('group', None)
    session.pop('current_job_index', None)
    print("DEBUG: Session popped. Redirecting to login.")
    return redirect(url_for('login'))

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True) # debug=True for development. Set to False for production!
# Note: In a production environment, ensure to set debug=False and use a proper secret key.
# Also, consider using a more robust session management system (e.g., Flask-Login).