# Detecting AI-Generated Job Scams: A Human and Machine Perspective

![AI Scam Detection GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExazMxc25uNmY3MmRkd3Z0cW11b2E4aXN2Zmxld2o5ZjI5Z2c3ZW5vYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3JlYXRlZF90aW1lPTE2NjA2MjMyNDAmY3BpZD1lZTM4ZDZmNGNmYThkYjdmN2Q0NjgzYjQ3MzBiODExMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MBeHh0U30k5w59v9kH/giphy.gif)

---

## **Project Overview**

The digital job market faces a growing and complex challenge:
**sophisticated fraudulent job postings crafted by advanced generative AI.**
As scammers leverage powerful AI, traditional detection methods, based on
linguistic cues and behavioral red flags, are increasingly failing.

Our study delves into the critical intersection of **cybersecurity**,
**human behavior**, and **Natural Language Processing (NLP)**. We ask:
*What happens when scammers have access to the same AI tools used to detect
them?*

This research is vital. According to the Federal Trade Commission, reported
losses from job opportunity scams totaled **$750.6 million in 2024**, a
nearly **$250 million increase from 2023**. These escalating figures
highlight the urgent need for new defenses.

---

## **Investigating the Problem: A Systems Perspective**

We're dissecting the job scam problem through a systems thinking lens,
examining it from observable events to underlying beliefs that perpetuate
the cycle.

### **Event: The Rise of Indistinguishable Scam Postings**

Scam job postings are surging, often *impossible to distinguish* from
legitimate ones. People apply, share personal data, and even send payments—
only to realize they've been tricked.

### **Patterns and Trends: The Scammers' Playbook**

* **Common Tactics:** Upfront payment requests (e.g., for background
    checks, training), psychological pressure (urgency, no interviews), and
    using real employee names from LinkedIn.
* **Most Impacted Groups:** Young professionals and job seekers under
    financial stress.
* **Growth Over Time:** Action Fraud UK received **4,876 scam job reports
    in 2024** versus 2,094 in 2022 ([BBC source](https://www.bbc.com/news/business-68646460)).

### **Structures Behind the Pattern: Exploiting Trust**

The job application process follows a predictable script. People expect to
provide personal info and generally don't question the steps. Scammers
exploit this trusted structure, meticulously mimicking real HR processes to
gain credibility.

### **Mental Models Keeping the System in Place: Why Scams Endure**

* **Desperation Mindset:** “I need a job, I’ll try anything.”
* **Shame Barrier:** Victims often stay silent or hesitate to warn others.
* **Individual Blame:** The system often treats this as a personal mistake,
    not a systemic vulnerability.
* **Normalization of Risk:** “Scams are common—it’s just how things are
    now.”

### **Gaps We Aim to Explore: Our Focus Areas**

Despite ongoing efforts by platforms like LinkedIn, critical gaps remain. We
aim to explore:

* Can **LLM-generated scams** be flagged through better linguistic cues?
* What happens when humans see a **scam score** before applying?
* Are **existing detection tools** still relevant against generative AI?

---

## **Our Research Question**

**Can humans still distinguish between legitimate and fraudulent job postings
when the scam text is written by advanced AI models?**

To address this, we will also explore:

* How do real and AI-generated scams compare linguistically?
* How do job seekers react to the presence and prominence of an automated
    scam score or warning?

---

## Our Approach

We are simulating the job application process through a survey to test job
seekers' detection abilities. Our primary goal is to assess whether humans can
reliably identify scams when presented with AI-generated job postings.

### **Methodology & Data Collection**

1. **Sample Selection:**
    * **Collect Real Job Postings:** We'll curate a balanced set of
        authentic postings from platforms like LinkedIn and Indeed. For each,
        we'll include the job title, company, full description, and posting
        link.
    * **Collect & Refine Fake Job Postings:** We'll source fake postings
        from public scam datasets. These will then be refined and modernized
        using advanced AI models (e.g., GPT, Claude) to simulate realistic,
        AI-written scam jobs.

2. **Survey Interface:**
    * Participants will be presented with job postings one by one.
    * For each, they'll be asked to label it as **“Legitimate”** or
        **“Scam.”**

3. **Analysis Pipeline:**
    * We will measure accuracy, false positives/negatives, and confidence
        levels.
    * Performance will be segmented by posting type (real vs. AI-generated)
        and compared across various participant attributes.

### **Possible Limitations**

* Some "real" jobs might be undetected scams.
* AI-crafted scams might lack full human-level subtlety.
* Participant bias due to prior awareness of scams.

---

## **Data Collection & Preparation Pipeline**

Our robust pipeline involves three key script-driven steps, designed for
transparency and reproducibility:

1. **Fake Jobs Extraction:** Extracts a diverse sample of fake job listings
    from raw datasets.
    * **Script**:
        [`scripts/fake_jobs_extraction_script.ipynb`](./scripts/fake_jobs_extraction_script.ipynb)

2. **Fake Jobs AI Refinement:** Uses LLMs (like Gemini, GPT, or Claude) to
    rewrite selected fake jobs to sound more realistic and professional,
    while maintaining their scam-like structure.
    * **Script**:
        [`scripts/fake_jobs_AIrefinement_script.ipynb`](./scripts/fake_jobs_AIrefinement_script.ipynb)

3. **Real Jobs Cleaning:** Cleans and standardizes the real job postings
    dataset.
    * **Script**:
        [`scripts/cleaned_real_jobs_script.ipynb`](./scripts/cleaned_real_jobs_script.ipynb)

All our data preparation scripts and processed datasets are publicly
hosted in this repo. For a **detailed breakdown** of the data flow,
including input/output paths and dataset structure

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

* **🔍 Detailed Background Research & Domain Study:**
    [Link to our Background Research](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)
* **💡 Project Planning & Documentation:**
    [Clarity document](https://docs.google.com/document/d/1i1eVjbVNQgU_a4QyH9LMGibSnDSmWRm3lal7s9J1-GM/edit?tab=t.0)

---

### About Us: The Hypatia Circle

We are The Hypatia Circle—a dedicated team of six women.
 United by a profound passion for data science and an
unwavering belief in the transformative power of diverse collaboration, we
strive to spark meaningful change and innovation.
