# Job Posting Fraud Detection: Data Exploration & Analysis

## Brief Description of the Project

This study examines job seekers' ability to detect AI-generated fraudulent job
 postings in an era where advanced language models can create highly convincing
 scams. By comparing participants' detection rates of AI-crafted versus traditional
  fraudulent postings, analyzing which red flags are most noticeable, and
  observing behavioral responses, the research aims to improve scam prevention
  strategies for job platforms, policymakers, and cybersecurity efforts. The
   experiment involves participants reviewing mixed real and fake job ads,
   rating their authenticity, and reporting their reactions, followed by
    demographic and awareness surveys. Insights from this study will help
     develop better fraud detection tools, educational resources for job seekers,
      and regulatory guidelines to combat AI-driven recruitment scams, ultimately
       creating a safer digital job market.

## Data Sources

This project uses a combination of public datasets and simulated AI-generated
job postings to study fraud detection in job listings. Below are the key data
 sources and processing steps:

1. Primary Dataset (Fake Job Postings)
📌 Source: Kaggle - Fake Job Posting Prediction
🔹 Description:

Contains 17,880 job postings labeled as real (0) or fake (1).

Features: title, location, company_profile, description, requirements, benefits,
 fraudulent (target).
🔹 Preprocessing:

Removed duplicate entries.

Standardized text (lowercase, removed special characters).

Handled missing values (company_profile, salary_range).

## Data Exploration File

You can view the full methodology in our [Project Documentation](https://drive.google.com/file/d/1D-5KzcFbE9AXQUdX6n8ERbE0XIaZJ7RZ/view?usp=sharing).
