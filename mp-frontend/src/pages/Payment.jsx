import './pay.css'
import { Link } from 'react-router-dom';

function Payment(){
    const handleClick = () => {
        const phoneNumber = 'hariprashaadsrofficial@okhdfcbank';
        const amount = 162.50;
        const upiLink = `upi://pay?pa=${phoneNumber}&am=${amount}&cu=INR`;
    
        // Redirecting to the UPI link
        window.location.href = upiLink;
      };
    return <>
    <header style = {{width : '110%', height : '110%', justifyContent : "flex-start", margin : " 0 0 0 0"}}>
      <Link to = '/assistant'><svg 
      xmlns="http://www.w3.org/2000/svg" 
      width="28" 
      fill="currentColor" 
      className="bi bi-arrow-left-circle" 
      viewBox="0 0 16 16"
      style = {{margin :'10px'}}
    >
      <path 
        fillRule="evenodd" 
        d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"
      />
    </svg></Link>
        <h3>
            Billing
        </h3>
    </header>
    <div class="checkout-container">
        <form id="checkout-form">
            <div class="billing-section">
            
                <div class="coolinput">
                    <label class="text" for="phone">Phone</label>
                    <input type="tel" id="phone" name="phone" class="input"/>
                    <div id="phone-error" class="error-message"></div>
                </div>
            </div>

            <div class="payment-section">
                <h2>Payment Method</h2>
                <div class="payment-option">
                    <input type="radio" id="upi" name="payment-method" value="upi"/>
                    <label for="upi">
                        <span>UPI</span>
                        <img src="https://akm-img-a-in.tosshub.com/indiatoday/images/story/202206/gpay_1200x768.jpeg" alt="UPI"/>
                    </label>
                    <p>You will be redirected to the Google-pay website after submission</p>
                </div>
                <div class="payment-option">
                    <input type="radio" id="paypal" name="payment-method" value="paypal"/>
                    <label for="paypal">
                        <span>PayPal</span>
                        <img src="https://www.paypalobjects.com/webstatic/icon/pp258.png" alt="PayPal"/>
                    </label>
                    <p>You will be redirected to the PayPal website after submission</p>
                </div>
                <div class="payment-option">
                    <input type="radio" id="credit-card" name="payment-method" value="credit-card"/>
                    <label for="credit-card">
                        <span>Pay with Credit Card</span>
                        <div class="credit-card-logos">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png" alt="Visa"/>
                        </div>
                    </label>
                    <div id="credit-card-info">
                        <div class="coolinput">
                            <label class="text" for="card-number">Card number</label>
                            <input type="text" id="card-number" name="card-number" class="input"/>
                            <div id="card-number-error" class="error-message"></div>
                        </div>
                        <div class="coolinput">
                            <label class="text" for="card-expiry">MM/YY</label>
                            <input type="text" id="card-expiry" name="card-expiry" class="input"/>
                            <div id="card-expiry-error" class="error-message"></div>
                        </div>
                        <div class="coolinput">
                            <label class="text" for="card-cvc">Card Security Code</label>
                            <input type="text" id="card-cvc" name="card-cvc" class="input"/>
                            <div id="card-cvc-error" class="error-message"></div>
                        </div>
                    </div>
                </div>
                <div class="payment-info">
                    <p>We protect your payment information using encryption to provide bank-level security.</p>
                </div>
            </div>

            <div class="order-review-section">
                <h2>Ticket summary</h2>
                <div class="order-item">
     
    <img src="https://cdn3.vectorstock.com/i/1000x1000/40/57/cartoon-man-male-parent-family-adult-member-vector-15024057.jpg" alt="Adult"/>
                    <div class="item-details">
                        <p>Adult</p>
                        <div class="quantity-selector">
                            <button type="button" class="quantity-btn" onclick="decreaseQuantity(this)">-</button>
                            <input type="text" class="quantity-input" value="3" readonly/>
                            <button type="button" class="quantity-btn" onclick="increaseQuantity(this)">+</button>
                        </div>
                    </div>
                    <p class="item-price">₹45.00</p>
                    <button type="button" class="remove-item-btn" onclick="removeItem(this)">×</button>
                </div>
                <div class="order-item">
                    <img src="https://cdn.pixabay.com/photo/2023/11/29/12/29/cartoon-8419487_640.jpg" alt="Children"/>
                    <div class="item-details">
                        <p>Children</p>
                        <div class="quantity-selector">
                            <button type="button" class="quantity-btn" onclick="decreaseQuantity(this)">-</button>
                            <input type="text" class="quantity-input" value="2" readonly/>
                            <button type="button" class="quantity-btn" onclick="increaseQuantity(this)">+</button>
                        </div>
                    </div>
                    <p class="item-price">₹10.00</p>
                    <button type="button" class="remove-item-btn" onclick="removeItem(this)">×</button>
                </div>
            </div>

            <div class="billing-summary-section">
                <h2>Billing Summary</h2>
                <div class="summary-item">
                    <p>Subtotal</p>
                    <p>₹55.00</p>
                </div>
                <div class="summary-item">
                    <p>Camera</p>
                    <p>₹50.00</p>
                </div>
                <div class="summary-item">
                    <p>Parking</p>
                    <p>₹50.00</p>
                </div>
                <div class="summary-item">
                    <p>Tax</p>
                    <p>₹7.50</p>
                </div>
                <div class="summary-item">
                    <p>Discount</p>
                    <p>-₹0.00</p>
                </div>
                <div class="summary-item grand-total">
                    <p>Grand Total</p>
                    <p>₹162.50</p>
                </div>
                <p class="inclusive-note">(Inclusive of all Tax)</p>
                <div class="terms-policy">
                    <input type="checkbox" id="terms-policy"/>
                    <label for="terms-policy">Please check to acknowledge our <a href="#">Privacy & Terms Policy</a></label><br/><br/><br/>
                    <div id="terms-policy-error" class="error-message"></div>
                </div>
                <button class = 'pay-btn' onClick={handleClick}>Pay ₹162.50</button>

            </div>
        </form>
        <br/>
        <br/>
        <br/>
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
}

export default Payment;