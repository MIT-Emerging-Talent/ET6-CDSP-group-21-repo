# Datasets

Only one dataset was used for the analysis process of this project, that is the
**Employment Scam Aegean Dataset**. All data processing, analysis, and
observations are mainly based on this dataset, along with 500 real job posts
which were extracted from **Indeed.**

## Aegean Raw Data

This dataset can be found in **Kaggle**, referred to as **_'Recruitment Scam
Dataset'_**, or in
**EMSCAD** project **website**, referred to as **_'Employment Scam Aegean Dataset'_**.

This dataset was collected and curated by the **_Laboratory of Information and Communication
Systems Security_** at the **_University of the Aegean_** in **_Greece_**.
It contains **18,000** job postings, with around **800** labeled as fraudulent.

This dataset
was mainly designed to  provide a realistic and comprehensive resource for research
on employment scams. It was collected from real online job ads between **2012**
and **2014**.
The job postings were gathered from multiple **_online_** sources, including **_job
portals_** and **_corporate websites_**.

Each entry in the dataset includes a
variety of features such as **_job title, location, department, salary range, company_**
**_profile, job description, requirements, benefits, telecommuting status, company
logo_**, **_presence, employment type, required experience, required education, industry,
function,_** and a **_class label_** indicating whether the posting is fraudulent
or not.

The dataset is publicly available and has been widely used in academic research
for developing and testing machine learning models to detect fraudulent job postings.

The main goal of this data is to clean it based on specific features that we aim
to use in the job board, organize it, refine it by Gemini, then use it to test
humans' and machines' ability to detect if the job provided is legitimate or
fraudulent when it's written by AI, since it mimics real job posts while
maintaining fraudulent posts main features.

[**File Path to Aegean Raw Data**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/28fb2c5be79be0883c8366fb2b4bacbbec9c6809/1_datasets/aegean_raw_data)

---

## Cleaned Data

There are three files in the [`../1_datasets/cleaned_data`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/1559fd4f70f49837b9626a46db57799e8c5a39da/1_datasets/cleaned_data)
folder:

### [Fake Job Posts](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/fake_jobs.csv)

- Includes 866 fake job posts which were extracted from the Aegean raw dataset. Shape
of the dataset is (866, 11) after cleaning.

### [Real Job Posts](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/real_jobs.csv)

- Includes 17014 real job posts which were extracted from the Aegean raw dataset.
Shape of the dataset is (17014, 11) after cleaning.
  
### [LLM-Refined Fake Job Posts](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/1559fd4f70f49837b9626a46db57799e8c5a39da/1_datasets/cleaned_data/llm_refined_fake_posts2.csv)

- Includes 866 fake job posts which were all LLM-refined. Shape of the dataset
is (866, 15) after cleaning.

---

## Aegean500_Hypatia500 Datasets Folder

In addition to the primary analysis focusing on the Aegean dataset, a
complementary analyses was done to explore the detection capabilities of four
traditional Machine Learning Models when given fake jobs refined by AI and real
jobs posted in the AI era.

### A note on the datasets that were used for the analyses

There are three files in the [`../1_datasets/aegean500_vs_hypatia500_datasets`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets)
folder:

### [**Fake Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/aegean500_fakejobs.csv)

- The (866, 17) fake jobs in the Aegean dataset contains lots of missing values
and needed to be cleaned for the analysis. A research of modern day job posts
structure revealed the following as core features - **job_id, job_title, location,
job_description, benefits** (with benefits often lumped into the job description).

- These features were retained and used to remove missing values from the dataset,
achieving a (500, 6) shape of fake jobs.

- Hence the difference between this file and the one in [`../1_datasets/cleaned_data/fake_jobs.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/fake_jobs.csv)
is that they both followed different data cleaning processes.

### [**Real Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/hypatia500_realjobs.csv)

- contains 500 real jobs scraped from the job board **Indeed** (_Jobs were
sorted by 'recently posted' on the board, and retrieved between 7/19/2025 - 7/20/2025_).
The chrome extention "webscraper.io" was utilized for the scrapping and these
key features - **Job_title, location, job description and job link** were
scrapped, with source-date retained as metadata.

- What informed the 'type' of real jobs to scrape?
  - The fake jobs word cloud showed that certain job titles - Data Entry,
  Engineer, Customer service, and Entry clerk, were dominant. These became the
  key jobs that were searched and scrapped from Indeed.

- Hence, the difference between this file and the one in [`../1_datasets/cleaned_data/real_jobs.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/real_jobs.csv)
is the fact that they are real jobs of different times,
(aegean (2012 - 2014), hypatia (2025))

### [**LLM-Refined Fake Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/aegean500_fakejobs_llmrefined.csv)

- The 500 job descriptions were fed to Gemini 2.5 flash with a robust prompt
aimed at modernizing the fake jobs. Specifically, this **"Add appealing but
potentially exaggerated benefits/responsibilities."** was part of the prompt to
bring the job descriptions up to modern standard.

- The refinement task was split between team members in this file:
  - [`/1_datasets/fakejobs_to_refine`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/08990371387dcddd06fb6f3361478bf4c33d45fb/1_datasets/fakejobs_to_refine).
- The refined version is seen here:
  - [`../1_datasets/fakejobs_refined`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/8251dfa7db2ae2e0b35c3e619dd3c7f6e52af037/1_datasets/fakejobs_refined).
- The 6 refined batches were recombined to get the aegean500_fakejobs_llmrefined.csv
- Hence, the difference between this file and [`../1_datasets/cleaned_data/llm_refined_fake_posts2.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/1559fd4f70f49837b9626a46db57799e8c5a39da/1_datasets/cleaned_data/llm_refined_fake_posts2.csv)
is that they both read and refined files that followed different cleaning processes.

### All scripts related to this complementary analyses

- [fake jobs extraction script](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/2_data_preparation/fake_jobs_extraction_script.ipynb).
- [fake jobs refinement script](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/2_data_preparation/fake_jobs_ai_refinement_script.ipynb).
- [batch recombination script](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/2_data_preparation/recombine_aegean500_batches.py).
- [data exploration script](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/3_data_exploration/aegean_hypatia_datasets_exploration.ipynb).
- [data analysis script](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/aegean_hypatia_datasets_analysis.ipynb).
