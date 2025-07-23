# Detecting AI-Generated Job Scams: A human and Machine Perspective

## Project Overview

The digital job market is facing an alarming rise in **sophisticated
fraudulent job postings crafted by advanced generative AI.** As scammers
increasingly leverage powerful AI, traditional detection methods—reliant
on linguistic cues and behavioral red flags—are proving insufficient.

Our study dives deep into the critical intersection of **cybersecurity**,
**human behavior**, and **Natural Language Processing (NLP)**. We pose a
fundamental question: *What happens when scammers have access to the same
AI tools used to detect them?*

This research is profoundly vital. According to the Federal Trade
Commission, reported losses from job opportunity scams soared to
**$750.6 million in 2024**, marking a nearly **$250 million increase from
2023**. These escalating figures underscore the urgent need for new,
effective defensive strategies.

---
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&pause=1000&color=CF1F4E&width=435&lines=Research+Question)](https://git.io/typing-svg)

**Can humans still distinguish between legitimate and fraudulent job
postings when the scam text is written by advanced AI models?**

To address this crucial inquiry, we investigated:

* How do genuine and AI-generated scam job postings compare linguistically?
* What markers distinguish AI-written scams from human-written scams?

**Comprehensive Domain Study & Problem Analysis:**
[Dive Deeper Here](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)

---

## Our Approach

We analyzed a curated set of real and fake job postings to study how
AI-generated scams differ linguistically from human-written real jobs.
We also refined each fake post using LLMs to create realistic yet
deceptive examples.

## Methodology

We used a single dataset sourced from the "Fake JobPostings" dataset
available on Kaggle. This dataset contains 17,880 job postings,
 of which only 866 are labeled as fake.
To enhance the realism of these fraudulent listings, we refined each one
using a large language model (LLM) to mimic legitimate language patterns
while preserving deceptive cues.

We acknowledge that this dataset is highly imbalanced, with 95.14% of
entries labeled as real. While this did not affect our exploratory
analysis, it posed challenges for clustering tasks. To mitigate this,
we created a balanced sample consisting of 866 real and 866 fake job
listings.

All data analysis and exploration were performed on this enriched dataset.

---

## Data Processing Pipeline

Our robust pipeline prepares all the data needed for the experiment. It
involves:

* **Extracting Fake Jobs:** Selecting initial fake job listings.
* **AI Refining Fake Jobs:** Using LLMs (like Gemini) to make fake jobs
  super realistic.
* **Cleaning Real Jobs:** Standardizing authentic job postings.

All data is in the
[`1_datasets`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/1_datasets)
folder. Scripts are in
[`2_data_preparation`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/2_data_preparation)
for full transparency.
Explore our data exploration notebooks:
[`3_data_exploration`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/3_data_exploration)
Explore our analyses and outputs in:
[`4_data_analysis`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/4_data_analysis)

---
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&pause=1000&color=CF1F4E&width=435&lines=Data+Analysis)](https://git.io/typing-svg)

## Hypotheses

We explored two main hypotheses throughout our project:

1. **Main Hypothesis:**  
   Human-written and AI-generated fake job listings differ
   significantly in their linguistic patterns from real job listings.

2. **Sub-Hypothesis:**  
   AI-generated scams are more polished and persuasive, making them
   potentially harder to detect than human-written scams.

Our visual analyses support both hypotheses by revealing distinct
word usage patterns, repetition in structure, and thematic exaggeration
in fake listings.

## Non-Technical Explanation of Findings

Our project investigates the linguistic patterns found in fake or
AI-generated job postings by comparing them to authentic human-written
listings. Using natural language processing (NLP) techniques, we explored
how language can be a signal of authenticity or deception.

Fake job descriptions often rely on vague or overly persuasive language to
attract attention. Phrases like "quick hire", "no experience", or "urgent
need" appeared frequently in fraudulent listings. These kinds of phrases
are designed to create urgency or appeal to job seekers without offering
much substance.

We also observed that some AI-generated postings are overly polished or
mechanically structured. Readability tests showed unusual sentence
complexity or artificial smoothness, contrasting with the more varied and
natural tone found in human-written descriptions.

Grammar analysis, through Part-of-Speech tagging, revealed overuse of
adjectives and repetitive sentence patterns in fake posts. Meanwhile,
named entity recognition sometimes flagged company or location names that
appeared fabricated or oddly placed.

Topic modeling and sentiment analysis (which have been completed) helped
identify recurring themes such as exaggerated job benefits, promises of
remote work, and overly positive tones. These emotional or thematic
markers differ from more neutral or balanced wording found in legitimate
listings.

### Visual Evidence

#### Word Frequency Distribution

This chart shows the most common words used across different types of job
descriptions. It highlights how certain terms are more frequent in fake or
AI-generated listings, providing a visual cue to potential fraud.

![Word Frequency Graph](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/cleaned_most_frequent_words/all_sections_words_count.png)

---

### Certainty and Confidence in Results

The analysis indicates clear patterns that distinguish fake or
AI-generated postings from real ones. While the results do not offer
absolute proof, there is a strong level of confidence in the trends we
uncovered. Multiple methods (frequency analysis, POS tagging, readability
scoring, topic modeling) aligned to suggest that language use differs in
meaningful and detectable ways.

---

### Sources of Error and Limitations

* The dataset is highly imbalanced, with only 4.86% of listings labeled
  as fake. While this had no major impact during exploratory analysis,
  it limited the effectiveness of some downstream tasks such as clustering.
  To address this, a balanced random sample of 866 real and 866 fake
  jobs was used in those specific steps.

* While there was an initial concern that fake jobs might cluster into
  different job types than real jobs, clustering analysis showed a high
  degree of overlap in job categories across both classes, suggesting
  no major bias in job type distribution.

* A few AI-generated samples lacked clear labeling, requiring some
  manual assumption-based classification.

* NLP methods focus on structure and word use, so they may overlook
  deeper context, sarcasm, or cultural nuance.

* Topic modeling was applied to a relatively small dataset, which can
  affect the stability and generalizability of themes.

Despite these limitations, the overall patterns are consistent and align
with previous research on text deception and AI language generation.

---

## Conclusion: Beyond Filters, a Battle of AIs

Scam detection is no longer just about spotting typos. It’s a fundamental
battle of **AI versus AI**, with human job seekers in the middle. Our goal
is to stress-test how we classify deceptions in the age of generative AI,
contributing to a safer digital job market.

* **Detailed Project Planning & Deliverables:**  
  [Access Our Project Plan](https://docs.google.com/document/d/1i1eVjbVNQgU_a4QyH9LMGibSnDSmWRm3lal7s9J1-GM/edit?tab=t.0)

---

## The Hypatia Circle

**The Hypatia Circle** — *"Reserve your right to think, for even to think
wrongly is better than not to think at all."* — Hypatia of Alexandria

We are The Hypatia Circle—a dedicated team of six women hailing from
diverse backgrounds across Africa and the Middle East. United by a
profound passion for data science and an unwavering belief in the
transformative power of diverse collaboration, we strive to spark
meaningful change and innovation in the world of data.

[Learn more about the team!](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/993536d48ceb618e12b753593098cbdb1f7b4df1/collaboration)
