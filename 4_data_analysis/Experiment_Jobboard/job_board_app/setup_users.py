import pandas as pd
import os
import random
import string

# Define the path to your users CSV file
USERS_FILE = 'users.csv'

# Define the groups for your study
STUDY_GROUPS = ['A', 'B', 'C', 'D']

def generate_random_string(length=8):
    """Generates a random alphanumeric string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def setup_users():
    """
    Reads the users.csv, generates usernames/passwords if missing,
    assigns groups randomly and balances them, and adds a 'has_logged_in' flag.
    """
    print(f"Starting user setup for {USERS_FILE}...")

    # Load existing users or create an empty DataFrame if file doesn't exist
    if os.path.exists(USERS_FILE):
        users_df = pd.read_csv(USERS_FILE)
        print(f"Loaded {len(users_df)} existing users.")
    else:
        # If users.csv doesn't exist, create with 'email' as the starting point
        users_df = pd.DataFrame(columns=['email'])
        print(f"'{USERS_FILE}' not found. Creating a new one with 'email' column.")

    # --- NEW: Ensure 'username', 'password' columns exist and generate if missing ---
    if 'username' not in users_df.columns:
        users_df['username'] = None
    if 'password' not in users_df.columns:
        users_df['password'] = None
    if 'email' not in users_df.columns: # Ensure email column exists if not already there
        users_df['email'] = None

    # Generate usernames and passwords for entries where they are missing
    for index, row in users_df.iterrows():
        if pd.isna(row['username']):
            users_df.at[index, 'username'] = f"user_{generate_random_string(6)}"
        if pd.isna(row['password']):
            users_df.at[index, 'password'] = generate_random_string(8)
    # --- END NEW ---

    # Ensure 'group' and 'has_logged_in' columns exist (existing logic)
    if 'group' not in users_df.columns:
        users_df['group'] = None # Initialize with None
    if 'has_logged_in' not in users_df.columns:
        users_df['has_logged_in'] = False # Initialize with False

    # Get counts of already assigned users per group
    group_counts = users_df['group'].value_counts().to_dict()
    for group in STUDY_GROUPS:
        group_counts.setdefault(group, 0) # Ensure all groups are in the dict, even if count is 0

    # Identify users who need a group assignment
    unassigned_users = users_df[users_df['group'].isnull()]

    if not unassigned_users.empty:
        print(f"Found {len(unassigned_users)} unassigned users. Assigning groups...")
        
        # Randomly assign groups to unassigned users, trying to balance them
        for index, row in unassigned_users.iterrows():
            # Find the group with the minimum number of assigned users
            min_count = float('inf')
            target_group = None
            
            # Shuffle groups to ensure true randomness if counts are equal
            shuffled_groups = random.sample(STUDY_GROUPS, len(STUDY_GROUPS)) 
            
            for group in shuffled_groups:
                if group_counts[group] < min_count:
                    min_count = group_counts[group]
                    target_group = group
            
            users_df.at[index, 'group'] = target_group
            group_counts[target_group] += 1
            users_df.at[index, 'has_logged_in'] = False # Ensure new users are set to False

        print("Group assignment complete.")
    else:
        print("No unassigned users found. All users have a group.")

    # Ensure 'has_logged_in' is False for any new users added without this column
    users_df['has_logged_in'] = users_df['has_logged_in'].fillna(False)

    # Save the updated DataFrame back to CSV
    users_df.to_csv(USERS_FILE, index=False)
    print(f"Updated '{USERS_FILE}' saved successfully.")
    print("\nFinal user data preview (first 5 rows):")
    print(users_df.head())
    print("\nFinal group distribution:")
    print(users_df['group'].value_counts())
    print("\n'has_logged_in' status:")
    print(users_df['has_logged_in'].value_counts())

if __name__ == "__main__":
    setup_users()
