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

## Goal of EDA

      To understand the dataset's characteristics, identify patterns, 
      spot anomalies (outliers), test hypotheses,and prepare the data for modeling.

## Data Sources

This project uses a combination of public datasets and simulated AI-generated
job postings to study fraud detection in job listings. Below are the key data
 sources and processing steps:

1. Primary Dataset (Fake Job Postings)

  📌 Source: Kaggle - Fake Job Posting Prediction
🔹**Description:**

 This dataset about **Fake Job Posting**, with columns like: job_id, title,
   location, department, salary_range,company_profile, description requirements,
   benefits, telecommuting,has_company_logo, has_questions,employment_type,
   required_experience, required_education, industry, function,fraudulent

 This dataset **Contains** 17,880 job postings labeled as real (0) or fake (1).

 The **Features** are title, location, company_profile, description, requirements,
 benefits,
  fraudulent (target).

🔹 **Preprocessing:**

- Removed duplicate entries.

- Standardized text (lowercase, removed special characters).

- Handled missing values (company_profile, salary_range).

## Initial Data Assessment

- **Columns**: 18 features including job metadata, descriptions, flags
 (telecommuting, logo), and target (fraudulent)
- **Sample Size**: 17,880 records
- **Target Variable**: fraudulent (binary):  
  - `0` = legitimate  
  - `1` = fraudulent

## Dataset Overview  

### Basic Information  

- **Dimensions:**  
  - Rows: 17,881  
  - Columns: 18  

### Column Data Types  

| Column Name            | Data Type                          |  
|------------------------|------------------------------------|  
| `job_id`               | Integer (`int`)                    |  
| `salary_range`         | Continuous numerical range (strings)|  
| `company_profile`      | String (`str`)                     |  
| `employment_type`      | String (`str`)                     |  
| `required_experience`  | String (`str`)                     |  
| `required_education`   | String (`str`)                     |  
| `industry`             | String (`str`)                     |  
| `description`          | String (`str`)                     |  
| `Department`           | String (`str`)                     |  
| `Location`             | String (`str`)                     |  
| `title`                | String (`str`)                     |  
| `benefits`             | String (`str`)                     |  
| `requirements`         | String (`str`)                     |  
| `telecommuting`        | Binary (`0`, `1`)                  |  
| `has_company_logo`     | Binary (`0`, `1`)                  |  
| `has_questions`        | Binary (`0`, `1`)                  |  
| `fraudulent`           | Binary (`0`, `1`)                  |  

### Key Observations  

- Most columns have a high number of non-null values, indicating minimal
  missing data.
- Categorical/text columns dominate the dataset, with a few binary and
  integer fields.  

**Why you do it(overall check)**: To get a high-level overview, identify
 initial data types, and spot potential issues like missing data or incorrect
  data types (e.g., numbers stored as strings).

## Descriptive Statistics

This step quantifies the basic properties of the **Fake Job Posting** dataset.  

## **Analysis Approach**  

### **For Numerical Columns**  

- Calculate:  
  - Count  
  - Mean  
  - Standard deviation  
  - Min/Max  
  - Quartiles (`25%`, `50%`/median, `75%`)  
- **Example:**  
  - Examine `salary_range`:  
    - Are the means reasonable?  
    - Is there a wide range (high standard deviation)?  

### **For Categorical Columns**  

- Use `value_counts()` to tally occurrences of each unique category.  
- **Key Columns to Analyze:**  
  - `telecommuting` (Does the job allow remote work?)  
  - `has_company_logo` (Is a company logo included?)  
  - `has_questions` (Are there screening questions?)  
  - `fraudulent` (Target variable: Is the job fake?)  
  - Other categorical fields (e.g., `employment_type`, `required_experience`).  

### **Check Unique Values (`nunique()`)**  

- Identify distinct values per column.  
  - High counts in text/object columns may indicate:  
    - Free-text fields (e.g., `description`).  
    - Unique identifiers (e.g., `job_id`).  

**Why you do it**: To understand the central tendency, spread, and distribution
 of numerical data, and the frequency of categories in categorical data.
 This helps you grasp the typical values and the variability.

## Key Exploration Areas  

## **A. Missing Values Analysis**  

Missing data can compromise analysis and models if unaddressed.  

### **Steps to Handle Missing Values**  

1. **Identify Missing Values**  
   - Use `.isnull().sum()` to count missing values per column.  
   - Calculate the **percentage missing**:  ```python  
     (missing_count / total_rows) * 100```
2. **Strategy Selection**  
   - **Drop Rows/Columns** if:  
     - A column has >50–70% missing values.  
     - Few rows are missing, and removal won’t shrink the dataset significantly.
   - **Impute (Fill) Values**:  
     - **Numerical**: Use **mean** (for normal distributions),
      **median** (robust to outliers), or **mode**.  
     - *Categorical*: Replace with the **mode** or a placeholder like `"Unknown"`.
     - *Advanced*: Predict missing values using ML models (e.g., KNN, regression).
   - **Leave as-is** if "missingness" carries meaning (e.g., optional fields).  

### **Why It Matters**  

- Ensures data **completeness** and **reliability**.  
- Prevents errors/biases in downstream tasks (e.g., modeling, visualizations).  

## **B. Categorical Features**  

*(Analysis continuation for categorical variables like `employment_type`.)*  

## **1. Employment Type Distribution**  

| Category      | Records  | Percentage | Insight                |  
|-------------- |----------|------------|------------------------|  
| **Full-time** | 11,620   | ~65%       | Dominates the dataset. |  
| **Part-time** | 797      | ~4.5%      | Rare compared to FT.   |  
| **Contract**  | 1,524    | ~8.5%      | Moderate presence.     |  
| **Temporary** | 241      | ~1.3%      | Very rare.             |  
| **Other**     | 227      | ~1.3%      | Negligible.            |  

**Key Insight:**  

- **Full-time roles** comprise **~65%** of postings, suggesting most fraudulent/

legitimate jobs target permanent positions.  

## **2. Required Experience Levels**  

| Level                | Records  | Percentage | Note                     |  
|----------------------|----------|------------|--------------------------|  
| **Mid-Senior**       | 3,809    | ~21.3%     | Most common requirement. |  
| **Entry Level**      | 2,697    | ~15.1%     | High demand for juniors. |  
| **Associate**        | 2,297    | ~12.8%     |                          |  
| **Not Applicable**   | 1,116    | ~6.2%      | May indicate generic ads.|  
| **Internship**       | 381      | ~2.1%      | Rare.                    |  
| **Director**         | 389      | ~2.2%      |                          |  
| **Executive**        | 141      | ~0.8%      | Very rare.               |  

**Key Insights:**  

- **Mid-Senior (21.3%)** and **Entry Level (15.1%)** dominate, aligning with
  typical job market trends.  
- **"Not Applicable"** postings (~6%) may lack specificity, potentially
 signaling lower-quality/fraudulent ads.  

### **Next Steps**  

- Cross-analyze with `fraudulent` flag to identify suspicious patterns
 (e.g., are "Other" employment types more likely to be fake?).  
- Visualize distributions (bar plots) for clearer comparisons.  

## Categorical & Numerical Features Analysis  

## **1. Education Level Distribution**  

| Education Level                     | Records | Percentage | Notes       |  
|-------------------------------------|---------|------------|-------------|  
| **Bachelor's Degree**              | 5,145   | ~28.8%      | Most common requirement|
| **High School or equivalent**      | 2,080   | ~11.6%     |                   |
| **Unspecified**                    | 1,397   | ~7.8%      |May indicate vague ads|
| **Master's Degree**                | 416     | ~2.3%      |                   |
| **Associate Degree**               | 274     | ~1.5%      |                   |
| **Certification**                  | 170     | ~0.9%      |                   |
| **Some College Coursework**        | 102     | ~0.6%      | Rare              |
| **Professional**                   | 74      | ~0.4%      |                   |
| **Vocational**                     | 49      | ~0.3%      |                   |
| **Doctorate**                      | 26      | ~0.1%      | Very rare         |

**Key Insights:**  

- **Bachelor's degrees** are the most demanded (~29%), followed by
 **High School diplomas** (~12%).  
- **Unspecified** entries (~8%) could signal incomplete or fraudulent postings.

## **2. Telecommuting (Remote Work)**  

| Category   | Records | Percentage |  
|------------|---------|------------|  
| **Remote** | 767     | ~4.3%      |  
| **On-Site**| 17,113  | ~95.7%     |  

**Insight:**  

- Over **95% of jobs require on-site work**,
 suggesting remote opportunities are rare in this dataset.  

## **3. Company Attributes**  

*(Upcoming analysis of features like `has_company_logo`, `has_questions`.)*  

**Next Steps**  

- Compare education levels against `fraudulent` flag to detect anomalies
 (e.g., fake jobs omitting education requirements).  
- Investigate if remote jobs have higher fraud rates.  

## Numerical & Binary Features Analysis

### 1. Telecommuting (Work Location)

| Category   | Records | Percentage | Insights                 |
|------------|---------|------------|--------------------------|
| **Remote** | 767     | 4.3%       | Rare in this dataset     |
| **On-Site**| 17,113  | 95.7%      | Overwhelming majority    |

**Note:** Potential fraud indicator - remote jobs may be more susceptible to scams.

### 2. Company Attributes

#### A. Company Logo Presence

| Presence       | Records | Percentage | Insights                 |
|----------------|---------|------------|--------------------------|
| **Has Logo**   | 14,220  | 74.2%      | Most postings include    |
| **No Logo**    | 3,660   | 25.8%      | Could signal less legitimacy |

#### B. Application Questions

| Presence       | Records | Percentage | Insights                 |
|----------------|---------|------------|--------------------------|
| **Has Questions** | 8,792  | 3%         | Very rare                |
| **No Questions** | 89.7%  | 97%        | Nearly universal         |

**Note:** Extremely low question rate may indicate less rigorous hiring processes.

### 3. Salary Information

- **Total Jobs with Salary Ranges:** 3 (0.02% of dataset)
- **Example Ranges:**
  - $120k-$150k
  - $70k-$90k
  - $100k-$600k (extremely wide range)

**Critical Insight:**

- Nearly all postings omit salary data
- The 3 listed salaries show suspicious patterns (especially $100k-$600k range)

## Key Takeaways

1. **Red Flags for Fraud Detection:**
   - Missing company logos (25.8%)
   - Lack of application questions (97%)
   - Absence of salary data (99.98%)
   - Extremely wide salary ranges when present

2. **Potential Analysis Directions:**
   - Cross-reference missing attributes with fraud labels
   - Investigate if logo absence correlates with fraud
   - Examine why so few postings include salary data

3. **Data Quality Notes:**
   - Salary data is nearly non-existent
   - Binary features show skewed distributions

## Univariate Analysis with Visualization

### 1. Numerical Features Visualization

#### **Recommended Plots:**

| Plot Type   | Purpose                          | Example Use Case             |
|-------------|----------------------------------|------------------------------|
| **Histogram** | Show distribution shape        | Salary range distribution    |
| **Box Plot** | Display quartiles & outliers    |Compare salary by fraud status|

**Key Questions:**

- Are numerical features normally distributed or skewed?
- Are there extreme outliers (e.g., unrealistic salary ranges)?

### 2. Categorical Features Visualization

**Recommended Plots:**

| Plot Type       | Purpose                          | Example Use Case  |
|-----------------|----------------------------------|-------------------|
| **Bar Plot**    | Show category frequencies        | Employment type distribution|
| **Pie Chart**   | Display proportions              | Fraud vs legitimate ratio|
| **Word Cloud**  | Visualize text patterns          |Fraudulent job description-keywords|

**Key Questions:**

- Which categories dominate (e.g., full-time jobs)?
- Are there unusual category distributions?

## 3. Target Variable Analysis (`fraudulent`)

### **Critical Checks:**

1. **Class Imbalance:**
   - Expected: ~5% fraudulent (common in fraud datasets)
   - Action: Consider techniques like SMOTE if severe imbalance

2. **Key Correlations:**

   | Feature            | Expected Fraud Correlation | Reason                   |
   |--------------------|----------------------------|--------------------------|
   | `telecommuting`    | Higher                     | Remote jobs easier to fake|
   | `has_company_logo` | Lower                      | Legitimate companies have-branding|
   | `salary_range`     | Missing = Higher risk      | Fraudsters often omit details|

### **Visualization Examples:**

Using **Python**

**Class Balance** : sns.countplot(data=df, x='fraudulent')
**Fraud by Employment Type** :
 pd.crosstab(df['employment_type'], df['fraudulent']).plot(kind='bar')

## Advanced Fraud Detection Analysis

### 1. Correlation Analysis

- **Heatmap** of:  
  - `telecommuting`  
  - `has_company_logo`  
  - `has_questions`  
  vs. `fraudulent` status  

### 2. Geospatial Check  

- Map locations to flag inconsistent entries  
- **Example**: "Auckland, NZ" for a "Washington DC" role  

### 3. Suspicious Indicators  

### High-Risk Job Examples  

- **Job 1**: Unpaid internship with high demands  
- **Job 8**: Vague benefits ("steak everyday", "karate lessons")  
- **Job 14**: Minimal requirements ($10/hr, heavy lifting)  

### 4. Tools to Use  

### Python Libraries  

- `pandas` for data profiling  
- `seaborn`/`matplotlib` for visualizations  
- `nltk` for text analysis  
- `missingno` for null value inspection  

### Additional Tools  

- Excel for manual review  

#### **Heatmap of Key Features vs. Fraud**

Using **Python**
import seaborn as sns
import matplotlib.pyplot as plt

**##Select features for correlation**
features = ['telecommuting', 'has_company_logo', 'has_questions', 'fraudulent']
corr_matrix = df[features].corr()

**##Generate heatmap**
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Fraud Correlation Heatmap")
plt.show()
