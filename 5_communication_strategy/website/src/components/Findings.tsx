import React from 'react';
import { TrendingUp, AlertTriangle, CheckCircle, Eye } from 'lucide-react';

const Findings = () => {
  const keyFindings = [
    {
      icon: AlertTriangle,
      title: "17 Statistically Significant Scam Markers",
      description: "Identified distinct linguistic patterns with statistical significance (p<0.01) that differentiate fraudulent from authentic job postings",
      stat: "17",
      color: "red"
    },
    {
      icon: TrendingUp,
      title: "Perfect Classification Accuracy",
      description: "BERT model achieved 100% accuracy in detecting fraudulent jobs, with XGBoost at 99% and Logistic Regression at 98%",
      stat: "100%",
      color: "rose"
    },
    {
      icon: Eye,
      title: "Linguistic Divergence",
      description: "AI scams used 23% more adjectives and corporate jargon, while human scams contained 42% more urgency-related phrases",
      stat: "23%",
      color: "red"
    },
    {
      icon: CheckCircle,
      title: "Readability Analysis",
      description: "Real posts maintained balanced readability (grade 10-12), human scams used simpler language (grade 7-8), AI scams were paradoxically complex",
      stat: "Grade 10-12",
      color: "rose"
    },
    {
      icon: TrendingUp,
      title: "Salary Inflation Pattern",
      description: "When salary data was provided, fake jobs offered 24% higher salaries on average, but 74% omitted salary information entirely",
      stat: "24%",
      color: "red"
    }
  ];

  const getColorClasses = (color: string) => {
    switch (color) {
      case 'red':
        return { bg: 'bg-red-50', icon: 'text-red-800', accent: 'text-red-800' };
      case 'rose':
        return { bg: 'bg-rose-50', icon: 'text-rose-700', accent: 'text-rose-700' };
      default:
        return { bg: 'bg-gray-50', icon: 'text-gray-600', accent: 'text-gray-600' };
    }
  };

  return (
    <section id="findings" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">Key Findings</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Our comprehensive NLP analysis reveals distinct linguistic patterns and detection capabilities 
            across real, human-fake, and AI-refined job postings.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          {keyFindings.map((finding, index) => {
            const colors = getColorClasses(finding.color);
            const Icon = finding.icon;
            
            return (
              <div key={index} className={`${colors.bg} p-8 rounded-xl border border-gray-200 hover:shadow-lg transition-all duration-300`}>
                <div className="flex items-start space-x-4">
                  <div className="flex-shrink-0">
                    <Icon className={`w-8 h-8 ${colors.icon}`} />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-xl font-bold text-gray-900 mb-2">{finding.title}</h3>
                    <p className="text-gray-600 mb-4">{finding.description}</p>
                    <div className={`text-3xl font-bold ${colors.accent}`}>
                      {finding.stat}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Placeholder for data visualizations */}
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-200">
          <h3 className="text-2xl font-bold text-gray-900 mb-6 text-center">Data Visualizations</h3>
          <div className="mb-6 p-4 bg-gray-50 rounded-lg">
            <h4 className="text-lg font-semibold text-gray-800 mb-2">Key Limitations</h4>
            <ul className="space-y-2 text-gray-600">
              <li>• <strong>NLP:</strong> Presence of missing values; filling them with synthetic values could have led to more consistent findings.</li>
              <li>• <strong>Classification:</strong> The 100% accuracy is highly dependent on the data we used and not necessarily a universal solution.</li>
            </ul>
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div className="bg-gray-50 p-6 rounded-lg border-2 border-dashed border-gray-300">
              <h4 className="text-lg font-semibold text-gray-700 mb-4">TF-IDF & N-gram Analysis</h4>
              <p className="text-gray-600">Word frequency patterns and n-gram distributions showing distinct linguistic fingerprints across the three categories.</p>
              <div className="mt-4 text-sm text-red-800 font-medium">Chart placeholder - Integration ready</div>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg border-2 border-dashed border-gray-300">
              <h4 className="text-lg font-semibold text-gray-700 mb-4">Model Performance Metrics</h4>
              <p className="text-gray-600">Classification results from Logistic Regression, XGBoost, and BERT models with precision and recall scores.</p>
              <div className="mt-4 text-sm text-red-800 font-medium">Chart placeholder - Integration ready</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Findings;