import React from "react";
import { Link } from 'react-router-dom';
import './styles.css';  // Make sure this path is correct

function Home() {
  return (
    <div className="home">
      <header className="home__header" style = {{margin : '0 0 0 0 '}}>
        <img
          src="/museum-banner.png"
          alt="Museum Background"
          className="home__header-image"
        />
        <div className="home__overlay">
          <h4 className="home__overlay-heading">Welcome to Museum Ticket Booker</h4>
        </div>
      </header>

      <main className="home__content">
        <p>
          Experience hassle-free museum visits with our smart, multilingual
          ticket booking assistant.
        </p>
        <p>
          Skip the queues and book your tickets from anywhere, anytime, with
          just a few taps. Our app offers instant access to ticket availability,
          museum hours, special events, and much more.
        </p>
        <p>
          Whether you're planning a solo visit, a family outing, or a group
          tour, our Ticket Buddy Bot guides you through a seamless booking
          process, ensuring a smooth and enjoyable visit. You'll receive your
          digital tickets instantly, making your museum experience more
          convenient and eco-friendly.
        </p>

        <h2 className="home__section-title">Key Features:</h2>
        <ul className="home__features-list">
          <li className="home__feature-item">
            <strong>24/7 Booking:</strong> No more waiting! Book your tickets
            anytime, even during off-hours.
          </li>
          <li className="home__feature-item">
            <strong>Instant Information:</strong> Get quick answers about ticket
            prices, exhibits, and more.
          </li>
          <li className="home__feature-item">
            <strong>Multilingual Support:</strong> Choose your preferred
            language for a personalized experience.
          </li>
          <li className="home__feature-item">
            <strong>Special Assistance:</strong> Accessibility options tailored
            to your needs for an inclusive visit.
          </li>
          <li className="home__feature-item">
            <strong>Secure Payments:</strong> Safe and easy transactions with
            integrated payment gateways.
          </li>
          <li className="home__feature-item">
            <strong>Environment-Friendly:</strong> Go paperless with digital
            tickets and confirmations.
          </li>
        </ul>

        <p class = 'home__center-para'>
          Explore the wonders of the museum, engage with history, art, and
          culture—all made easy with Museum Ticket Booker!
        </p>
        <br/>
        <br/>
        <br/>
      </main>

      <footer className="home__footer">
        <Link to = '/' ><div className="home__footer-icon home__footer-icon--home"></div></Link>
        <Link to="/assistant">
          <div className="home__footer-icon home__footer-icon--assistant"></div>
        </Link>
        <div className="home__footer-icon home__footer-icon--dashboard"></div>
        <div className="home__footer-icon home__footer-icon--profile"></div>
      </footer>
    </div>
  );
}

export default Home;
