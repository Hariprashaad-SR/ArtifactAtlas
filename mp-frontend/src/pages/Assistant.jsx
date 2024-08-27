import React from "react";
import "./styles2.css";
import { Link } from 'react-router-dom';

function Assistant() {
  return (
    <>
      <div className="assistant__header">
        <img src="museum-banner.png" alt="Museum Background" className="assistant__header-image" />
        <div className="assistant__user-icon">
          {/* User Icon can be added here if needed */}
        </div>
      </div>

      <div className="assistant__content">
        <div className="assistant__cta-banner">
          <h4>BOOK YOUR TICKET WITH OUR TICKET BUDDY BOT</h4>
        </div>

        <div className="assistant__booking-option assistant__booking-option--voice">
          <h3 className="assistant__booking-option-heading">Voice-Based Booking:</h3>
          <p>Let our bot guide you through the ticket booking process using simple voice commands. Just speak, and we'll take care of the rest—quick, easy, and hands-free.</p>
          <a href="#" className="assistant__select-button">BOOK NOW <span className="assistant__select-button-text">&#10140;</span></a>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLS1tf-JxMnFPMK8usb-NbexXblx-Qr3_AbA&s" alt="Voice Icon" className="assistant__icon" />
        </div>

        <div className="assistant__booking-option assistant__booking-option--selection">
          <h3 className="assistant__booking-option-heading">Selection-Based Booking:</h3>
          <p>Prefer tapping through your options? No problem! Choose your preferences step by step with our intuitive selection interface. It's all about making your booking experience as comfortable as possible.</p>
          <Link to="/assistant/035" className="assistant__select-button">BOOK NOW <span className="assistant__select-button-text">&#10140;</span></Link>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTmd1Xq1vVqw4gQ6YtwmH7lODkPDVz0O7xvg&s" alt="Selection Icon" className="assistant__icon" />
        </div>

        <div className="assistant__museum-carousel">
          <button className="assistant__carousel-button assistant__carousel-button--left">&#9664;</button>
          <div className="assistant__museum-image">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSaweybwd-KUyt8FzrCeIkeSTS50AyXpW5uA&s" alt="Chennai Egmore Museum" />
            <div className="assistant__museum-label">CHENNAI EGMORE MUSEUM</div>
          </div>
          <button className="assistant__carousel-button assistant__carousel-button--right">&#9654;</button>
        </div>
      </div>
      <br />
      <br />
      <br />

      <div className="assistant__footer">
        <Link to='/'><div className="assistant__footer-icon assistant__footer-icon--home"></div></Link>
        <div className="assistant__footer-icon assistant__footer-icon--explore"></div>
        <div className="assistant__footer-icon assistant__footer-icon--explore"></div>
        <div className="assistant__footer-icon assistant__footer-icon--assistant"></div>
      </div>
    </>
  );
}

export default Assistant;
