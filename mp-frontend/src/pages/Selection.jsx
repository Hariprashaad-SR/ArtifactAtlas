import React from "react";
import "./styles3.css"; 
import {Link} from 'react-router-dom';


function Selection(){
    return <>
      <header>
      <Link to = '/assistant'><svg 
      xmlns="http://www.w3.org/2000/svg" 
      width="28" 
      fill="currentColor" 
      className="bi bi-arrow-left-circle" 
      viewBox="0 0 16 16"
    >
      <path 
        fillRule="evenodd" 
        d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"
      />
    </svg></Link>
        <h3>
            Welcome to our Ticket Buddy Bot
        </h3>
    </header>
    <div class="chat-container">
        <div class="bot-message">
            <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" class="bot-icon"/>
            <div class="message-box">
                <p>Hi! Are You Looking to Book your Museum Tickets?</p>
                <div class="options">
                    <div class="option yes">Yes</div>
                    <div class="option no">No</div>
                </div>
            </div>
        </div>


        <div class="user-message">
            <div class="user-response">Yes</div>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjK4Jnvmic3UxyEeSpei-rL0OkWTH0ktHUPyaXoV9LqnS6s2qczdbMMf0t61rTA4Zo-3Y&usqp=CAU" alt="User Icon" class="user-icon"/>
        </div>
        <div class="bot-message">
            <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" class="bot-icon"/>
            <div class="message-box">
                <p>Which musuem are you interested to go?</p>
                <div class="options">
                    <div class="option yes">Egmore</div>
                    <div class="option no">Some random one</div>
                </div>
            </div>
        </div>

        
        <div class="user-message">
            <div class="user-response">Egmore</div>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjK4Jnvmic3UxyEeSpei-rL0OkWTH0ktHUPyaXoV9LqnS6s2qczdbMMf0t61rTA4Zo-3Y&usqp=CAU" alt="User Icon" class="user-icon"/>
        </div>
        <div class="bot-message">
            <img src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg" alt="Bot Icon" class="bot-icon"/>
            <div class="message-box">
                <p>Are you a foreigner ?</p>
                <div class="options">
                    <div class="option select">Yes</div>
                    <div class="option select">No</div>
                </div>
            </div>
        </div>
        <br/>
        <br/>
        <br/>
    </div>

    <footer class="footer">
        <Link to = '/'><div class="footer-icon home"></div></Link>
        <Link to = '/assistant'><div class="footer-icon explore"></div></Link>
        <div class="footer-icon explore"></div>
        <div class="footer-icon assistant"></div>
    </footer>
    

    </>
}

export default Selection;