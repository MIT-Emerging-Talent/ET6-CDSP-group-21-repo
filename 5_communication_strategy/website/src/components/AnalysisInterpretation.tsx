import React from 'react';
import WordFrequencyImg from '/src/public/Words.png';
import ReadabilityImg from '/src/public/Readability.png';
import UrgencyImg from '/src/public/Urgency.png';
import DepartmentsImg from '/src/public/Departments.png';
import ClassificationImg from '/src/public/Classification.png';

const AnalysisInterpretation = () => {
  return (
    <section id="analysis-interpretation" className="py-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-none">
          <h2 className="text-4xl font-bold text-gray-900 mb-8">
            Detailed Analysis Interpretation
          </h2>

          <div className="space-y-16">
            {/* Text Analysis */}
            <div>
              <h3 className="text-3xl font-bold text-red-800 hover:text-red-900 mb-4">
                Text Analysis
              </h3>

              <div className="space-y-6">
                {/* Word Frequency */}
                <div className="flex flex-col md:flex-row md:items-start md:space-x-8">
                  <div className="md:w-1/2">
                    <h4 className="text-xl text-black italic font-medium mb-2">
                      Word Frequency and N-Gram Analysis:
                    </h4>
                    <p className="text-black leading-relaxed">
                      We identified the most frequent words and word sequences (n-grams) to find common patterns. Real jobs used job-specific terms, human scams used urgency-related words and generic words, and AI-refined posts used corporate jargon and buzzwords like <strong>"strategic"</strong> and <strong>"cross-functional synergy"</strong>.
                    </p>
                  </div>
                  <div className="md:w-1/2">
                    <img
                      src={WordFrequencyImg}
                      alt="Word Frequency"
                      className="w-full h-auto rounded-lg shadow-md"
                    />
                  </div>
                </div>

                {/* Readability */}
                <div className="flex flex-col md:flex-row md:items-start md:space-x-8">
                  <div className="md:w-1/2">
                    <h4 className="text-xl text-black italic font-medium mb-2">
                      Readability Assessment:
                    </h4>
                    <p className="text-black leading-relaxed">
                      We calculated Flesch-Kincaid and SMOG scores to measure the complexity and readability of the text. We found that human scams used simpler language, while AI scams were paradoxically complex but difficult to read.
                    </p>
                  </div>
                  <div className="md:w-1/2">
                    <img
                      src={ReadabilityImg}
                      alt="Readability"
                      className="w-full h-auto rounded-lg shadow-md"
                    />
                  </div>
                </div>

                {/* Emotional Tone */}
                <div className="flex flex-col md:flex-row md:items-start md:space-x-8">
                  <div className="md:w-1/2">
                    <h4 className="text-xl text-black italic font-medium mb-2">
                      Emotional Tone Detection:
                    </h4>
                    <p className="text-black leading-relaxed">
                      We used sentiment analysis tools to detect urgency and emotional markers. Human scams showed significantly higher emotional intensity compared to real or AI-generated posts.
                    </p>
                  </div>
                  <div className="md:w-1/2">
                    <img
                      src={UrgencyImg}
                      alt="Urgency Tone"
                      className="w-full h-auto rounded-lg shadow-md"
                    />
                  </div>
                </div>

                {/* POS Tagging */}
                <div>
                  <h4 className="text-xl text-black italic font-medium mb-2">
                    Part-of-Speech (POS) Tagging:
                  </h4>
                  <p className="text-black leading-relaxed">
                    By analyzing the ratio of different word types (nouns, verbs, adjectives), we found that human scams used more imperative verbs <strong>"apply now"</strong>, while AI scams overused adjectives and nominalizations.
                  </p>
                </div>
              </div>
            </div>

            {/* Feature-Based Analysis Section */}
            <div>
              <h3 className="text-3xl font-bold text-red-800 hover:text-red-900 mb-4">
                Feature-Based Analysis
              </h3>
              <p className="text-black text-lg mb-4 leading-relaxed">
                Beyond text, we analyzed other key features of the job postings.
              </p>

              {/* Departments and Salaries */}
              <div className="flex flex-col md:flex-row md:items-start md:space-x-8 mb-6">
                <div className="md:w-1/2">
                  <h4 className="text-xl text-black italic font-medium mb-2">
                    Department and Salary Analysis:
                  </h4>
                  <p className="text-black leading-relaxed">
                    We clustered similar job descriptions to see if scammers targeted specific roles. Fake jobs were spread across all departments and did not target specific departments, but were 24% more likely to offer an inflated salary when provided, with 74% of fake jobs omitting salary data entirely.
                  </p>
                </div>
                <div className="md:w-1/2">
                  <img
                    src={DepartmentsImg}
                    alt="Departments and Salaries"
                    className="w-full h-auto rounded-lg shadow-md"
                  />
                </div>
              </div>
            </div>

            {/* Model Building Section */}
            <div>
              <h3 className="text-3xl font-bold text-red-800 hover:text-red-900 mb-4">
                Model Building and Validation
              </h3>
              <p className="text-black text-lg mb-6 leading-relaxed">
                To validate our findings, we built and tested several machine learning models to classify the job postings.
              </p>

              <div className="space-y-4">
                <div>
                  <h4 className="text-xl text-black italic font-medium mb-2">
                    Feature Engineering:
                  </h4>
                  <p className="text-black leading-relaxed">
                    We converted our NLP findings into numerical features using methods like TF-IDF vectorization and proper noun counts.
                  </p>
                </div>

                <div>
                  <h4 className="text-xl text-black italic font-medium mb-2">
                    Classifier Modeling:
                  </h4>
                  <p className="text-black leading-relaxed">
                    We trained and tested models, including Logistic Regression, XGBoost, and BERT, using a balanced dataset of 866 real and 866 fake job posts.
                  </p>
                </div>

                {/* Performance and Classification */}
                <div className="flex flex-col md:flex-row md:items-start md:space-x-8">
                  <div className="md:w-1/2">
                    <h4 className="text-xl text-black italic font-medium mb-2">
                      Performance:
                    </h4>
                    <p className="text-black leading-relaxed">
                      Our models achieved near-perfect scores (1.00 precision and recall) in detecting fraudulent posts, confirming that the linguistic and structural markers we identified are highly effective at distinguishing scams from legitimate jobs.
                    </p>
                  </div>
                  <div className="md:w-1/2">
                    <img
                      src={ClassificationImg}
                      alt="Model Classification"
                      className="w-full h-auto rounded-lg shadow-md"
                    />
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default AnalysisInterpretation;
