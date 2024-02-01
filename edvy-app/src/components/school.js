import './school.css';
/* import React, { useState, useEffect } from 'react'; */
import Logo from './assets/school-default-icon.svg';

export default function Schools() {
  const logos = [
    { src: Logo, school: 'School1', alt: 'logo' },
    { src: Logo, school: 'School2', alt: 'logo' },
    { src: Logo, school: 'School3', alt: 'logo' },
    { src: Logo, school: 'School4', alt: 'logo' },
  ];
  /* const [currentIndex, setCurrentIndex] = useState(0);
  const animationDuration = 3000; */

  /* useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % (logos.length * 2));
    }, animationDuration / logos.length);
  
    return () => clearInterval(interval);
  }, [logos.length, animationDuration]);*/

  const logosStyle = {
    display: 'flex',
    width: `${(logos.length) * (4.9 + 5)}em`,
    /* transform: `translateX(-${(currentIndex - 1) * (4.9 + 4)}em)`, */
    /* animation: `slide ${animationDuration / 1000}s linear infinite`, */
    gap: '5em',
  }; 

  return (
    <div className="schools-container">
      <div className="school-logos" style={logosStyle}>
        {logos.map((logo, index) => (
          <div className="school-logos-inner" key={(index + logos.length) % logos.length}>
            <img src={logo.src} alt={logo.alt} />
            <p className="name">{logo.school}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
