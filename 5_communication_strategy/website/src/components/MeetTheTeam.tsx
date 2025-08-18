import React from 'react';
import AlaaImg from '/src/public/Alaa.jpg';
import AseelImg from '/src/public/Aseel.png';
import JustinaImg from '/src/public/Justina.png';
import MajdImg from '/src/public/Majd.png';
import RouaaImg from '/src/public/Rouaa.png';
import GeehanImg from '/src/public/Geehan.png';

const MeetTheTeam = () => {
  return (
    <section
      id="meet-the-team"
      className="py-20 bg-gradient-to-b from-gray-900 via-red-900 to-red-700"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-4xl font-bold text-white mb-12 text-center">
          Meet The Team
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
          {[
            { img: AlaaImg, name: "Alaa Mohamed", linkedin: "https://www.linkedin.com/in/alaa-hashim-9a9570202/" },
            { img: AseelImg, name: "Aseel Omer", linkedin: "https://www.linkedin.com/in/aseel-omer-61115826b/" },
            { img: JustinaImg, name: "Justina Odoeze", linkedin: "https://www.linkedin.com/in/elochukwuodoeze" },
            { img: MajdImg, name: "Majd Abualsoud", linkedin: "https://www.linkedin.com/in/majd-abualsoud/" },
            { img: RouaaImg, name: "Rouaa Hamzah" },
            { img: GeehanImg, name: "Geehan Ali" }
          ].map((member, idx) => (
            <div key={idx} className="text-center">
              {member.linkedin ? (
                <a href={member.linkedin} target="_blank" rel="noopener noreferrer">
                  <img
                    src={member.img}
                    alt={member.name}
                    className="mx-auto rounded-full w-40 h-40 shadow-2xl transition-transform duration-300 hover:scale-105"
                  />
                </a>
              ) : (
                <img
                  src={member.img}
                  alt={member.name}
                  className="mx-auto rounded-full w-40 h-40 shadow-2xl"
                />
              )}
              <p className="mt-2 text-white font-bold hover:text-red-300">{member.name}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default MeetTheTeam;
