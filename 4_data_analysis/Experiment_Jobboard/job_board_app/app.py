"""
This file contains the Flask application, routing, and logic for login
and the desperation index, now using a PostgreSQL database via Flask-SQLAlchemy.
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy # NEW: Import SQLAlchemy
import pandas as pd # Still used for initial job data loading
import os
import csv # Still used for initial CSV header creation for historical data (though data will go to DB)
from datetime import datetime
from dotenv import load_dotenv
import random


# --- Flask App Initialization ---
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY") # Ensure this is set in your .env for local and Railway for production

# --- Database Configuration (NEW) ---
# Use DATABASE_URL environment variable for production (e.g., Railway)
# Fallback to SQLite for local development
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Suppress warning

db = SQLAlchemy(app) # Initialize SQLAlchemy

# --- Database Models (NEW) ---
# Define your database tables as Python classes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing ID
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    group = db.Column(db.String(1), nullable=False) # A, B, C, or D
    has_logged_in = db.Column(db.Boolean, default=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True) # Added email field

    def __repr__(self):
        return f"<User {self.username} (Group {self.group})>"

class DesperationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.String(80), nullable=False) # Store username as user_id
    group = db.Column(db.String(1), nullable=False)
    age_range = db.Column(db.String(20), nullable=False)
    q1_answer = db.Column(db.String(50), nullable=False)
    q2_answer = db.Column(db.String(50), nullable=False)
    q3_answer = db.Column(db.String(50), nullable=False)
    q4_answer = db.Column(db.String(50), nullable=False)
    q5_answer = db.Column(db.String(50), nullable=False)
    desperation_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<DesperationResult {self.user_id} Score: {self.desperation_score}>"

class JobResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(1), nullable=False)
    job_id = db.Column(db.String(50), nullable=False)
    job_index_in_set = db.Column(db.Integer, nullable=False)
    is_scam_job = db.Column(db.Boolean, nullable=False) # Actual scam status
    is_scam_response = db.Column(db.String(10), nullable=True) # User's response ('yes', 'no', or empty)
    scam_reason_text = db.Column(db.Text, nullable=True) # Comma-separated reasons
    applied_clicked = db.Column(db.Boolean, default=False, nullable=False)
    link_interacted = db.Column(db.Boolean, default=False, nullable=False)
    time_on_job_page_seconds = db.Column(db.Integer, nullable=False)
    desperation_score = db.Column(db.Integer, nullable=False)
    age_range = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<JobResponse {self.user_id} Job {self.job_id} Type: {self.interaction_type}>"

class ExitSurveyResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(1), nullable=False)
    jobs_interacted_range = db.Column(db.String(50), nullable=False)
    low_interaction_reasons = db.Column(db.Text, nullable=True)
    low_interaction_other_reason = db.Column(db.Text, nullable=True)
    scam_warning_feedback = db.Column(db.Text, nullable=True)
    scam_warning_other_feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<ExitSurveyResult {self.user_id}>"

# --- END Database Models ---


# --- File Paths (for initial job data loading only) ---
DATA_DIR = 'data'
AI_REFINED_FAKE_JOBS_FILE = os.path.join(DATA_DIR, 'llm_refined_30_fake_job_postings.csv')
MANUALLY_COLLECTED_REAL_JOBS_FILE = os.path.join(DATA_DIR, 'cleaned_real_jobs.csv')


# --- Job Data Loading and Preparation (remains mostly the same as it's static content) ---
all_jobs_df = pd.DataFrame()
JOB_DATA_COLUMNS = [
    'job_id','job_title', 'job_description', 'company_name', 'is_scam_job', # Essential for the study
    # 'location', 'employment_type', 'raw_description', 'source_platform', 'original_url', 'collection_date', 'notes' # Other columns from schema, can be loaded if needed for display/analysis
]

try:
    fake_jobs = pd.read_csv(AI_REFINED_FAKE_JOBS_FILE)
    real_jobs = pd.read_csv(MANUALLY_COLLECTED_REAL_JOBS_FILE)

    for col in JOB_DATA_COLUMNS:
        if col not in fake_jobs.columns:
            fake_jobs[col] = pd.NA
        if col not in real_jobs.columns:
            real_jobs[col] = pd.NA

    fake_jobs = fake_jobs[JOB_DATA_COLUMNS]
    real_jobs = real_jobs[JOB_DATA_COLUMNS]

    all_jobs_df = pd.concat([fake_jobs, real_jobs], ignore_index=True)
    print(f"Loaded {len(fake_jobs)} fake jobs and {len(real_jobs)} real jobs.")
    print(f"Total jobs loaded: {len(all_jobs_df)}")

    all_real_jobs = all_jobs_df[all_jobs_df['is_scam_job'] == False].copy()
    all_fake_jobs = all_jobs_df[all_jobs_df['is_scam_job'] == True].copy()

    if len(all_real_jobs) < 12 or len(all_fake_jobs) < 11:
        raise ValueError("Not enough real or fake jobs to create a balanced set of 10 real and 11 fake jobs.")

    common_job_set_fake = all_fake_jobs.sample(n=11, random_state=42).copy()
    common_job_set_real = all_real_jobs.sample(n=10, random_state=42).copy()
    
    common_job_set = pd.concat([common_job_set_fake, common_job_set_real], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
    common_job_set['job_id'] = common_job_set['job_id'].astype(str)

    app.config['JOB_SETS'] = {
        'A': common_job_set.to_dict(orient='records'),
        'BCD': common_job_set.to_dict(orient='records')
    }
    print(f"Common job set prepared for all groups. Total jobs: {len(common_job_set)}")

except FileNotFoundError as e:
    print(f"ERROR: Job data file not found: {e}. Please ensure '{DATA_DIR}' exists and contains '{AI_REFINED_FAKE_JOBS_FILE}' and '{MANUALLY_COLLECTED_REAL_JOBS_FILE}'.")
    app.config['JOB_SETS'] = {'A': [], 'BCD': []}
except ValueError as e:
    print(f"ERROR: Not enough jobs or imbalance for sets: {e}")
    app.config['JOB_SETS'] = {'A': [], 'BCD': []}


# --- Desperation Index Questions and Scoring ---
DESPERATION_QUESTIONS = [
    "Are you urgently seeking a new job?",
    "Does your current financial/life situation urgently depend on finding a new job soon?",
    "Are you willing to accept a job that is not your ideal role?",
    "Do you feel pressure to secure employment quickly?",
    "Are you likely to overlook minor red flags in a job posting if the pay is good?"
]

AGE_RANGES = [
    "18-24", "25-34", "35-44", "45-54", "55-64", "65+"
]

# --- Exit Survey Questions ---
JOBS_INTERACTED_RANGES = ["Less than 5", "5-10", "11-15", "16-20", "More than 20"]
LOW_INTERACTION_REASONS = [
    "Roles were not a fit", "Salaries too low", "I got bored or tired", "Technical issues", "Other"
]

SCAM_WARNING_FEEDBACK_OPTIONS = [
    "It helped me quickly identify potential scam jobs.",
    "I sometimes found it distracting.",
    "It made me more cautious about applying to certain jobs.",
    "I felt it was too alarmist or made me overly suspicious.",
    "It increased my trust in the job board.",
    "It felt helpful and informative.",
    "It didn't significantly change how I interacted with jobs.",
    "I found it confusing.",
    "I tended to ignore it.",
    "Other"
]

# --- Routes ---

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    GET: Displays the login form.
    POST: Processes login credentials.
    """
    if request.method == 'GET':
        session.clear()
        print("DEBUG: GET / - Session explicitly cleared.")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query user from database
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            # Check if user has already logged in
            if user.has_logged_in:
                print(f"DEBUG: User {username} tried to log in again. Access denied.")
                return render_template('login.html', error="This account has already completed the study or is currently in use. Please contact support if you believe this is an error.")
            
            # If not logged in before, proceed with login
            session['user_id'] = user.username
            session['group'] = user.group
            session['interacted_job_ids'] = []

            # Mark user as logged in in the database and commit
            user.has_logged_in = True
            db.session.commit() # Commit the change to the database
            print(f"User {user.username} logged in successfully. Marked as 'has_logged_in'. Assigned to group: {user.group}")
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
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = session['user_id']
        group = session['group']
        age_range = request.form.get('age_range')

        answers = {}
        desperation_score = 0
        score_mapping = {
            'Strongly Disagree': 0, 'Disagree': 5, 'Neutral': 10, 'Agree': 15, 'Strongly Agree': 20
        }

        for i, question_text in enumerate(DESPERATION_QUESTIONS):
            question_key = f'q{i+1}'
            answer = request.form.get(question_key)
            answers[question_key] = answer
            desperation_score += score_mapping.get(answer, 0)

        # Store desperation_score and age_range in session for later use in job_responses
        session['desperation_score'] = desperation_score
        session['age_range'] = age_range

        # Create and save DesperationResult to database
        new_desperation_result = DesperationResult(
            user_id=user_id,
            group=group,
            age_range=age_range,
            q1_answer=answers.get('q1'),
            q2_answer=answers.get('q2'),
            q3_answer=answers.get('q3'),
            q4_answer=answers.get('q4'),
            q5_answer=answers.get('q5'),
            desperation_score=desperation_score
        )
        db.session.add(new_desperation_result)
        db.session.commit() # Commit the new record
        print(f"Desperation index submitted for user {user_id} (Score: {desperation_score}).")

        return redirect(url_for('job_display'))
    
    questions_with_index = list(enumerate(DESPERATION_QUESTIONS))
    print(f"DEBUG: Displaying desperation_index form for user {session.get('user_id')}.")
    return render_template('desperation_index.html', questions=questions_with_index, age_ranges=AGE_RANGES)

@app.route('/job_display', methods=['GET'])
def job_display():
    """
    Displays all job postings for the user's group as a scrollable board.
    Dynamically adds scam indicator based on group.
    """
    print(f"DEBUG: Entering job_display route (GET). Current session: user_id={session.get('user_id')}")
    if 'user_id' not in session:
        print("DEBUG: User not in session, redirecting to login from job_display.")
        return redirect(url_for('login'))

    user_id = session['user_id']
    group = session['group']
    
    job_set = app.config['JOB_SETS']['BCD']

    jobs_for_display = [job.copy() for job in job_set]

    current_interacted_ids = set(session.get('interacted_job_ids', []))

    for job in jobs_for_display:
        is_scam = job.get('is_scam_job', False)

        job['show_scam_question'] = (group == 'A')
        
        if group == 'B':
            if is_scam:
                job['scam_risk_score'] = random.randint(58, 89)
            else:
                job['scam_risk_score'] = random.randint(1, 5)
        else:
            job['scam_risk_score'] = None

        if group == 'C':
            job['scam_sign_color'] = 'green' if not is_scam else 'red'
            job['scam_sign_text'] = 'Legitimate Job' if not is_scam else 'Potential Scam Risk'
        else:
            job['scam_sign_color'] = None
            job['scam_sign_text'] = None

        if group == 'D':
            if is_scam:
                job['scam_warning_text'] = "WARNING: This posting contains elements consistent with common scam patterns. Proceed with extreme caution."
            else:
                job['scam_warning_text'] = "There is always a risk of scam in job postings, proceed with caution."
        else:
            job['scam_warning_text'] = None
            
        job['interacted'] = job['job_id'] in current_interacted_ids

    print(f"DEBUG: Displaying job board for user {user_id} in group {group}. Total jobs: {len(jobs_for_display)}")
    print(f"DEBUG: Sample job (first) after processing: {jobs_for_display[0] if jobs_for_display else 'No jobs'}")

    return render_template(
        'job_board.html',
        jobs=jobs_for_display,
        user_group=group,
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
    
    data = request.get_json()
    job_id = str(data.get('job_id'))
    interaction_type = data.get('interaction_type')
    
    scam_reason_list = data.get('scam_reason_text', [])
    scam_reason_text = ", ".join(scam_reason_list) if isinstance(scam_reason_list, list) else str(scam_reason_list).strip()
    
    time_on_page_seconds = data.get('time_on_page_seconds', 0)
    is_scam_job_actual = data.get('is_scam_job_actual')

    # Retrieve desperation_score and age_range from session
    desperation_score_session = session.get('desperation_score', 'N/A')
    age_range_session = session.get('age_range', 'N/A')

    # Create and save JobResponse to database
    new_job_response = JobResponse(
        user_id=user_id,
        group=group,
        job_id=job_id,
        # job_index_in_set is not strictly needed in DB model if job_id is unique,
        # but keeping it for consistency with previous CSV structure.
        # We need to find it from the job_set.
        job_index_in_set=[idx for idx, job_item in enumerate(app.config['JOB_SETS']['BCD']) if str(job_item.get('job_id')) == job_id][0],
        is_scam_job=is_scam_job_actual,
        is_scam_response='yes' if interaction_type == 'is_scam_yes' else ('no' if interaction_type == 'is_scam_no' else None),
        scam_reason_text=scam_reason_text if interaction_type.startswith('is_scam_') else None, # Only store if scam response
        applied_clicked=(interaction_type == 'applied'),
        link_interacted=(interaction_type == 'link_clicked'),
        time_on_job_page_seconds=time_on_page_seconds,
        desperation_score=desperation_score_session,
        age_range=age_range_session
    )
    db.session.add(new_job_response)
    db.session.commit() # Commit the new record
    print(f"DEBUG: Recorded interaction '{interaction_type}' for job {job_id} by user {user_id}.")

    # Update interacted_job_ids in session
    interacted_job_ids_list = session.get('interacted_job_ids', [])
    if job_id not in interacted_job_ids_list:
        interacted_job_ids_list.append(job_id)
    session['interacted_job_ids'] = interacted_job_ids_list
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
        
        jobs_interacted_range = request.form.get('jobs_interacted_range')
        low_interaction_reasons = request.form.getlist('low_interaction_reasons')
        low_interaction_other_reason = request.form.get('low_interaction_other_reason', '').strip()
        
        scam_warning_feedback = request.form.getlist('scam_warning_feedback')
        scam_warning_other_feedback = request.form.get('scam_warning_other_feedback', '').strip()

        low_interaction_reasons_str = ", ".join(low_interaction_reasons)
        scam_warning_feedback_str = ", ".join(scam_warning_feedback)

        # Create and save ExitSurveyResult to database
        new_exit_survey_result = ExitSurveyResult(
            user_id=user_id,
            group=group,
            jobs_interacted_range=jobs_interacted_range,
            low_interaction_reasons=low_interaction_reasons_str,
            low_interaction_other_reason=low_interaction_other_reason,
            scam_warning_feedback=scam_warning_feedback_str,
            scam_warning_other_feedback=scam_warning_other_feedback
        )
        db.session.add(new_exit_survey_result)
        db.session.commit() # Commit the new record
        print(f"DEBUG: Exit survey submitted for user {user_id}.")
        return redirect(url_for('thank_you'))

    return render_template(
        'exit_survey.html',
        jobs_interacted_ranges=JOBS_INTERACTED_RANGES,
        low_interaction_reasons=LOW_INTERACTION_REASONS,
        scam_warning_feedback_options=SCAM_WARNING_FEEDBACK_OPTIONS,
        user_group=session['group']
    )

@app.route('/thank_you')
def thank_you():
    """
    Renders the final thank you page after study completion.
    """
    print(f"DEBUG: Entering thank_you route. Session user_id: {session.get('user_id')}")
    session.clear() # Clear session after study completion
    print("DEBUG: Session cleared.")
    return render_template('thank_you.html')


@app.route('/logout')
def logout():
    """
    Logs out the user by clearing the session.
    """
    print(f"DEBUG: Logging out user. Session user_id before clear: {session.get('user_id')}")
    session.pop('user_id', None)
    session.pop('group', None)
    session.pop('interacted_job_ids', None)
    session.pop('desperation_score', None)
    session.pop('age_range', None)
    print("DEBUG: Session popped. Redirecting to login.")
    return redirect(url_for('login'))

# --- Run the App ---
if __name__ == '__main__':
    with app.app_context(): # NEW: Ensures app context for db operations
        db.create_all() # Create database tables if they don't exist
    app.run(debug=True)
