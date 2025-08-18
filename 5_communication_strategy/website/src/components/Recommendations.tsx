import React from 'react';
import { Lightbulb, ShieldCheck } from 'lucide-react';

interface Recommendation {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  points: React.ReactNode[];
  color: 'red' | 'rose' | 'gray';
}

const Recommendations: React.FC = () => {
  const recommendations: Recommendation[] = [
    {
      icon: Lightbulb,
      title: "For Job Seekers",
      points: [
        <span>
          <strong className="text-black">Protect Your Personal Information:</strong> Never share sensitive documents like your social security number or driver's license early in the hiring process. Always verify the company's legitimacy and purpose for the request before providing any personal information.
        </span>,
        <span>
          <strong className="text-black">Research the Company:</strong> Always cross-reference the company by checking for an official website and professional social media profiles. Be wary if their online presence is weak or appears unprofessional.
        </span>,
        <span>
          <strong className="text-black">Suspicious Email Addresses:</strong> Always check the sender's email address. A legitimate company will use a professional email address that matches its domain (e.g., careers@companyname.com). Be wary of emails sent from generic addresses like Gmail, Yahoo, or other free providers.
        </span>,
        <span>
          <strong className="text-black">Evaluate the Salary:</strong> Exercise caution if a job offers a salary that seems disproportionately high for the required experience. Unrealistically high pay is a common tactic used to lure applicants.
        </span>,
        <span>
          <strong className="text-black">Avoid Upfront Payments:</strong> Legitimate employers will never ask you to pay for equipment, training, or any other startup costs. Any request for money is a clear sign of a scam.
        </span>,
        <span>
          <strong className="text-black">Watch for Urgency and Vague Language:</strong> Be skeptical of phrases like "Apply Now!" or "Immediate Hire," which are designed to pressure you. Similarly, be wary of job descriptions that are overly generic and lack specific details about responsibilities.
        </span>,
        <span>
          <strong className="text-black">Spot Excessive Jargon:</strong> Look for job descriptions filled with corporate buzzwords and abstract phrases but short on clear, practical duties. Scammers use this to make a role sound impressive without providing real substance.
        </span>,
      ],
      color: "red"
    },
    {
      icon: ShieldCheck,
      title: "For Platforms",
      description: "To help protect users on a larger scale, we recommend that platforms implement these strategies:",
      points: [
        <span>
          <strong>Deploy NLP Filters:</strong> Utilize NLP filters to automatically flag job descriptions with unusual word patterns, emotional urgency cues, or suspicious grammar. This can help identify both human-written and AI-generated scams.
        </span>,
        <span>
          <strong>Continuously Update Detection Models:</strong> Scammers are always evolving. It is crucial to continuously update your fraud detection models to adapt to new AI-generated tactics and maintain effective protection for all users.
        </span>
      ],
      color: "rose"
    }
  ];

  const getColorClasses = (color: string) => {
    switch (color) {
      case 'red':
        return { bg: 'bg-red-50', icon: 'text-red-800', border: 'border-red-200', bulletBg: 'bg-red-700', bulletBorder: 'border-red-900' };
      case 'rose':
        return { bg: 'bg-rose-50', icon: 'text-rose-700', border: 'border-rose-200', bulletBg: 'bg-rose-700', bulletBorder: 'border-rose-900' };
      default:
        return { bg: 'bg-gray-50', icon: 'text-gray-600', border: 'border-gray-200', bulletBg: 'bg-gray-600', bulletBorder: 'border-gray-800' };
    }
  };

  return (
    <section id="actionable-insights" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-16 text-left">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">Key Recommendations</h2>
          <p className="text-xl text-black">
            Based on our analysis, we have developed a set of actionable recommendations for both job seekers and online platforms to help mitigate fraud and detect AI-refined job postings.
          </p>
        </div>

        <div className="space-y-12">
          {recommendations.map((rec, index) => {
            const colors = getColorClasses(rec.color);
            const Icon = rec.icon;

            return (
              <div key={index} className={`${colors.bg} ${colors.border} border-2 rounded-xl p-8 hover:shadow-lg transition`}>
                <div className="flex items-center space-x-4 mb-4">
                  <div className={`${colors.bg} p-4 rounded-full border-2 ${colors.border}`}>
                    <Icon className={`w-8 h-8 ${colors.icon}`} />
                  </div>
                  <h3 className="text-2xl font-bold text-gray-900">{rec.title}</h3>
                </div>
                <ul className="space-y-5"> {/* Extra space between bullet points */}
                  {rec.points.map((point, idx) => (
                    <li key={idx} className="flex items-start space-x-3">
                      <span className={`mt-2 w-1.5 h-1.5 rounded-full border-2 ${colors.bulletBg} ${colors.bulletBorder}`} />
                      <span className="text-black">{point}</span>
                    </li>
                  ))}
                </ul>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Recommendations;
