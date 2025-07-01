# [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&pause=1000&color=CF1F4EFF&width=490&lines=DETECTING+AI-GENERATED+JOB+SCAMS;A+HUMAN+AND+MACHINE+PERSPECTIVE)](https://git.io/typing-svg)

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
CAN HUMANS STILL DISTINGUISH BETWEEN LEGITIMATE AND FRAUDULENT JOB
**POSTINGS WHEN THE SCAM TEXT IS WRITTEN BY ADVANCED AI MODELS?**
To address this crucial inquiry, we will also investigate:

* How do genuine and AI-generated scam job postings compare linguistically?
* How do job seekers react to the presence and prominence of an automated
    "scam score" or warning signal on job platforms?

---

## Our Approach: A Simulated Job Board Experiment

We are building a **simulated job board** to test how well people can spot
fake job ads, especially when those ads are created by advanced AI. We also
want to see if a simple "scam warning" helps them.

Here's our plan:

### **1. Crafting Job Postings**

* **Real Jobs:** We gather authentic job ads from top platforms like
    LinkedIn and Indeed. These are our legitimate examples.
* **AI-Enhanced Fake Jobs:** We take existing fake job ads and give them
    to powerful AIs (like Gemini or GPT). These AIs rewrite them to sound
    *highly realistic and professional*, but still contain subtle scam
    elements.

### **2. Testing with Participants**

* We'll recruit participants who are job seekers. They'll browse our
    simulated job board.
* Participants will be divided into **four groups**, each seeing a
    different type of "scam warning" next to the job posts:
  * **Group A:** No warnings.
  * **Group B:** A "scam score" (e.g., 7/10 Scam Risk).
  * **Group C:** A "warning sign" icon (e.g., ⚠️).
  * **Group D:** A "warning text" (e.g., "Potential Scam").
* For each job, they'll decide if it's "Legitimate" or "Scam," and tell
    us how confident they are.

### **3. Analyzing Results**

* We'll compare how accurately each group spotted scams.
* Crucially, we'll see if AI-written scams are harder to detect than
    human-written ones.
* We'll also learn if those "scam warnings" actually help job seekers avoid
    fraud.

### **Ethical Considerations**

All participants will provide informed consent, can withdraw anytime, and
their data will be anonymized and kept secure.

### **Possible Limitations**

Our study might face limitations like some "real" jobs being undetected
scams, AI-crafted scams not being perfectly human-like, or participant bias
if they are already very scam-aware.

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

---

## Conclusion: Beyond Filters, a Battle of AIs

Scam detection is no longer just about spotting typos. It’s a fundamental
battle of **AI versus AI**, with human job seekers in the middle. Our goal
is to stress-test how we classify deceptions in the age of generative AI,
contributing to a safer digital job market.

---

## Further Project Insights & Our Team

* **Comprehensive Domain Study & Problem Analysis:**
    [Dive Deeper Here](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/0_domain_study)

* **Detailed Project Planning & Deliverables:**
    [Access Our Project Plan](https://docs.google.com/document/d/1i1eVjbVNQgU_a4QyH9LMGibSnDSmWRm3lal7s9J1-GM/edit?tab=t.0)

---

## The Hypatia Circle

**The Hypatia Circle** — *"Reserve your right to think, for even to think
wrongly is better than not to think at all."* — Hypatia of Alexandria

We are The Hypatia Circle—a dedicated team of six women hailing from diverse
backgrounds across Africa and the Middle East. United by a profound passion
for data science and an unwavering belief in the transformative power of
diverse collaboration, we strive to spark meaningful change and innovation
in the world of data.
