import './home.css';
import Button from './components/button.js';
import Offer from './components/offer_card.js'

export default function Home() {
  return (
    < div>
        <section className="intro">
        <div className="intro-word">
            <p className="tagline"><span>Your Education,</span> all in one place</p>
            <p className='description'>Edvy is an innovative web platform designed to bridge the gap between students, teachers, and information</p>
            <Button text="sign-up"/>
        </div>
        <div className="intro-pic">
        </div>
      </section>
      <section className="offer">
        <h2>What we offer</h2>
        <div className="offer-cards">
          <Offer header="Connect"
          desc="Engage through interactive blog posts, forums, and discussion boards"/>
          <Offer header="Collaborate"
          desc="Facilitate real-time conversations between teachers and students"/>
          <Offer header="Optimize & Streamline"
          desc="Securely manage student and teacher information, including grades, attendance, and class schedules"/>
        </div>
      </section>
    </div>
  );
}
