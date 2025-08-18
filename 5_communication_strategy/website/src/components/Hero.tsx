import React from 'react';
import { ChevronDown, Database, Brain, BarChart3 } from 'lucide-react';

const Hero = () => {
  // Generic scroll function
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="bg-gradient-to-br from-red-50 to-red-100 py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">
            Detecting Fake Jobs in the Era of AI
            <span className="text-red-800 block mt-2">Using NLP Analysis</span>
          </h1>
          
          <div className="flex justify-center space-x-6 mb-12">
            <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-full shadow-sm">
              <Database className="w-5 h-5 text-red-800" />
              <span className="text-sm font-medium text-gray-700">Employment Dataset</span>
            </div>
            <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-full shadow-sm">
              <Brain className="w-5 h-5 text-red-700" />
              <span className="text-sm font-medium text-gray-700">Gemini Refinement</span>
            </div>
            <div className="flex items-center space-x-2 bg-white px-4 py-2 rounded-full shadow-sm">
              <BarChart3 className="w-5 h-5 text-red-900" />
              <span className="text-sm font-medium text-gray-700">NLP Analysis</span>
            </div>
          </div>

          <button
            onClick={() => scrollToSection('project-overview')}
            className="bg-red-800 hover:bg-red-900 text-white px-8 py-3 rounded-lg font-semibold transition-colors duration-200 inline-flex items-center space-x-2"
          >
            <span>Learn More</span>
            <ChevronDown className="w-5 h-5" />
          </button>
        </div>
      </div>
    </section>
  );
};

export default Hero;
