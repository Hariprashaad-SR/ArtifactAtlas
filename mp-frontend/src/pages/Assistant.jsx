import React from "react";
import "./styles2.css";
import {Link} from 'react-router-dom';


function Assistant() {
  return <>
  <div className="header">
        <img src="museum-banner.png" alt="Museum Background" className="header-image"/>
        <div className="user-icon">
        </div>
    </div>

   
    <div className="content">

        <div className="cta-banner">
            <h4>BOOK YOUR TICKET WITH OUR TICKET BUDDY BOT</h4>
        </div>


        <div className="booking-option voice-booking">
            <h3>Voice-Based Booking:</h3>
            <p>Let our bot guide you through the ticket booking process using simple voice commands. Just speak, and we'll take care of the rest—quick, easy, and hands-free.</p>
            <a href="#" className="select-button">BOOK NOW <span>&#10140;</span></a>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLS1tf-JxMnFPMK8usb-NbexXblx-Qr3_AbA&s" alt="Voice Icon" className="icon"/>
        </div>

        <div className="booking-option selection-booking">
            <h3>Selection-Based Booking:</h3>
            <p>Prefer tapping through your options? No problem! Choose your preferences step by step with our intuitive selection interface. It's all about making your booking experience as comfortable as possible.</p>
            <a href="#" className="select-button">BOOK NOW <span>&#10140;</span></a>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTmd1Xq1vVqw4gQ6YtwmH7lODkPDVz0O7xvg&s" alt="Selection Icon" className="icon"/>
        </div>

        <div className="museum-carousel">
            <button className="carousel-button left">&#9664;</button>
            <div className="museum-image">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSaweybwd-KUyt8FzrCeIkeSTS50AyXpW5uA&s" alt="Chennai Egmore Museum"/>
                <div className="museum-label">CHENNAI EGMORE MUSEUM</div>
            </div>
            <button className="carousel-button right">&#9654;</button>
        </div>
    </div>
    <br/>
    <br/>
    <br/>

    <div className="footer">
        <Link to = '/'><div className="footer-icon home"></div></Link>
        <div className="footer-icon explore"></div>
        <div className="footer-icon explore"></div>
        <div className="footer-icon assistant"></div>
    </div>
  </>
    
}

export default Assistant;
