import React from 'react';

const Header = () => {
  const scrollToSection = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-4">
          <h1 className="text-2xl font-bold text-gray-900">
            Detecting Fake Jobs in the Era of AI
          </h1>
          <div className="hidden md:flex space-x-8">
            <button onClick={() => scrollToSection('methodology')} className="text-gray-600 hover:text-red-800 transition-colors font-medium">
              Methodology
            </button>
            <button onClick={() => scrollToSection('analysis-interpretation')} className="text-gray-600 hover:text-red-800 transition-colors font-medium">
              Technical Findings
            </button>
            <button onClick={() => scrollToSection('actionable-insights')} className="text-gray-600 hover:text-red-800 transition-colors font-medium">
              Actionable Insights
            </button>
            <button onClick={() => scrollToSection('meet-the-team')} className="text-gray-600 hover:text-red-800 transition-colors font-medium">
              Team
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
