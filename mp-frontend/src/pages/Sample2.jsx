import React, { useState } from "react";
import "./styles3.css"; 
import { Link } from 'react-router-dom';

function Sample() {
    const [lang, setLang] = useState("English");
    const [bookingOption, setBookingOption] = useState(null);
    const [museum, setMuseum] = useState(null);
    const [adultTickets, setAdultTickets] = useState(0);
    const [childTickets, setChildTickets] = useState(0);
    const [foreignVisitor, setForeignVisitor] = useState(null);
    const [photoVideo, setPhotoVideo] = useState(null);
    const [parking, setParking] = useState(null);
    const [payment, setPayment] = useState(null);
    const [totalBill, setTotalBill] = useState(0);

    const museumList = [
        "---", 
        "National Museum, Delhi", 
        "Indian Museum, Kolkata", 
        "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai", 
        "Salar Jung Museum, Hyderabad", 
        "Government Museum, Chennai", 
        "Albert Hall Museum, Jaipur"
    ];

    const handleBookingOption = (option) => {
        setBookingOption(option);
    };

    const handleMuseumSelection = (selectedMuseum) => {
        setMuseum(selectedMuseum);
    };

    const handleTicketChange = (type, value) => {
        if (type === "adult") {
            setAdultTickets(value);
            setTotalBill(totalBill + value * 15);
        } else {
            setChildTickets(value);
            setTotalBill(totalBill + value * 5);
        }
    };

    const handleForeignVisitor = (option) => {
        setForeignVisitor(option);
    };

    const handlePhotoVideo = (option) => {
        setPhotoVideo(option);
        if (option === "Yes") {
            setTotalBill(totalBill + 50);
        }
    };

    const handleParking = (option) => {
        setParking(option);
        if (option === "Yes") {
            setTotalBill(totalBill + 50);
        }
    };

    const handlePayment = (option) => {
        setPayment(option);
        if (option === "Yes") {
            alert("Proceeding to payment gateway...");
        } else {
            alert("Booking not completed.");
        }
    };

    return (
        <>
            <header>
                <Link to='/assistant'>
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" fill="currentColor" className="bi bi-arrow-left-circle" viewBox="0 0 16 16">
                        <path fillRule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                    </svg>
                </Link>
                <h3>Welcome to our Ticket Buddy Bot</h3>
            </header>
            <div className="chat-container">
                {!bookingOption && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>Hi! Are You Looking to Book your Museum Tickets?</p>
                            <div className="options">
                                <div className="option" onClick={() => handleBookingOption("Yes")}>Yes</div>
                                <div className="option" onClick={() => handleBookingOption("No")}>No</div>
                            </div>
                        </div>
                    </div>
                )}

                {bookingOption === "Yes" && !museum && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>Which museum are you interested in?</p>
                            <div className="options">
                                {museumList.map((m, index) => (
                                    <div key={index} className="option" onClick={() => handleMuseumSelection(m)}>{m}</div>
                                ))}
                            </div>
                        </div>
                    </div>
                )}

                {museum && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>How many adult tickets do you need? (₹15 each)</p>
                            <input type="number" min="0" value={adultTickets} onChange={(e) => handleTicketChange("adult", parseInt(e.target.value))} />
                            <p>How many children tickets do you need? (₹5 each)</p>
                            <input type="number" min="0" value={childTickets} onChange={(e) => handleTicketChange("child", parseInt(e.target.value))} />
                            <p>Are you a foreign visitor?</p>
                            <div className="options">
                                <div className="option" onClick={() => handleForeignVisitor("Yes")}>Yes</div>
                                <div className="option" onClick={() => handleForeignVisitor("No")}>No</div>
                            </div>
                        </div>
                    </div>
                )}

                {foreignVisitor && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>Do you want to take photos and videos in the museum? (+₹50)</p>
                            <div className="options">
                                <div className="option" onClick={() => handlePhotoVideo("Yes")}>Yes</div>
                                <div className="option" onClick={() => handlePhotoVideo("No")}>No</div>
                            </div>
                        </div>
                    </div>
                )}

                {photoVideo && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>Do you need parking? (+₹50)</p>
                            <div className="options">
                                <div className="option" onClick={() => handleParking("Yes")}>Yes</div>
                                <div className="option" onClick={() => handleParking("No")}>No</div>
                            </div>
                        </div>
                    </div>
                )}

                {parking && (
                    <div className="bot-message">
                        <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" className="bot-icon"/>
                        <div className="message-box">
                            <p>Your total bill amount is: ₹{totalBill}</p>
                            <p>Would you like to proceed with the payment?</p>
                            <div className="options">
                                <div className="option" onClick={() => handlePayment("Yes")}>Yes</div>
                                <div className="option" onClick={() => handlePayment("No")}>No</div>
                            </div>
                        </div>
                    </div>
                )}
            </div>

        <footer class="footer">
        <Link to = '/'><div class="footer-icon home"></div></Link>
        <Link to = '/assistant'><div class="footer-icon explore"></div></Link>
        <div class="footer-icon explore"></div>
        <div class="footer-icon assistant"></div>
    </footer>
    

    </>)
}

export default Sample;
