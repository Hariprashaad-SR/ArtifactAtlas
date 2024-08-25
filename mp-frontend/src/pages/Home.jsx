import React from "react";
import "./styles.css"; 
import {Link} from 'react-router-dom';


function Home() {
  return (
    <div className="App">
      <header className="header">
        <img
          src="/museum-banner.png"
          alt="Museum Background"
          className="header-image"
        />
        <div className="overlay">
          <h4>Welcome to Museum Ticket Booker</h4>
        </div>
      </header>

      <main className="content">
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

        <h2>Key Features:</h2>
        <ul className="features-list">
          <li>
            <strong>24/7 Booking:</strong> No more waiting! Book your tickets
            anytime, even during off-hours.
          </li>
          <li>
            <strong>Instant Information:</strong> Get quick answers about ticket
            prices, exhibits, and more.
          </li>
          <li>
            <strong>Multilingual Support:</strong> Choose your preferred
            language for a personalized experience.
          </li>
          <li>
            <strong>Special Assistance:</strong> Accessibility options tailored
            to your needs for an inclusive visit.
          </li>
          <li>
            <strong>Secure Payments:</strong> Safe and easy transactions with
            integrated payment gateways.
          </li>
          <li>
            <strong>Environment-Friendly:</strong> Go paperless with digital
            tickets and confirmations.
          </li>
        </ul>

        <p>
          Explore the wonders of the museum, engage with history, art, and
          culture—all made easy with Museum Ticket Booker!
        </p>
        <br/>
      <br/>
      <br/>
      </main>
     

      <footer className="footer">
        <div className="footer-icon home"></div>
        <Link to="/assistant">
          <div className="footer-icon explore"></div>
        </Link>
        <div className="footer-icon explore"></div>
        <div className="footer-icon assistant"></div>
      </footer>
    </div>
  );
}

export default Home;
