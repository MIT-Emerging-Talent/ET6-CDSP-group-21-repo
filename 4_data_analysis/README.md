# Data Analysis: Detecting Fake Job Posts

## Job Posting Authenticity Analysis  

*Detecting Linguistic Patterns in AI-Generated and Human-Written Fraudulent Job
Listings" explores a comprehensive linguistic and machine learning approach to
identify fraudulent job postings by analyzing distinct language features in both
AI-generated and human-written scams.*

## Research Overview  

### Core Research Question  

**Can quantitative linguistic analysis combined with machine learning reliably
differentiate between:**

1. Authentic human-written job postings  
2. Human-crafted fraudulent job postings  
3. AI-generated fraudulent job postings?

### Team Contributions  

**MIT Emerging Talent Group 21 (ET6-CDSP-group-21-repo)** implemented a
multi-modal analysis approach:

| Team Member         | Primary Contribution Area                  |
|---------------------|--------------------------------------------|
| **Aseel Omer**      | Readability metrics & n-gram analysis      |
| **Justina Elocodes**| Model architecture & optimization          |
| **Majd Abualsoud**  | TF-IDF feature engineering & analysis      |
| **Rouaa Hamza**     | Emotional tone & urgency detection         |
| **Alaa Elgozouli**  | Lexical frequency & salary analysis        |
| **Geehan Ali**      | POS tagging and syntactic analysis         |

## Key Observations  

### 1. Linguistic Anomalies  

**What we noticed:**  

- **AI-generated posts** exhibited unnatural lexical choices, favoring:  
  - Overly formal terms ("exhibits" vs "shows")  
  - Medium-frequency corporate jargon ("synergistic," "leverage")  
  - Uncommon word pairings ("delve into the ramifications")  

- **Human scams** relied on:  
  - Emotional persuasion ("Limited time opportunity!")  
  - Simplified language (lower Flesch-Kincaid grade levels)  
  - Generic benefits ("work from home") rather than role specifics  

**How this supports our research:**  
These patterns directly address our core question by demonstrating measurable
differences in how humans and AI systems construct fraudulent posts compared to
authentic ones. The consistency of these markers across datasets suggests they
may serve as reliable detection signals.

### 2. Model Performance  

**What we noticed:**  
Our classifiers (Logistic Regression, XGBoost) achieved 100% accuracy when
distinguishing:  

- AI-generated posts (from our LLM)  
- Human-written scams (Aegean dataset)  
- Authentic postings (Indeed-sourced)  

**Critical observation:**  
This perfect separation primarily reflected stark stylistic differences between
our specific data sources rather than universal scam detection capability.
The models effectively learned to distinguish our LLM's "writing fingerprint"
from Indeed's posting style.

### 3. Salary and Department Patterns  

**What we noticed:**  

- 74.2% of fake posts omitted salary data (vs 12.1% of real posts)  
- When present, fake salaries averaged 28% higher than real counterparts for
similar roles  
- No targeting of specific industries - scams appeared across all sectors  

## Methodological Approach  

### Data Composition  

| Dataset          | Source             | Count  | Type               |  
|------------------|--------------------|--------|--------------------|  
| Authentic Jobs   | Aegean + Indeed    | 17,514 | Human-written      |  
| Human Scams      | Aegean (2012-2014) | 866    | Human-written fake |  
| AI Scams         | LLM-generated      | 500    | GPT-refined        |  

### Analytical Techniques  

1. **Textual Feature Extraction**  
   - TF-IDF vectorization (unigrams/bigrams)  
   - Named Entity Recognition (spaCy)  
   - Readability metrics (Flesch, SMOG)  

2. **Pattern Analysis**  
   - N-gram frequency comparisons  
   - Cosine similarity between datasets  
   - Emotional tone classification  

3. **Model Development**  
   - Logistic Regression (baseline)  
   - XGBoost (best performer)  
   - SHAP analysis for feature importance  

## Key Findings  

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

## Limitations and Future Directions  

### Current Constraints  

- Dataset bias: Models may not generalize to other LLM outputs  
- Temporal factors: Human scam tactics evolve faster than AI patterns  
- Feature dependence: Reliance on textual features ignores visual/webpage cues  

### Recommended Next Steps  

1. Expand data collection to include:  
   - Multi-platform authentic posts (LinkedIn, Glassdoor)  
   - Varied LLM sources (Claude, Gemini)  
2. Develop hybrid models incorporating:  
   - Perplexity scoring  
   - Layout analysis  
3. Conduct human evaluation studies to:  
   - Compare detection capability vs. models  
   - Identify cognitive scam markers  

### TF-IDF Findings

**What we observed:**  

- **AI-generated posts** exhibited:  
  - 37% higher mean TF-IDF scores for corporate buzzwords ("synergistic", "paradigm")
  - Inverse document frequency (IDF) values clustered in 2.1-3.8 range vs 1.5-2.9
  for human text  
  - Notable absence of industry-specific low-IDF terms  

- **Human scams** showed:  
  - 22% more imperative verbs ("apply now", "contact immediately")  
  - Higher TF for benefit-related terms ("flexible", "remote")  

**How this answers our question:**  
The TF-IDF matrix revealed statistically significant (p<0.001) differences in
term importance distributions across the three categories, providing our models
with discriminative features.

#### Readability Metrics

**Key data points:**  

| Metric             | Authentic | Human Scam | AI Scam |  
|--------------------|-----------|------------|---------|  
| Flesch Reading Ease| 58.2      | 72.1       | 42.3    |  
| Avg. Grade Level   | 10.4      | 7.8        | 13.2    |  
| Sentence Complexity| 1.82      | 1.31       | 2.15    |  

**Critical insight:**  
AI-generated posts paradoxically scored both higher in grade level (more complex)
 yet lower in readability (more difficult), indicating unnatural syntactic structures.

### 2. Model Development & Performance  

#### Feature Engineering  

We created a 1,752-dimensional feature space combining:  

1. **Lexical features**:  
   - TF-IDF (1-3 grams)  
   - Word2Vec embeddings (300D)  
2. **Syntactic features**:  
   - POS tag ratios (noun/verb density)  
   - Dependency tree depth  
3. **Stylistic features**:  
   - Readability scores  
   - Punctuation frequency  

#### Classification Results  

| Model              | Precision | Recall | F1   | Feature Importance Top 3 |  
|--------------------|-----------|--------|------|---------------------------|  
| Logistic Regression| 0.98      | 0.97   | 0.98 | 1. TF-IDF "salary"        |  
| XGBoost            | 0.99      | 0.99   | 0.99 | 2. NER ORG count          |  
| BERT (fine-tuned)  | 1.00      | 1.00   | 1.00 | 3. Flesch-Kincaid score   |  

**Critical observation from Elocodes:**  
The perfect BERT performance suggests transformer models may capture subtle
semantic patterns beyond what traditional features provide.

### 3. Sector-Specific Patterns  

#### Salary Analysis  

- **Data completeness**:  
  - 87.9% of real posts included salary data  
  - Only 25.8% of fake posts contained salary information  

- **When present**:  
  - Fake post salaries were inflated by mean of 28.4% (SD=12.7)  
  - Used round numbers ($50,000) 73% more frequently than authentic posts  

#### Department Clustering  

HDBSCAN revealed:  

- No significant clustering by industry for fake posts  
- Authentic posts showed natural clustering by:  
  - Technical roles (programming languages)  
  - Healthcare (certification requirements)  

## Methodological Deep Dive  

### Data Pipeline  

1. **Preprocessing**:  
   - Unicode normalization  
   - Industry-specific stopword removal  
   - Salary range standardization  
