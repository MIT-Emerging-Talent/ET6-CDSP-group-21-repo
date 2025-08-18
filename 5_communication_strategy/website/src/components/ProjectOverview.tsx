import React, { useState, useRef, useEffect } from 'react';

const ProjectOverview = () => {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement>(null);
  const [barHeights, setBarHeights] = useState<number[]>(Array(20).fill(10));

  const handlePlayPause = () => {
    if (!audioRef.current) return;
    if (audioRef.current.paused) {
      audioRef.current.play();
      setIsPlaying(true);
    } else {
      audioRef.current.pause();
      setIsPlaying(false);
    }
  };

  // Animate bars while playing
  useEffect(() => {
    let animationId: number;
    const animateBars = () => {
      setBarHeights(prev =>
        prev.map(() => (isPlaying ? Math.random() * 80 + 20 : 10))
      );
      animationId = window.setTimeout(animateBars, 150);
    };
    if (isPlaying) animateBars();
    return () => clearTimeout(animationId);
  }, [isPlaying]);

  return (
    <section id="project-overview" className="py-16 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">Project Overview</h2>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          In the past, spotting a job scam was often easy. You could tell based on the language used, if it’s oddly phrased, with typos and grammatical mistakes, and not enough details about the role, then that would be your cue to leave the role behind. However, times have changed now with scammers having AI on their side.
        </p>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          One of the downsides of AI is that now everyone can use it for their favor, even scammers. It’s becoming even more difficult to detect scam jobs, especially when scammers are evolving more and more with this powerful tool. Scammers can now create fake job postings that are grammatically perfect, professional-sounding, and highly convincing, so we wanted to address this issue through our research.
        </p>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          This research aims to improve scam prevention strategies for both job seekers and online platforms. We studied human written real and fake job posts, along with AI-refined fake job posts. We’ve identified features and tactics scammers are now using. We’re sharing our findings with you to help you navigate this changing landscape and protect yourself from fraud.
        </p>

        <h3 className="text-2xl font-bold text-gray-900 mb-4">Participate in Our Study</h3>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          We’ve already completed the first phase of our research, where we tested how well machines can detect these new AI-powered scams. Now, for phase two, we need your help.
        </p>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          We're inviting job seekers to participate in our study to test humans' ability to spot fake jobs in a realistic setting. You'll use a job board we've built to review different postings and decide if they're legitimate. Your feedback is crucial and will provide invaluable insights for our research.
        </p>

        <p className="text-lg text-gray-600 mb-6 leading-relaxed">
          Ready to help us fight online fraud? Sign up today to participate.
        </p>

        <a
          href="https://forms.gle/sNGCd3DVmMtMroSr6"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block bg-red-800 hover:bg-red-900 text-white px-6 py-3 rounded-lg font-semibold transition-colors duration-200 mb-10"
        >
          Sign Up for Our Study
        </a>

        <p className="text-lg text-gray-600 mb-12 leading-relaxed">
          This research is done as part of our one-year journey with the <strong>MIT Emerging Talent</strong> program, an online certificate program in computer science and data analysis. Explore our full research on{' '}
          <a
            href="https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo"
            target="_blank"
            rel="noopener noreferrer"
            className="text-red-800 hover:text-red-900 font-semibold"
          >
            GitHub
          </a>.
        </p>

        {/* Podcast Section */}
        <div className="mt-12 p-8 bg-red-50 border-2 border-red-200 rounded-xl text-center">
          <h3 className="text-2xl font-bold text-gray-900 mb-4">Listen to Our Podcast</h3>
          <p className="text-lg text-gray-600 mb-6">
            Hear our latest discussion on fraudulent job detection in the era of AI.
          </p>

          {/* Pulsing Microphone */}
          <div className="flex justify-center mb-4">
            <svg
              className={`h-12 w-12 text-red-800 ${isPlaying ? 'animate-pulse' : ''}`}
              fill="currentColor"
              viewBox="0 0 24 24"
            >
              <path d="M12 1a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3zm5 10a5 5 0 0 1-10 0H5a7 7 0 0 0 14 0h-2zm-5 7a7 7 0 0 0 7-7h-2a5 5 0 0 1-10 0H5a7 7 0 0 0 7 7zm-1 4h2v2h-2v-2z" />
            </svg>
          </div>

          {/* Pulsing Bars */}
          <div className="flex justify-center items-end space-x-1 h-24 mb-6">
            {barHeights.map((height, idx) => (
              <div
                key={idx}
                className="w-2 bg-red-800 rounded-full transition-all duration-150"
                style={{ height: height + 'px' }}
              />
            ))}
          </div>

          {/* Hidden Audio */}
          <audio
            ref={audioRef}
            className="hidden"
            onPlay={() => setIsPlaying(true)}
            onPause={() => setIsPlaying(false)}
            onEnded={() => setIsPlaying(false)}
          >
            <source
              src="https://github.com/Alaa-Elgozouli/g21-podcast/raw/main/Podcast%20final.mp3"
              type="audio/mpeg"
            />
            Your browser does not support the audio element.
          </audio>

          {/* Play/Pause Button */}
          <button
            onClick={handlePlayPause}
            className="mt-4 bg-red-800 hover:bg-red-900 text-white px-6 py-3 rounded-lg font-semibold transition-colors duration-200"
          >
            {isPlaying ? 'Pause Podcast' : 'Play Podcast'}
          </button>
        </div>
      </div>
    </section>
  );
};

export default ProjectOverview;
