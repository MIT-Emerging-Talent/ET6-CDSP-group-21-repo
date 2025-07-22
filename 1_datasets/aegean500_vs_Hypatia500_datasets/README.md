# Description of Datasets

This folder contains;

***unrefined aegean500 dataset***: 500 rows of fake jobs were extracted and
cleaned from the 866 rows of fake jobs in the raw Aegean Dataset (a popular dataset
referenced in fake job studies (*read more about it in 1_datasets/Readme*)).

Find this unrefined aegean500 in *cleaned_aegean_fakejobs/aegean_500_fakejobs.csv*
Extraction script used - *2_data_preparation/fake_jobs_extraction_script.ipynb*

***refined aegean500 dataset***: The 500 job descriptions in the above dataset
is given to a Large Language Model (Gemini 2.5 Flash) to refine, to simulate
*fake job postings written by AI*. Why? Please read the "Why" below for a quick
understanding of the study.

Find this refined version in *cleaned_aegean_fakejobs/aegean_500_fakejobs_llmrefined.csv*
Refinement script used - *2_data_preparation/fake_jobs_AIrefinement_script.ipynb*

***Hypatia500 realjobs dataset***: 500 rows of real jobs scraped from the job
board **Indeed** (*Jobs were sorted by 'recently posted' on the board, and
retrieved between 7/19/2025 - 7/20/2025*)

What informed the 'type' of real jobs to scrape?

In exploring the aegean500 dataset (please find the data exploration details
in the notebook ***3_data_exploration/aegean_hypatia_datasets_exploration.ipynb***),
the word cloud showed that certain job types - Data Entry, Engineer, Customer
service, and Entry clerk, were dominant. These became the key jobs that were
searched and scrapped from Indeed. Please find the data exploration details of
the Hypatia500 in the Notebook ***3_data_exploration/aegean_hypatia_datasets_exploration.ipynb***

## Choice of Dataset

A brief recap of the study - Our research is focused on exploring fake job
dynamics in the era of AI. Specifically we are asking; To what extent can humans
and models detect fraudulent job posts when the scam text is written by AI.

To study this, we need a simulation of fake jobs written by AI (hence the
refined aegean500) and modern day real jobs (hence the hypatia500).
