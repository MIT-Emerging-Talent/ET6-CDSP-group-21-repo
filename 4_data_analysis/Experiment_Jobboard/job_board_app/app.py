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

    # Remaining jobs for set BCD (e.g., 8 fake, 7 real - from those not in set A)
    remaining_fake_jobs = all_fake_jobs.drop(job_set_A_fake.index)
    remaining_real_jobs = all_real_jobs.drop(job_set_A_real.index)

    job_set_BCD_fake = remaining_fake_jobs.sample(n=8, random_state=42)
    job_set_BCD_real = remaining_real_jobs.sample(n=7, random_state=42)
    job_set_BCD = pd.concat([job_set_BCD_fake, job_set_BCD_real], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)

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
        # --- TARGETED FIX: Re-set current_job_index just before redirect ---
        # This ensures it's explicitly present in the session for the next request.
        session['current_job_index'] = 0 
        print(f"DEBUG: Session state BEFORE redirect to job_display: user_id={session.get('user_id')}, group={session.get('group')}, job_index={session.get('current_job_index')}")
        # Redirect to the next part of the study (Day 2's job display)
        return redirect(url_for('job_display')) # This route will be implemented on Day 2
    
    # GET request: Display the form
    questions_with_index = list(enumerate(DESPERATION_QUESTIONS))
    print(f"DEBUG: Displaying desperation_index form for user {session.get('user_id')}.")
    return render_template('desperation_index.html', questions=questions_with_index)

@app.route('/job_display', methods=['GET', 'POST'])
def job_display():
    """
    Displays individual job postings and captures responses.
    """
    print(f"DEBUG: Entering job_display route. Current session: user_id={session.get('user_id')}, job_index={session.get('current_job_index')}")
    if 'user_id' not in session or 'current_job_index' not in session:
        print("DEBUG: Session missing user_id or current_job_index in job_display, redirecting to login.")
        return redirect(url_for('login'))

    user_id = session['user_id']
    group = session['group']
    current_job_index = session['current_job_index']

    # Determine which job set to use based on group
    if group == 'A':
        job_set = app.config['JOB_SETS']['A']
    else: # Groups B, C, D
        job_set = app.config['JOB_SETS']['BCD']

    # Check if there are jobs left to display
    if current_job_index >= len(job_set):
        # All jobs displayed, redirect to thank you page (Day 4)
        print(f"DEBUG: All jobs displayed for user {user_id}, redirecting to thank_you.")
        return redirect(url_for('thank_you')) # This route will be implemented on Day 4

    current_job = job_set[current_job_index]

    if request.method == 'POST':
        # Capture data from the current job interaction
        is_scam_response = request.form.get('is_scam') # 'yes' or 'no'
        scam_reason_text = request.form.get('scam_reason', '').strip()
        applied_clicked = request.form.get('applied_clicked', 'no') # 'yes' or 'no'
        link_interacted = request.form.get('link_interacted', 'no') # 'yes' or 'no'
        time_on_page = request.form.get('time_on_page', '0') # Time in seconds

        # Store job response
        with open(JOB_RESPONSES_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                user_id,
                group,
                current_job['job_id'],
                current_job_index, # Index within their assigned set
                is_scam_response,
                scam_reason_text,
                applied_clicked,
                link_interacted,
                time_on_page
            ])
        print(f"Job {current_job['job_id']} response recorded for user {user_id}.")

        # Increment job index and redirect to next job
        session['current_job_index'] += 1
        print(f"DEBUG: Session state AFTER job response and BEFORE redirect to next job: user_id={session.get('user_id')}, group={session.get('group')}, job_index={session.get('current_job_index')}")
        return redirect(url_for('job_display'))

    # GET request: Display the current job
    # Pass job data and group info to the template
    print(f"DEBUG: Displaying job {current_job_index + 1} for user {user_id} in group {group}.")
    return render_template(
        'job_posting.html',
        job=current_job,
        group=group,
        job_number=current_job_index + 1, # For display (1-indexed)
        total_jobs=len(job_set)
    )

@app.route('/track_interaction', methods=['POST'])
def track_interaction():
    """
    Endpoint for JavaScript to send interaction data (like apply clicks, link clicks)
    without submitting the main form.
    """
    print(f"DEBUG: Entering track_interaction route. Session user_id: {session.get('user_id')}")
    if 'user_id' not in session:
        return jsonify(success=False, message="Not logged in"), 401

    user_id = session['user_id']
    group = session['group']
    job_id = request.json.get('job_id')
    interaction_type = request.json.get('interaction_type') # e.g., 'apply_click', 'link_click'
    
    # You might want to log this to a separate, more detailed interaction log
    # or find a way to update the existing job_responses.csv.
    # For simplicity, we'll just print it for now.
    print(f"User {user_id} in group {group} interacted with job {job_id}: {interaction_type}")

    # A more robust solution would update the specific row in job_responses.csv
    # or log to a dedicated interaction file. For now, this is just a signal.
    
    return jsonify(success=True)


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