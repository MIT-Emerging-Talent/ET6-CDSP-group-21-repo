# Problem Statement

On 6/12/2025, a group of about 100 students from the MIT Emerging Talent Program
attended a job readiness workshop with program staff, Carlos. One problem quickly
stood out: almost every student present had encountered a fake job posting.

[The Hypatia Circle](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/collaboration/README.md)
converged after the meeting to discuss and scope a project based on this.

**Problem Statement: Detecting Fraudulent Remote Job Postings In the AI Era:
A Machine Learning Approach**

As AI-generated text becomes more sophisticated, scammers can craft **convincing
fake job postings**, making traditional fraud detection methods, largely reliant
on linguistic analysis, less effective. Remote job scams are particularly
concerning, as they **lack physical verification mechanisms**, making deception
easier to execute.  

This project explores a **groundbreaking hybrid approach**; integrating
**text-based analysis with technical fraud markers**, such as **website
behavior, tracking elements, and form submission patterns**, to develop a more
holistic scam detection framework. By analyzing **job postings from 2015-2025**,
we aim to assess **how fraud tactics have evolved pre- and post-AI advancements**
and whether purely text-based classifiers remain sufficient.  

While the **primary focus is text-based classification**, this study will
**consult experts** on the feasibility of incorporating **non-text indicators**
into scam detection. Should technical fraud markers prove difficult to track due
to data constraints, the project will **refine its scope to focus solely on
linguistic fraud detection** while keeping non-text analysis open for future research.

**Scope:**

- **Core Focus:** Text-based scam detection using machine learning models.
- **Exploratory Area:** Investigating non-text indicators (website behavior,
tracking patterns, form submissions) with expert consultation.  
- **Dataset Strategy:** Since no structured dataset exists for 2015-2025, we
will **scrape and curate our own dataset** from verified job postings.  
- **Comparative Analysis:** Fraud evolution pre- vs. post-AI advancements.  

**Objectives:**

- **Develop a machine learning model** to classify scam vs. legitimate remote
job listings.  
- **Analyze linguistic fraud patterns**, focusing on deceptive phrasing and
urgency indicators.  
- **Assess feasibility** of non-text-based fraud markers and their integration
into detection models.  
- **Evaluate the impact** of AI-generated text on scam effectiveness.  

**Expected Outcomes:**

- A fraud detection model that **prioritizes text analysis**, with potential
expansion into technical fraud markers.  
- A **structured dataset** capturing 2015-2025 scam trends in remote job
postings.  
- Insights into **how scammers have adapted** as AI tools improve text
generation.  
- Expert consultation to determine whether non-text indicators can enhance scam detection.

[Link to the Background Review of our Research Domain](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/0_domain_study/README.md)

## Understanding the Problem Domain

### 🧩 The Problem at a Glance

In recent years, remote work has become a major part of the job market—but
alongside it, job scams have surged. With the rise of **AI-generated text**,
scammers now craft **convincing fraudulent job postings** that easily bypass
traditional red flags like grammar errors or formatting issues.

This has created a **trust crisis**, particularly for students and early-career
professionals navigating digital job platforms. Existing fraud detection
methods—many of which rely solely on **linguistic analysis**—are no longer
enough. Our group sees this not just as a technical issue, but as a
**systemic problem** that spans platforms, tools, and user vulnerability.

---

### Applying Systems Thinking

We looked at the different parts of this system and how they interact.

|   **Actors**         |   **Evolving Dynamics**                             |
|-----------------------|-------------------------------------------------------|
| Job Seekers           | Increased exposure to remote listings and online fraud|
| Scammers              | Using AI tools to produce highly realistic fake jobs  |
| Job Platforms         | Struggling to verify postings at scale                |
| Security Experts      | Exploring smarter fraud detection techniques          |
| Machine Learning Tools| Used for both scam creation and detection             |

---

### Why It Matters

If these scams continue to grow unchecked:

- Platforms may **lose user trust**
- Vulnerable populations may **face emotional and financial harm**
- **AI advancements** may be weaponized by bad actors faster than they are
  countered

---

### Our Approach

This project aims to address these challenges through a
**machine learning–driven fraud detection model** focused on **text-based
indicators**. Additionally, we explore the potential for incorporating
**technical fraud markers** (like suspicious form behaviors and tracking
patterns) to build a **hybrid detection system**.

By analyzing job scams between **2015–2025**, our group seeks to:

- Understand how fraud tactics evolved in the **AI era**
- Evaluate whether current detection strategies are sufficient
- Offer a framework that combines **linguistic features** and **platform
  behaviors**
