import pandas as pd
import os

# --- Configuration ---
# Base directory where all your 'batch_100_X_refined.csv' files are located.
# This should be '1_dataset/fakejobs_to_refine/' relative to your repository root.
# Assuming you run this script from the repository root or a similar relative path.
# If you run this script from '2_data_preparation/', adjust relative path:
# REFINED_FILES_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir, '1_dataset', 'fakejobs_to_refine'))

# Let's assume you'll run this from the root of your 'ET6-CDSP-group-21-repo'
# or you adjust this path to be absolute.
REFINED_FILES_DIR = '../1_datasets/fakejobs_refined/'

# List of expected refined batch filenames.
# Adjust this list if your batch names are different or you have more/fewer batches.
# Based on your previous setup, these would be 'A', 'B', 'C', 'D', 'E'.
# If you have a 'batch_84_Justina_refined.csv' from a unique split, add it here.
EXPECTED_BATCH_SUFFIXES = ['Alaa', 'Aseel', 'Justina', 'Majd', 'Rouaa', 'Geehan'] # Add more if you split into more files
PREFIX = "batch_84_" # Prefix used when splitting the files

# Output filename for the combined dataset
OUTPUT_COMBINED_CSV = '../1_datasets/aegean500_vs_Hypatia500_datasets/aegean500_fakejobs_llmrefined.csv'

# --- Script Logic ---
def combine_refined_datasets(input_dir, suffixes, prefix, output_path):
    """
    Combines individual refined batch CSVs into a single DataFrame and saves it.
    """
    all_dfs = []
    found_files_count = 0

    print(f"Starting to combine refined files from: {input_dir}")

    for suffix in suffixes:
        filename = f"{prefix}{suffix}_refined.csv"
        filepath = os.path.join(input_dir, filename)

        if os.path.exists(filepath):
            print(f"  Found and loading: {filename}")
            try:
                df = pd.read_csv(filepath)
                all_dfs.append(df)
                found_files_count += 1
            except Exception as e:
                print(f"  Error loading {filename}: {e}")
                print(f"  Skipping {filename} due to load error.")
        else:
            print(f"  File not found: {filename} (might still be processing or pushed)")

    if not all_dfs:
        print("No refined files were found or successfully loaded. Cannot combine.")
        print("Please ensure your team has pushed their refined CSVs and paths are correct.")
        return

    print(f"\nSuccessfully loaded {found_files_count} refined batch files.")

    try:
        # Concatenate all DataFrames row-wise
        combined_df = pd.concat(all_dfs, ignore_index=True)

        # Optional: Remove any potential duplicates based on 'job_id'
        # This is a good safeguard, though ideally not needed if splitting was perfect.
        if 'job_id' in combined_df.columns:
            initial_rows = len(combined_df)
            combined_df.drop_duplicates(subset=['job_id'], inplace=True)
            if len(combined_df) < initial_rows:
                print(f"  Removed {initial_rows - len(combined_df)} duplicate job entries.")
        else:
            print("  'job_id' column not found for checking duplicates.")

        # Save the final combined DataFrame
        combined_df.to_csv(output_path, index=False)
        print(f"\nSuccessfully combined {len(combined_df)} refined jobs into: {output_path}")
        print("You can now proceed with your NLP analysis on this file.")

    except Exception as e:
        print(f"An error occurred during concatenation or saving: {e}")

# --- Run the combination process ---
if __name__ == "__main__":
    # If you have a specific filename like 'batch_84_Justina_refined.csv' that
    # doesn't fit the batch_100_X pattern, you'll need to add its full path
    # to a list and pass it to a slightly modified function, or add its suffix
    # to the EXPECTED_BATCH_SUFFIXES list if its name still fits the pattern.
    # For example, if 'batch_84_Justina.csv' was 'batch_100_F.csv', then add 'F' to the list.
    # If it's a completely different naming scheme, you'd need to list it explicitly:
    # Example:
    # OTHER_REFINED_FILES = ['batch_84_Justina_refined.csv']
    # # Then modify the loop in combine_refined_datasets to also check these.
    # # For simplicity here, we stick to the batched naming scheme.

    combine_refined_datasets(REFINED_FILES_DIR, EXPECTED_BATCH_SUFFIXES, PREFIX, OUTPUT_COMBINED_CSV)
