# Data Analysis: Detecting Fake Job Posts

## NLP Analysis of Job Postings

## Introduction

Fraudulent job postings have become an increasing problem in online job markets,
making it crucial to identify scams before they harm job seekers. This project uses
Natural Language Processing (NLP) to detect deceptive job ads by analyzing linguistic
patterns that separate real postings from fake ones. By examining key textual
features, we can uncover whether a job posting was likely written by a human scammer
or generated by AI—helping job seekers avoid potential fraud.

## Research Connections

This analysis directly supports our core investigation of synthetic content detection
by:

1. **Quantifying Linguistic Divergence**  
   - Establishing measurable differences between human, AI-generated, and authentic
   posts  
   - Identifying 17 statistically significant scam markers (p<0.01)  

2. **Detection Strategy Validation**  
   - Confirming that hybrid NLP approaches outperform single-method analysis  
   - Demonstrating that textual features alone achieve 92%+ accuracy  

3. **Evolutionary Pattern Tracking**  
   - Revealing how LLM-refined scams adapt lexical patterns while preserving
   malicious intent

## Job Posting Authenticity Analysis

## Part 1: NLP Feature Analysis

### Text Readability Analysis

***Input***:

- Job description texts (17,014 real, 866 fake, 866 LLM-refined)

***Process***:

- Calculated Flesch-Kincaid and SMOG scores using TextStat
- Compared grade levels and sentence complexity

***Observation***:

- Real posts: Balanced readability (grade 10-12)
- Human scams: Simpler language (grade 7-8)
- AI scams: Paradoxically complex but harder to read

---

### Word Frequency Analysis

***Input***:

- Title, description, requirements, and benefits text

***Process***:

- NLTK tokenization with custom stopwords
- Cosine similarity between frequency vectors

***Observation***:

| Section        | Real-Fake Similarity | Fake-LLM Similarity |
|----------------|----------------------|---------------------|
| Requirements   | 0.95                 | 0.39                |
| Benefits       | 0.88                 | 0.99                |

---

### POS Tagging Analysis  

***Input***:

- Combined job title + description text

***Process***:

- spaCy's POS tagging
- Verb/noun ratio analysis

***Observation***:

- AI scams: 23% more adjectives
- Human scams: 3.2× more imperative verbs

---

## Part 2: Classifier Modeling

### Feature Engineering

***Input***:

- All extracted NLP features

***Process***:

- TF-IDF vectorization (Scikit-learn)
- Combined with NER counts

***Observation***:

- Top 3 important features:
  1. TF-IDF score for "salary"
  2. Proper noun count  
  3. Readability score

---

### Model Performance

***Input***:

- Balanced dataset (866 samples per class)

***Process***:

- Tested Logistic Regression, XGBoost, BERT
- 5-fold cross-validation

***Observation***:

| Model          | Precision | Recall |
|----------------|-----------|--------|
| Logistic Reg   | 0.98      | 0.97   |
| XGBoost        | 0.99      | 0.99   |
| BERT           | 1.00      | 1.00   |

---

## Summary & Limitations

**Key Findings**:

1. AI-generated scams have measurable linguistic fingerprints
2. Human scams rely on emotional urgency markers
3. Hybrid models (POS+TF-IDF+N-grams) perform best

**Limitations**:

- Dataset bias: 95% real jobs in raw data
- May not generalize to other LLM variants
- Salary data often missing in fake posts (74%)

**Recommendation**: Combine NLP analysis with metadata checks for robust detection.

## Analysis Notebooks

### [N-Gram Analysis](http://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/n-gram.ipynb)

**Methodology:**

- Examined frequency patterns of word sequences (1-3 grams)
- ***Key findings***:
  - Real posts showed consistent use of job-specific terminology
  - Human scams contained 42% more urgency-related bigrams
  - AI-generated posts exhibited unnatural n-gram distributions
- Processed text using NLTK for tokenization
- Compared n-gram profiles across post types using χ² tests

## 📊 Input Data

**Text Sources Analyzed**:

- Job descriptions  
- Requirements sections  
- Benefits sections  
**Dataset Composition**:
| Post Type          | Count  | Source           |
|--------------------|--------|------------------|
| Real job postings  | 17,014 | Aegean Dataset   |
| Human-written scams| 866    | Aegean Dataset   |
| LLM-refined scams  | 866    | GPT-3.5 generated|

## **Key Observations:**

- Real posts showed stable n-gram distributions (e.g., "project management skills"
appeared consistently)
- Human scams contained outlier bigrams ("quick hiring", "no experience")
- AI posts exhibited unusual trigram fluency ("demonstrate robust cross-functional")

### N-Gram Patterns by Post Type  

| Gram Type  | Real Job Example       | Human Scam Example      | AI Scam Example|
|------------|------------------------|-------------------------|----------------|
| **1-gram**| "management"| "urgent"| "optimize"|
| **2-gram** | "team collaboration"| "apply today"| "cross-functional synergy"|
| **3-gram** | "3 years experience"| "no experience needed"| "leveraging robust paradigms"|

### Alternative Methods Considered

**N-Grams outperformed alternatives because they:**

- ***Show exact phrases*** (unlike abstract embeddings)  
- ***Preserve word order*** (unlike TF-IDF)  
- ***Run efficiently*** (unlike BERT)  

***Key Tradeoffs Considered:***

| Method          | Best For          | Worst For          | Our Choice Reason|
|-----------------|-------------------|--------------------|------------------|
| Word Embeddings | Semantic meaning  | Specific patterns  | Needed clear scam flags|
| TF-IDF          | Keyword importance| Phrase detection   | Required word sequences|
| BERT            | Context           | Speed/cost         | Prioritized efficiency|

**Alternative Approach:**
Could have used word embeddings (GloVe) instead of pure frequency counts, but n-grams
provided better interpretability for our specific scam markers.

### [TF-IDF Analysis](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/4_data_analysis/tfidfinsights)

- Calculated term importance scores across post types
- Notable results:
  - Identified 17 statistically significant scam markers (p<0.01)
  - AI posts showed 28% higher average IDF scores for corporate jargon
  - Developed custom stopword list for job posting domain

### [Readability Assessment](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/readability.ipynb)

**Libraries Selected:**

- TextStat (Flesch, SMOG)
- SyntaxNet (sentence complexity)
- Chose these for:
  - Established academic validation
  - Multi-metric consensus
  - Sentence-level granularity

**Unexpected Result or Critical Insight:**
Interestingly, AI-written posts tend to use more complex vocabulary (scoring higher
in grade level) but are actually harder to understand (lower in readability).
This contradiction highlights their unnatural writing style.

### [Emotional Tone Detection](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/urgency_tone_analysis.ipynb)

**Analysis Flow:**

1. VADER for urgency detection
2. LIWC for psychological markers
3. Custom regex patterns for scam phrases

- Human scams showed:
  - 37% higher emotional intensity
  - 5x more urgency indicators
- AI posts maintained neutral but unnatural tone

**Why This Approach:**
Combined methods overcome individual limitations:

- VADER detects explicit urgency
- LIWC catches subtle emotional cues
- Regex finds known scam patterns

**Fallback Option:**
Had initial plans to use BERT sentiment but found traditional methods more
interpretable for our specific need.

### [POS Tagging Analysis](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/pos_tagging.ipynb)

**Objective:**  
Identify grammatical patterns distinguishing authentic posts from human-written and
AI-generated scams through part-of-speech distributions.

- Analyzed part-of-speech distributions:
  - AI posts contained excessive nominalizations
  - Real posts showed balanced syntactic patterns

**Key Observations:**

- Structural Differences:
  - AI posts showed rigid grammatical templates
  - Human scams had erratic punctuation patterns
  - Real posts exhibited natural variation

**Technical Stack:**

- Stanza for accurate tagging
- Custom noun/verb ratio metrics
- Dependency tree analysis

**Key Insight:**
Human scams used 22% more imperative verbs ("apply now") while AI overused
nominalizations ("the demonstration of skills").

### [Aegean-Hypatia Dataset Analysis](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/aegean_hypatia_datasets_analysis.ipynb)

- Conducted comparative analysis between original Aegean dataset and LLM-refined
versions
- Used cosine similarity to measure textual divergence
- Applied HDBSCAN clustering for department/salary patterns

**Methodology:**

- Comparative analysis of original vs LLM-refined posts
- Cosine similarity metrics for section-by-section comparison
- HDBSCAN clustering for salary/department patterns

**Key Findings:**

- LLM refinement increased corporate jargon by 28% while preserving scam intent
- Requirements sections showed strongest divergence (cosine similarity: 0.39)
- Benefits sections unexpectedly mimicked authentic posts (similarity: 0.90)

**Critical observation**  
The perfect BERT performance suggests transformer models may capture subtle semantic
patterns beyond what traditional features provide.

### [Most Frequent Words Analysis](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/most_frequent_words.ipynb)

**Methodology:**  

- Term frequency analysis across post sections (description/requirements/benefits)
- Cosine similarity matrix for cross-category comparison  
- Stopword-optimized counting (NLTK + custom job-specific terms)  

**Key Observations:**

| Category      | Top Words            | Distinct Characteristics            |
|---------------|----------------------|-------------------------------------|
| Real Jobs     | "management", "customer", "team" | Job-specific terminology|
| Human Scams   | "home", "online", "flexible"| Emphasis on work arrangements|
| LLM-Refined Scams  | "strategic", "dynamic", "cross" | Corporate buzzwords |

**Technical Implementation:**
***Libraries Used***
pandas , matplotlib, scikit-learn and NLTK

**Key Findings:**  

| Section        | Real vs Fake Similarity | Fake vs LLM Similarity |  
|----------------|-------------------------|------------------------|  
| Description    | 0.896                   | 0.267                  |  
| Requirements   | 0.953                   | 0.390                  |  
| Benefits       | 0.881                   | 0.989                  |  

**Insight:**  

***Research Implications***

- LLM Refinement Creates Distinct Style:
- Neither mimics real posts nor preserves original scam patterns
- Introduces new lexical characteristics (corporate jargon)

***Section-Specific Detection:***

- Requirements sections show greatest divergence (0.39 similarity)
- Benefits sections are poor differentiators (0.99 similarity)

***Hypothesis Rejection:***

- LLM-refined posts did not become more similar to real posts
- Created a third distinct category of job postings

## Department & Salary Analysis

### Analysis Steps

1. **Prepared Data**  
   - Combined job titles, departments, and industries into single descriptions  
   - Converted salary ranges to average numbers (e.g., "$50k-$70k" → $60k)  
   - Balanced the dataset to compare equal numbers of real/fake jobs  

2. **Grouped Similar Jobs**  
   - Used AI to automatically cluster jobs with similar roles  
   - Compared how many real vs. fake jobs appeared in each cluster  

3. **Compared Salaries**  
   - Calculated average salaries by cluster  
   - Checked for patterns in missing salary data  

### [Departments & Salaries Analysis](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/4_data_analysis/departments_salaries_comparison.ipynb)

### Tools Used

|Tool|Purpose|Why Chosen|
|---|---|---|
|Sentence Transformers|Group similar job descriptions|Understands meaning (not keywords)|
|HDBSCAN|Create job clusters|Handles overlapping categories|
|Matplotlib|Generate visualizations|Easy chart creation|

### Key Findings

#### Cluster Patterns

- **Goal**: Identify if scammers target specific job types  
- **Observation**:  
  - Fake jobs were evenly distributed across all industries  
  - No particular department was targeted more than others  

#### Salary Comparison  

- **Goal**: Verify if fake jobs offer higher salaries  
- **Observation**:  
  - When listed, fake job salaries were 24% higher on average  
  - 74% of fake jobs omitted salary data (vs 13% of real jobs)  

### Alternative Approaches

If this approach failed, we would have tried:  

1. Manual industry categorization (more precise but time-consuming)  
2. Direct job title comparisons (would miss similar roles with different names)
3. Salary-only analysis (would miss department patterns)  

**Key Insight**: Fake jobs don't target specific fields but often use inflated
salaries as bait when payment details are provided.

## **Key Findings:**

### Supporting Evidence for Research Question  

1. **AI-generated scams** are detectable through:  
   - Unnatural word distributions (TF-IDF)  
   - Overly balanced syntactic structures  
   - Lack of domain-specific named entities  

2. **Human scams** exhibit:  
   - Higher emotional valence (p<0.01)  
   - Urgency markers ("apply immediately")  
   - Simpler language complexity  

3. **Authentic posts** maintain:  
   - Consistent professional tone  
   - Role-specific terminology  
   - Balanced readability (grade 10-12)  
