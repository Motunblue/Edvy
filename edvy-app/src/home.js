import './home.css';
import Button from './components/button.js';

export default function Home() {
  return (
    < div>
        <section className="intro">
        <div className="intro-word">
            <p className="tagline"><span>Your Education,</span> all in one place</p>
            <p>Edvy is an innovative web platform designed to bridge the gap between students, teachers, and information</p>
            <Button />
        </div>
        <div className="intro-pic">
        </div>
      </section>
      <section className="offer">
        <h2>What we offer</h2>
        <div className="offer-cards">

        </div>
      </section>
    </div>
  );
}
