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

## Aegean and Hypatia Datasets

There are three files in the [`../1_datasets/aegean500_vs_hypatia500_datasets`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets)
folder:

### [**Fake Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/aegean500_fakejobs.csv)

- Includes 500 fake job posts which were extracted from the Aegean raw dataset. The
difference between this file and the one in [`../1_datasets/cleaned_data/fake_jobs.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/fake_jobs.csv)
is that they both followed different data cleaning process.

### [**Real Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/hypatia500_realjobs.csv)

- Includes 500 real job posts which were extracted from Indeed. The difference
between this file and the one in [`../1_datasets/cleaned_data/real_jobs.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/14894562ec2b519501aaed5b0525f54313fdfb0f/1_datasets/cleaned_data/real_jobs.csv)
is the fact that they were extracted from different sources.

### [**LLM-Refined Fake Job Posts**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/e46c53bf17c3d608c8e67b607300d9faf4b6043e/1_datasets/aegean500_vs_hypatia500_datasets/aegean500_fakejobs_llmrefined.csv)

- Includes 500 fake jobs which were all LLM-refined. The difference between
this file and [`../1_datasets/cleaned_data/llm_refined_fake_posts2.csv`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/1559fd4f70f49837b9626a46db57799e8c5a39da/1_datasets/cleaned_data/llm_refined_fake_posts2.csv)
is the fact that they both read files that followed different cleaning process.

- This file was a merge output between:
  - [`/1_datasets/fakejobs_to_refine`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/08990371387dcddd06fb6f3361478bf4c33d45fb/1_datasets/fakejobs_to_refine).
  - [`../1_datasets/fakejobs_refined`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/8251dfa7db2ae2e0b35c3e619dd3c7f6e52af037/1_datasets/fakejobs_refined).

---

## Past Relevant Studies

The research, **_Assessing AI vs Human-Authored Spear Phishing SMS Attacks: An
Empirical Study_**, a **2025** study, was conducted by researchers at **_Brigham
Young University._**

To collect data, participants were recruited and asked to provide personal
information that could be used to personalize phishing messages.

Meanwhile, on the other hand, both human and AI authors used this personal information
to craft spear phishing SMS messages tailored to each participant.

There were mainly **_four_** steps for the data collection procedure. **_Firstly_**
participants were shown a set of personalized SMS messages (some human-authored,
some AI-generated).
**_Secondly_**, they were asked to rank the messages by how convincing they found
them. **_Thirdly_**, participants also provided qualitative feedback on each message.
**_Lastly_**, they were then asked to guess whether each message was written by a
human or by AI.

This experiment measured how convincing the messages were (both written by humans
and AI) and whether participants could distinguish between human and AI authorship.

There was **_no study_** that specifically tested humans' ability to differentiate
if a job post is legitimate or fraudulent when the post is AI-generated that we
know of, hence we're planning to use this study as a foundation for the process
of building and analyzing the job board.

[**Past Relevant Studies File Path.**](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/549942e9039edafdae73dff7d904ec97fa432148/1_datasets/past_relevant_studies.md)
