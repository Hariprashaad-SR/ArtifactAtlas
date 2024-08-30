import React, { useState } from "react";
import "./styles3.css";
import { Link } from "react-router-dom";

function TicketBookingBot() {
  const questions = [
    {
      id: 1,
      question: "Welcome to our Ticket Buddy Bot Selection Based booking service. Choose Your Language:",
      type: "select",
      options: ["English", "हिंदी", "தமிழ்", "తెలుగు"],
      key: "language",
    },
    {
      id: 2,
      question: "Are you looking to book a museum ticket?",
      type: "select",
      options: ["Yes", "No"],
      key: "bookingInterest",
    },
    {
      id: 3,
      question: "Select a museum:",
      type: "select",
      options: [
        "National Museum, Delhi",
        "Indian Museum, Kolkata",
        "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai",
        "Salar Jung Museum, Hyderabad",
        "Government Museum, Chennai",
        "Albert Hall Museum, Jaipur",
      ],
      key: "museum",
    },
    {
      id: 4,
      question: "Number of adult tickets (₹15 each):",
      type: "number",
      key: "adultTickets",
    },
    {
      id: 5,
      question: "Number of children tickets (₹5 each):",
      type: "number",
      key: "childTickets",
    },
    {
      id: 6,
      question: "Is there any foreign visitor?",
      type: "select",
      options: ["Yes", "No"],
      key: "foreignVisitor",
    },
    {
      id: 7,
      question: "Upload ID proof (for foreign visitors):",
      type: "file",
      key: "idProof",
      condition: (responses) => responses.foreignVisitor === "Yes",
    },
    {
      id: 8,
      question: "Are you looking to take photos and videos in the museum?",
      type: "select",
      options: ["Yes", "No"],
      key: "photoPermission",
    },
    {
      id: 9,
      question: "Is parking required?",
      type: "select",
      options: ["Yes", "No"],
      key: "parking",
    },
    {
      id: 10,
      question: "Are you willing to process the payment?",
      type: "select",
      options: ["Yes", "No"],
      key: "payment",
    },
    {
      id: 11,
      question: "Thank you for visiting! Please reach out when you are ready to book.",
      type: "info",
      key: "farewell",
      condition: (responses) => responses.bookingInterest === "No" || responses.payment === "No",
    },
    {
      id: 12,
      question: "Booking confirmed! Your tickets have been booked successfully.",
      type: "info",
      key: "confirmation",
      condition: (responses) => responses.payment === "Yes",
    },
  ];

  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [responses, setResponses] = useState({});
  const [totalBill, setTotalBill] = useState(0);
  const [conversation, setConversation] = useState([]);

  const handleResponse = (response) => {
    const currentQuestion = questions[currentQuestionIndex];

    // Update responses state
    const updatedResponses = {
      ...responses,
      [currentQuestion.key]: response,
    };
    setResponses(updatedResponses);

    setConversation([
      ...conversation,
      { role: "bot", message: currentQuestion.question },
      { role: "user", message: formatResponse(response, currentQuestion.type) },
    ]);

    // Perform calculations if necessary
    if (currentQuestion.key === "adultTickets") {
      setTotalBill((prevTotal) => prevTotal + parseInt(response) * 15);
    }

    if (currentQuestion.key === "childTickets") {
      setTotalBill((prevTotal) => prevTotal + parseInt(response) * 5);
    }

    if (currentQuestion.key === "photoPermission" && response === "Yes") {
      setTotalBill((prevTotal) => prevTotal + 50);
    }

    if (currentQuestion.key === "parking" && response === "Yes") {
      setTotalBill((prevTotal) => prevTotal + 50);
    }

    // Determine next question index
    let nextIndex = currentQuestionIndex + 1;

    // Skip questions based on conditions
    while (
      nextIndex < questions.length &&
      questions[nextIndex].condition &&
      !questions[nextIndex].condition(updatedResponses)
    ) {
      nextIndex++;
    }

    // Display total bill before payment question
    if (currentQuestion.key === "parking") {
      setConversation((prev) => [
        ...prev,
        { role: "bot", message: `Total bill amount is ₹${totalBill}` },
      ]);
    }

    // Move to next question if exists
    if (nextIndex < questions.length) {
      setCurrentQuestionIndex(nextIndex);
    }
  };

  // Format response for display
  const formatResponse = (response, type) => {
    if (type === "file") {
      return response.name;
    }
    return response;
  };

  // Render current question
  const renderQuestion = () => {
    const currentQuestion = questions[currentQuestionIndex];

    // Handle end of conversation
    if (!currentQuestion) return null;

    // Render based on question type
    switch (currentQuestion.type) {
      case "select":
        return (
          <div className="bot-message">
            <img
              src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg"
              alt="Bot Icon"
              className="bot-icon"
            />
            <div className="message-box">
              <p>{currentQuestion.question}</p>
              <div className="options">
                {currentQuestion.options.map((option, index) => (
                  <div
                    key={index}
                    className="option"
                    onClick={() => handleResponse(option)}
                  >
                    {option}
                  </div>
                ))}
              </div>
            </div>
          </div>
        );

      case "number":
        return (
          <div className="bot-message">
            <img
              src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg"
              alt="Bot Icon"
              className="bot-icon"
            />
            <div className="message-box">
              <p>{currentQuestion.question}</p>
              <input
                type="number"
                min="0"
                onChange={(e) => handleResponse(e.target.value)}
                className="number-input"
              />
            </div>
          </div>
        );

      case "file":
        return (
          <div className="bot-message">
            <img
              src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg"
              alt="Bot Icon"
              className="bot-icon"
            />
            <div className="message-box">
              <p>{currentQuestion.question}</p>
              <input
                type="file"
                accept=".jpg,.jpeg,.png,.pdf"
                onChange={(e) => handleResponse(e.target.files[0])}
                className="file-input"
              />
            </div>
          </div>
        );

      case "info":
        return (
          <div className="bot-message">
            <img
              src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg"
              alt="Bot Icon"
              className="bot-icon"
            />
            <div className="message-box">
              <p>{currentQuestion.question}</p>
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <>
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
        <h3>Welcome to our Ticket Buddy Bot</h3>
      </header>

      <div className="chat-container">
        {conversation.map((msg, index) => (
          <div
            key={index}
            className={msg.role === "bot" ? "bot-message" : "user-message"}
          >
            {msg.role === "bot" ? (
              <>
                <img
                  src="https://img.freepik.com/premium-vector/chat-bot-logo-virtual-assistant-bot-icon-logo-robot-head-with-headphones_843540-99.jpg"
                  alt="Bot Icon"
                  className="bot-icon"
                />
                <div className="message-box">
                  <p>{msg.message}</p>
                </div>
              </>
            ) : (
                <div class="user-message">
            <div class="user-response">{msg.message}</div>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjK4Jnvmic3UxyEeSpei-rL0OkWTH0ktHUPyaXoV9LqnS6s2qczdbMMf0t61rTA4Zo-3Y&usqp=CAU" alt="User Icon" class="user-icon"/>
        </div>
            //   <>
            //     <div className="user-message">
            //       <p>{msg.message}</p>
            //     </div>
            //     <img
            //       src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjK4Jnvmic3UxyEeSpei-rL0OkWTH0ktHUPyaXoV9LqnS6s2qczdbMMf0t61rTA4Zo-3Y&usqp=CAU"
            //       alt="User Icon"
            //       className="user-icon"
            //     />
            //   </>
            )}
          </div>
        ))}

        {renderQuestion()}
        <br/>
        <br/>
        <br/>
      </div>

      <footer className="footer">
        <Link to="/">
          <div className="footer-icon home"></div>
        </Link>
        <Link to="/assistant">
          <div className="footer-icon explore"></div>
        </Link>
        <div className="footer-icon explore"></div>
        <div className="footer-icon assistant"></div>
      </footer>
    </>
  );
}

export default TicketBookingBot;
