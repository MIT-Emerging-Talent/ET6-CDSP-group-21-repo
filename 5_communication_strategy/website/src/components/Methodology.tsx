import React from 'react';
import { Users, Sparkles, Search, ArrowRight } from 'lucide-react';

interface Phase {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  description: string;
  details: React.ReactNode[];
  color: 'red' | 'rose' | 'gray';
  limitations?: string[];
}

const Methodology: React.FC = () => {
  const phases: Phase[] = [
    {
      icon: Users,
      title: "Phase 1: Dataset Preparation",
      description: "To begin, we built a comprehensive set of data for analysis. This included:",
      details: [
        <>
          <strong>Real Job Postings:</strong> We used 17,014 legitimate job postings from{' '}
          <a
            href="https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/tree/main/1_datasets/aegean_raw_data"
            target="_blank"
            rel="noopener noreferrer"
            className="text-red-800 hover:text-red-900 font-medium"
          >
            employment dataset
          </a>.
        </>,
        <>
          <strong>Fraudulent Job Postings:</strong> From the same dataset, we isolated 866 fake job postings.
        </>,
        <>
          <strong>Modern Job Postings:</strong> To ensure our research was relevant to today's job market, we scraped an additional 500 real job postings from Indeed to represent modern industry standards.
        </>,
        // Last paragraph as regular text, with extra spacing
        <>
          All of this data underwent a rigorous cleaning and feature extraction process to prepare it for analysis. It's important to note that the dataset was highly imbalanced, with only almost 4.86% labeled as fake jobs.
        </>
      ],
      color: "red"
    },
    {
      icon: Sparkles,
      title: "Phase 2: Gemini AI Refinement",
      description: "Enhanced fraudulent job postings using Gemini, focusing on job descriptions and related content for comparison analysis.",
      details: [
        <>
          To simulate how scammers use AI, we took the 866 fake job descriptions and fed them into the Gemini 2.5 Flash API. Our goal was to refine the language and structure, making them appear more professional and modern. By doing this, we were able to create a new set of AI-generated fraudulent posts for a direct comparison with the original, human-written scams.
        </>,
        <>
          It's important to note that while this process provides valuable insights, our AI-refined posts may contain unique patterns not yet adopted by real-world scammers. Additionally, the human-written scams from 2012-2014 may reflect outdated tactics.
        </>
      ],
      color: "rose",
    },
    {
      icon: Search,
      title: "Phase 3: Analysis and Model Development",
      description: "In our final phase, we used a multi-pronged strategy to uncover the red flags of modern scams.",
      details: [
        <>
          <strong>Linguistic Analysis:</strong> We performed an in-depth linguistic analysis to profile the language of each job posting. This included examining readability scores, common phrases (n-grams), emotional tone, and grammar patterns (POS tagging).
        </>,
        <>
          <strong>Socio-Economic Patterns:</strong> We analyzed departments, industries, and salaries to identify trends. We found that while scammers don't target specific fields, they frequently use inflated salaries as a lure. However, it's worth noting that 74.2% of fake jobs had no salary information, which was a key limitation in this analysis.
        </>,
        <>
          <strong>Machine Learning Models:</strong> Finally, we used these findings to train and test several machine learning models. Our top-performing classifiers, including XGBoost, were able to accurately distinguish between legitimate and fraudulent posts based on the patterns we uncovered.
        </>
      ],
      color: "red",
    }
  ];

  const getColorClasses = (color: string) => {
    switch (color) {
      case 'red':
        return {
          bg: 'bg-red-50',
          icon: 'text-red-800',
          border: 'border-red-200',
          bulletBg: 'bg-red-700',
          bulletBorder: 'border-red-900'
        };
      case 'rose':
        return {
          bg: 'bg-rose-50',
          icon: 'text-rose-700',
          border: 'border-rose-200',
          bulletBg: 'bg-rose-700',
          bulletBorder: 'border-rose-900'
        };
      default:
        return {
          bg: 'bg-gray-50',
          icon: 'text-gray-600',
          border: 'border-gray-200',
          bulletBg: 'bg-gray-600',
          bulletBorder: 'border-gray-800'
        };
    }
  };

  return (
    <section id="methodology" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-16 space-y-8">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">Research Methodology</h2>

          <p className="text-xl text-gray-600">
            Our study uses a systematic method to understand the evolution of job scams. We started with a large dataset of nearly <strong>18,000 job postings</strong>, originally collected between 2012 and 2014. This dataset included both real and fake job ads, with almost 800 identified as scams.
          </p>

          <p className="text-xl text-gray-600">
            Next, we used advanced <strong>AI refinement techniques</strong> on the fake job posts. This allowed us to simulate how scammers are now using AI to make their fraudulent ads more convincing. By comparing these new, AI-generated scams with the original human-written ones, we were able to pinpoint the subtle linguistic and structural changes that make them harder to spot.
          </p>

          <p className="text-xl text-gray-600">
            Finally, we used sophisticated <strong>NLP (Natural Language Processing) methods</strong> to analyze these patterns. Our goal was to find the specific keywords, phrases, and writing styles that act as modern red flags for fraudulent posts. This work is the foundation for creating better scam prevention tools for everyone.
          </p>
        </div>

        {/* Phases */}
        <div className="space-y-12">
          {phases.map((phase, index) => {
            const colors = getColorClasses(phase.color);
            const Icon = phase.icon;

            return (
              <div key={index}>
                <div className={`${colors.bg} ${colors.border} border-2 rounded-xl p-8 hover:shadow-lg transition`}>
                  {/* Icon + Title */}
                  <div className="flex items-center space-x-4 mb-4">
                    <div className={`${colors.bg} p-4 rounded-full border-2 ${colors.border}`}>
                      <Icon className={`w-8 h-8 ${colors.icon}`} />
                    </div>
                    <h3 className="text-2xl font-bold text-gray-900">{phase.title}</h3>
                  </div>

                  {/* Description */}
                  <p className="text-gray-600 text-lg mb-6">{phase.description}</p>

                  {/* Details */}
                  <ul className="space-y-3">
                    {phase.details.map((detail, detailIndex) => {
                      const isPhase1LastParagraph = index === 0 && detailIndex === phase.details.length - 1;
                      if (isPhase1LastParagraph) {
                        return (
                          <p key={detailIndex} className="text-gray-600 text-lg mt-6">{detail}</p> // extra spacing added
                        );
                      }
                      return (
                        <li key={detailIndex} className="flex items-start space-x-3">
                          <span className={`mt-2 w-1.5 h-1.5 rounded-full border-2 ${colors.bulletBg} ${colors.bulletBorder}`} />
                          <span className="text-gray-700">{detail}</span>
                        </li>
                      );
                    })}
                  </ul>

                  {/* Limitations */}
                  {phase.limitations && (
                    <div className="mt-6">
                      <h4 className="text-lg font-semibold text-gray-800 mb-3">Limitations</h4>
                      <ul className="space-y-2">
                        {phase.limitations.map((limitation, limitIndex) => (
                          <li key={limitIndex} className="flex items-start space-x-3">
                            <span
                              className={`mt-2 w-1.5 h-1.5 rounded-full border-2 ${
                                phase.color === 'red'
                                  ? 'bg-red-700 border-red-900'
                                  : 'bg-rose-700 border-rose-900'
                              }`}
                            />
                            <span className="text-gray-700">{limitation}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>

                {/* Arrow between phases */}
                {index < phases.length - 1 && (
                  <div className="flex justify-center my-6">
                    <ArrowRight className="w-6 h-6 text-gray-400" />
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Methodology;
