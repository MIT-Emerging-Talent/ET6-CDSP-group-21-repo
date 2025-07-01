# Detecting AI-Generated Job Scams: A Human and Machine Perspective

## **Project Overview**

The digital job market faces a growing and complex challenge: **sophisticated
fraudulent job postings crafted by advanced generative AI.** As scammers
leverage powerful AI, traditional detection methods, based on linguistic
cues and behavioral red flags, are increasingly failing.

Our study delves into the critical intersection of **cybersecurity**,
**human behavior**, and **Natural Language Processing (NLP)**. We ask:
*What happens when scammers have access to the same AI tools used to detect
them?*

This research is vital. According to the Federal Trade Commission, reported
losses from job opportunity scams totaled **$750.6 million in 2024**, a
nearly **$250 million increase from 2023**. These escalating figures
highlight the urgent need for new defenses.

---

## Investigating the Problem

We’re dissecting the scam job crisis through real-world examples and emerging
trends. For a detailed overview of scam patterns, case studies, and how they
relate to human behavior and AI:

[Read our Domain Study](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)

---

## **Our Research Question**

**Can humans still distinguish between legitimate and fraudulent job postings
when the scam text is written by advanced AI models?**

To address this, we will also explore:

* How do real and AI-generated scams compare linguistically?
* How do job seekers react to the presence and prominence of an automated
    scam score or warning?

---

## **Methodology: A Simulated Job Board Experiment**

Our approach involves a **simulated job board platform** designed to
evaluate participants’ ability to distinguish between legitimate and
fraudulent job postings. The primary focus is to assess whether AI-generated
fraudulent posts are more or less detectable compared to those written by
humans.

### **Data Collection**

* **Real Job Postings:** Sourced from LinkedIn, Indeed, and an existing
    dataset containing both human- and AI-written job ads. These posts
    will form our pool of legitimate examples.
* **Fake Job Postings:** Obtained from a 2014 dataset containing 18,000
    posts, 800 of which are labeled as fake. **Thirty** fake job posts were
    randomly selected and automatically refined using the Gemini API to
    generate AI-enhanced fraudulent postings, creating highly realistic scam
    variants.

### **Experimental Groups**

Participants will be randomly assigned to one of four groups, each exposed
to different risk indicators on the simulated job board:

* **Group A:** No risk indicators displayed.
* **Group B:** A **‘scam score’** (e.g., a numerical rating) displayed.
* **Group C:** A **‘warning sign’ icon** displayed.
* **Group D:** A **‘warning text’** (e.g., "Potential Scam") displayed.

### **Procedure**

Participants will interact with the simulated job board, reviewing a
randomized selection of job postings from each category (real/fake, human/AI-
written). For each post, they will indicate whether they believe the job is
legitimate or fraudulent. Their responses, along with response time,
confidence level, and what affected their decision, will be recorded.

### **Participants**

Participants will be recruited via a Google Form distributed across various
professional and social networks. The form will collect consent to
participate and email addresses. Inclusion criteria include being over 18
years old and having some experience with online job searching.

### **Ethical Considerations**

All participants will provide informed consent before participating. They
will also have the **option to withdraw at any time** without penalty. Data
will be anonymized and stored securely. No personally identifiable
information will be shared or published.

### **Data Analysis**

Detection accuracy, confidence levels, and response times will be compared
across the four groups and between human- and AI-generated posts. This
analysis will determine if AI-written scams are easier or harder to detect
and whether risk indicators effectively improve human detection.

---

## **Data Collection & Preparation Pipeline** ⚙️

Our robust pipeline involves three key script-driven steps, designed for
transparency and reproducibility. These scripts process raw data into the
refined datasets used in our experiment.

1. **Fake Jobs Extraction:** Extracts a diverse sample of fake job listings
    from raw datasets.
    * **Script**:
        [`2_data_preparation/fake_jobs_extraction_script.ipynb`](./2_data_preparation/fake_jobs_extraction_script.ipynb)

2. **Fake Jobs AI Refinement:** Uses LLMs (like Gemini, GPT, or Claude) to
    rewrite selected fake jobs to sound more realistic and professional,
    while maintaining their scam-like structure.
    * **Script**:
        [`2_data_preparation/fake_jobs_AIrefinement_script.ipynb`](./2_data_preparation/fake_jobs_AIrefinement_script.ipynb)

3. **Real Jobs Cleaning:** Cleans and standardizes the real job postings
    dataset.
    * **Script**:
        [`2_data_preparation/cleaned_real_jobs_script.ipynb`](./2_data_preparation/cleaned_real_jobs_script.ipynb)

 All raw and processed data are stored in the
[`1_datasets`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/1_datasets)
folder. For a **detailed breakdown** of the data flow, including input/output
paths and dataset structure, please refer to the documentation within the
[`2_data_preparation`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/2_data_preparation)
directory.

---

## **Conclusion: Beyond Filters, a Battle of AIs**

Scam detection is no longer just about spam filters or "watching for typos."
It’s now fundamentally a battle of **AI versus AI**, with human job seekers
caught in the middle. Our goal isn't just to build a better model, but to
critically stress-test and rethink the foundational assumptions of how we
classify and catch job deceptions in the age of generative AI. By pushing
the boundaries of detection, we aim to contribute to a safer, more
transparent digital job market.

---

## **Further Clarity & Our Team**

* **Detailed Domain Study & Problem Analysis:**
    [Link to our Domain Study](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)

* **Project Planning & Deliverables:**
    [Link to our comprehensive Project Plan](https://docs.google.com/document/d/1i1eVjbVNQgU_a4QyH9LMGibSnDSmWRm3lal7s9J1-GM/edit?tab=t.0)

---

## About Us: The Hypatia Circle

We are The Hypatia Circle—a dedicated team of six women from across Africa
and the Middle East. United by a profound passion for data science and an
unwavering belief in the transformative power of diverse collaboration, we
strive to spark meaningful change and innovation.
