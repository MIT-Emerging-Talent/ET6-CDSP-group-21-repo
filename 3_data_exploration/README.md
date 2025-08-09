# Job Posting Fraud Detection: Data Exploration & Analysis

## Brief Description of the Project

This study examines job seekers' ability to detect AI-generated fraudulent job
postings in an era where advanced language models can create highly convincing
scams. By comparing participants' detection rates of AI-crafted versus
traditional fraudulent postings, analyzing which red flags are most noticeable,
 and observing behavioral responses, the research aims to improve scam prevention
 strategies for job platforms, policymakers, and cybersecurity efforts.

## Goal of EDA

To understand the dataset's characteristics, identify patterns, spot anomalies
(outliers), test hypotheses, and prepare the data for modeling.

## Data Sources

This project uses a combination of public datasets and simulated AI-generated
 job postings:

1. **Primary Dataset (Fake Job Postings)**
   - Source: Kaggle - Fake Job Posting Prediction
   - Contains 17,880 job postings labeled as real (0) or fake (1)
   - Features include: job_id, title, location, department, salary_range,
   company_profile, description, requirements, benefits, telecommuting,
   has_company_logo, has_questions, employment_type, required_experience,
    required_education, industry, function, fraudulent

### Preprocessing

- Removed duplicate entries
- Standardized text (lowercase, removed special characters)
- Handled missing values (company_profile, salary_range)

## Initial Data Assessment

- **Columns**: 18 features
- **Sample Size**: 17,880 records
- **Target Variable**: fraudulent (binary)
  - `0` = legitimate
  - `1` = fraudulent

## Dataset Overview

### Basic Information

- **Dimensions**:
  - Rows: 17,881
  - Columns: 18

### Column Data Types

| Column Name            | Data Type                          |
|------------------------|------------------------------------|
| job_id                 | Integer (int)                      |
| salary_range           | Continuous numerical range (strings)|
| company_profile        | String (str)                       |
| employment_type        | String (str)                       |
| required_experience    | String (str)                       |
| required_education     | String (str)                       |
| industry               | String (str)                       |
| description            | String (str)                       |
| Department             | String (str)                       |
| Location               | String (str)                       |
| title                  | String (str)                       |
| benefits               | String (str)                       |
| requirements           | String (str)                       |
| telecommuting          | Binary (0, 1)                      |
| has_company_logo       | Binary (0, 1)                      |
| has_questions          | Binary (0, 1)                      |
| fraudulent             | Binary (0, 1)                      |

## Descriptive Statistics

### Numerical Columns

- Calculate: count, mean, standard deviation, min, max, quartiles
- Example: Examine salary_range for reasonable means and range

### Categorical Columns

- Use value_counts() for frequency analysis
- Key columns: telecommuting, has_company_logo, has_questions, fraudulent

## Key Exploration Areas

### Missing Values Analysis

1. Identify missing values using .isnull().sum()
2. Calculate percentage missing
3. Strategy:
   - Drop if >50-70% missing
   - Impute numerical with mean/median
   - Impute categorical with mode or "Unknown"

### Categorical Features

#### Employment Type Distribution

| Category     | Records | Percentage |
|--------------|---------|------------|
| Full-time    | 11,620  | 65%        |
| Part-time    | 797     | 4.5%       |
| Contract     | 1,524   | 8.5%       |
| Temporary    | 241     | 1.3%       |
| Other        | 227     | 1.3%       |

#### Required Experience Levels

| Level              | Records | Percentage |
|--------------------|---------|------------|
| Mid-Senior         | 3,809   | 21.3%      |
| Entry Level        | 2,697   | 15.1%      |
| Associate          | 2,297   | 12.8%      |
| Not Applicable     | 1,116   | 6.2%       |
| Internship         | 381     | 2.1%       |
| Director           | 389     | 2.2%       |
| Executive          | 141     | 0.8%       |

## Numerical Features Analysis

### Telecommuting

| Category   | Records | Percentage |
|------------|---------|------------|
| Remote     | 767     | 4.3%       |
| On-Site    | 17,113  | 95.7%      |

### Company Attributes

| Attribute          | Present | Percentage |
|--------------------|---------|------------|
| Company Logo       | 14,220  | 74.2%      |
| Application Questions | 8,792 | 3%        |

## Key Findings

1. **Red Flags**:
   - Missing company logos (25.8%)
   - Lack of application questions (97%)
   - Absence of salary data (99.98%)

2. **Analysis Directions**:
   - Cross-reference missing attributes with fraud labels
   - Investigate logo absence correlation with fraud
   - Examine salary data patterns

## Tools Used

- Python: pandas, seaborn, matplotlib
- Libraries: nltk, missingno
- Excel for manual review

### 📊 To view the file, please download it from the link below

[Click here to download the Excel file](https://1drv.ms/x/c/5a56bc1cb2acee7d/EVkz8qCOOgdKnVO8lc5sKqQB1K9gCsmRkoTB4fddA0np2g?e=knGBAZ)
