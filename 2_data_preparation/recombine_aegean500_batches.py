import pandas as pd
import os

# --- Configuration ---
REFINED_FILES_DIR = "../1_datasets/fakejobs_refined/"

# List of expected refined batch filenames.
EXPECTED_BATCH_SUFFIXES = [
    "Alaa",
    "Aseel",
    "Justina",
    "Majd",
    "Rouaa",
    "Geehan",
]  # Add more if you split into more files
PREFIX = "batch_84_"  # Prefix used when splitting the files

# Output filename for the combined dataset
OUTPUT_COMBINED_CSV = (
    "../1_datasets/aegean500_vs_Hypatia500_datasets/aegean500_fakejobs_llmrefined.csv"  # noqa: E501
)


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
            print(f"  File not found: {filename} (might still be processing or pushed)")  # noqa: E501

    if not all_dfs:
        print("No refined files were found or successfully loaded. Cannot combine.")
        print(
            "Please ensure your team has pushed their refined CSVs and paths are correct."
        )  # noqa: E501
        return

    print(f"\nSuccessfully loaded {found_files_count} refined batch files.")

    try:
        # Concatenate all DataFrames row-wise
        combined_df = pd.concat(all_dfs, ignore_index=True)

        # Optional: Remove any potential duplicates based on 'job_id'
        # This is a good safeguard, though ideally not needed if splitting was perfect.
        if "job_id" in combined_df.columns:
            initial_rows = len(combined_df)
            combined_df.drop_duplicates(subset=["job_id"], inplace=True)
            if len(combined_df) < initial_rows:
                print(
                    f"  Removed {initial_rows - len(combined_df)} duplicate job entries."
                )
        else:
            print("  'job_id' column not found for checking duplicates.")

        # Save the final combined DataFrame
        combined_df.to_csv(output_path, index=False)
        print(
            f"\nSuccessfully combined {len(combined_df)} refined jobs into: {output_path}"
        )  # noqa: E501
        print("You can now proceed with your NLP analysis on this file.")

    except Exception as e:
        print(f"An error occurred during concatenation or saving: {e}")


# --- Run the combination process ---
if __name__ == "__main__":
    combine_refined_datasets(
        REFINED_FILES_DIR, EXPECTED_BATCH_SUFFIXES, PREFIX, OUTPUT_COMBINED_CSV
    )  # noqa: E501
