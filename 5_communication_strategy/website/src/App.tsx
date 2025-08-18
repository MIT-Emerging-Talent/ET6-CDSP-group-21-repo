import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import ProjectOverview from './components/ProjectOverview';
import Methodology from './components/Methodology';
import AnalysisInterpretation from './components/AnalysisInterpretation';
import Footer from './components/Footer';
import MeetTheTeam from "./components/MeetTheTeam";
import Recommendations from './components/Recommendations';

function App() {
  return (
    <div className="min-h-screen bg-white">
      <Header />
      <Hero />
      <ProjectOverview />
      <Methodology />
      <AnalysisInterpretation />
      <Recommendations />
      <Footer />
      <MeetTheTeam />
    </div>
  );
}

export default App;