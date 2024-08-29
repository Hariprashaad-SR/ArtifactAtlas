import React from 'react';
import "./styles3.css"; 
import {Link} from 'react-router-dom';

function Selection2() {
  return (
    <>
    <header style={{ margin : "0 0 1px 0", borderRadius : '0'}}>
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
    <div className="streamlit">
      <iframe
        src=" http://192.168.233.217:8501"
        width="99%"
        height="100%"
        title="Streamlit App"
      ></iframe>
    </div>

    <footer className="home__footer">
        <Link to = '/' ><div className="home__footer-icon home__footer-icon--home"></div></Link>
        <Link to="/assistant">
          <div className="home__footer-icon home__footer-icon--assistant"></div>
        </Link>
        <div className="home__footer-icon home__footer-icon--dashboard"></div>
        <div className="home__footer-icon home__footer-icon--profile"></div>
      </footer>
    </>
    
  );
}

export default Selection2;
