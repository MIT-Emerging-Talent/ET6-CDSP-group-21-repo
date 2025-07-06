import pandas as pd
import os
import random
import string
from flask import Flask # Import Flask to create app context
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from dotenv import load_dotenv # To load DATABASE_URL for local testing

# Define the path to your users CSV file (now used for initial import only if needed)
USERS_FILE = 'users.csv'

# Define the groups for your study
STUDY_GROUPS = ['A', 'B', 'C', 'D']

# --- Flask App and Database Setup (mimicking app.py for context) ---
# This small Flask app setup is needed here to get a db context for SQLAlchemy
app = Flask(__name__)
load_dotenv() # Load .env variables for DATABASE_URL if present
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model (must match the one in app.py exactly)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    group = db.Column(db.String(1), nullable=False)
    has_logged_in = db.Column(db.Boolean, default=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return f"<User {self.username} (Group {self.group})>"
# --- End Flask App and Database Setup ---


def generate_random_string(length=8):
    """Generates a random alphanumeric string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def setup_users_in_db():
    """
    Reads the users.csv (if exists), generates usernames/passwords if missing,
    assigns groups randomly and balances them, and adds users to the database.
    """
    print(f"Starting user setup for database...")

    with app.app_context(): # Essential for database operations outside of Flask routes
        db.create_all() # Ensure tables are created if not already

        # Load existing users from the database
        existing_users_in_db = User.query.all()
        existing_usernames = {u.username for u in existing_users_in_db}
        existing_emails = {u.email for u in existing_users_in_db if u.email}
        print(f"Found {len(existing_users_in_db)} existing users in the database.")

        # Try to load users from users.csv (if it exists)
        users_from_csv_df = pd.DataFrame()
        if os.path.exists(USERS_FILE):
            users_from_csv_df = pd.read_csv(USERS_FILE)
            print(f"Loaded {len(users_from_csv_df)} users from '{USERS_FILE}'.")
        else:
            print(f"'{USERS_FILE}' not found. Will only process users already in DB (if any).")

        new_users_to_add = []
        for index, row in users_from_csv_df.iterrows():
            email = row.get('email')
            # Skip if email already exists in DB, or if username already exists
            if email and email in existing_emails:
                print(f"Skipping user with email {email}: Already exists in database.")
                continue
            if row.get('username') and row['username'] in existing_usernames:
                print(f"Skipping user with username {row['username']}: Already exists in database.")
                continue

            # Generate username and password if missing from CSV
            username = row.get('username') if pd.notna(row.get('username')) else f"user_{generate_random_string(6)}"
            password = row.get('password') if pd.notna(row.get('password')) else generate_random_string(8)

            # Check for username uniqueness again before adding
            if User.query.filter_by(username=username).first():
                print(f"Generated username {username} already exists, generating new one.")
                username = f"user_{generate_random_string(6)}" # Regenerate if clash

            new_users_to_add.append({
                'email': email,
                'username': username,
                'password': password,
                'group': None, # Will be assigned below
                'has_logged_in': False
            })

        if not new_users_to_add and not existing_users_in_db:
            print("No users to process or add. Please ensure your users.csv has data.")
            return

        # Combine existing DB users with new users from CSV for group assignment logic
        # Convert existing DB users to a list of dicts for easier manipulation
        all_users_data = [
            {
                'email': u.email,
                'username': u.username,
                'password': u.password,
                'group': u.group,
                'has_logged_in': u.has_logged_in
            } for u in existing_users_in_db
        ]
        all_users_data.extend(new_users_to_add)
        
        # Create a temporary DataFrame for group assignment logic
        temp_df = pd.DataFrame(all_users_data)

        # Get counts of already assigned users per group
        group_counts = temp_df['group'].value_counts().to_dict()
        for group in STUDY_GROUPS:
            group_counts.setdefault(group, 0)

        # Identify users who need a group assignment (those with group=None)
        unassigned_indices = temp_df[temp_df['group'].isnull()].index

        if not unassigned_indices.empty:
            print(f"Found {len(unassigned_indices)} users needing group assignments. Assigning...")
            for idx in unassigned_indices:
                min_count = float('inf')
                target_group = None
                shuffled_groups = random.sample(STUDY_GROUPS, len(STUDY_GROUPS))
                
                for group in shuffled_groups:
                    if group_counts[group] < min_count:
                        min_count = group_counts[group]
                        target_group = group
                
                temp_df.at[idx, 'group'] = target_group
                group_counts[target_group] += 1
                temp_df.at[idx, 'has_logged_in'] = False # Ensure new users are set to False

            print("Group assignment complete for new users.")
        else:
            print("No users needing group assignments. All users in the combined set have a group.")

        # Now, update/add users to the database based on the temp_df
        for index, row in temp_df.iterrows():
            user = User.query.filter_by(username=row['username']).first()
            if user:
                # Update existing user
                user.email = row['email']
                user.password = row['password']
                user.group = row['group']
                user.has_logged_in = row['has_logged_in']
            else:
                # Add new user
                new_user = User(
                    email=row['email'],
                    username=row['username'],
                    password=row['password'],
                    group=row['group'],
                    has_logged_in=row['has_logged_in']
                )
                db.session.add(new_user)
        
        db.session.commit() # Commit all changes to the database
        print("Database updated successfully with user data.")

        # For verification, fetch and display from DB
        final_users_in_db = User.query.all()
        final_df = pd.DataFrame([
            {'email': u.email, 'username': u.username, 'password': u.password, 'group': u.group, 'has_logged_in': u.has_logged_in}
            for u in final_users_in_db
        ])

        print("\nFinal user data preview from database (first 5 rows):")
        print(final_df.head())
        print("\nFinal group distribution from database:")
        print(final_df['group'].value_counts())
        print("\n'has_logged_in' status from database:")
        print(final_df['has_logged_in'].value_counts())

        # Optionally, save the final state to a CSV for your records (not used by app.py)
        final_df.to_csv("users_final_db_state.csv", index=False)
        print("\nFinal database state also saved to 'users_final_db_state.csv' for your reference.")


if __name__ == "__main__":
    setup_users_in_db()