import streamlit as st
from PIL import Image


# List of museums from the given Wikipedia link (you can refine this list as needed)
museum_list = ["--select--", "National Museum, Delhi", "Indian Museum, Kolkata", "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai", "Salar Jung Museum, Hyderabad", "Government Museum, Chennai", "Albert Hall Museum, Jaipur"]

def main():
    # Initial UI for booking inquiry
    st.subheader("Welcome to our Ticket Buddy Bot Selection Based booking service")
    lang=st.selectbox("Choose Your Language",("--select--","আছা","English","ગુજરાતી","हिंदी","ಕನ್ನಡ","کشمیٖری","മലയാളം","मराठी","नेपाली","ਪੰਜਾਬੀ","سنڌي","தமிழ்","తెలుగు","اردو"))
    if lang!="--select--":
        st.info(f"BOT: You Preferred {lang}.")
        booking_option = st.selectbox("Are you looking to book a museum ticket?", ["--select--", "Yes", "No"])
        if booking_option == "Yes":
            st.info("BOT: Continue the next Steps to get your tickets")
            museum = st.selectbox("Select a museum:", museum_list)
            if museum != "--select--":
                st.info(f"BOT: You have selected {museum}.")
                adult_tickets = st.number_input("Number of adult tickets (₹15 each):", min_value=0, step=1)
                adult_bill = adult_tickets * 15
                adultbutton=st.checkbox("Adult Ticket Count is Completed")
                if adultbutton==True:
                    st.success(f"BOT: You need {adult_tickets} number of Adult Tickets")
                    child_tickets = st.number_input("Number of children tickets (₹5 each):", min_value=0, step=1)
                    child_bill = child_tickets * 5
                    childbutton=st.checkbox("Child Ticket Count is Completed")
                    if childbutton==True:
                        st.success(f"BOT: You need {child_tickets} number of Child Tickets")
                        total_bill = adult_bill + child_bill
                        foreign_visitor = st.selectbox("Is there any foreign visitor?", ["--select--", "Yes", "No"])
                        if foreign_visitor == "Yes":
                            foreign_id = st.file_uploader("Upload ID proof (for foreign visitors):", type=["jpg", "jpeg", "png"])
                            if foreign_id is not None:
                                img = Image.open(foreign_id)
                                st.image(img, caption="Uploaded ID Proof", use_column_width=True)
                                st.success("BOT: ID proof recognized successfully.")
                                photo_video = st.selectbox("Are you looking to take photos and videos in the museum?", ["--select--", "Yes", "No"])
                                if photo_video == "Yes":
                                    st.info("BOT: "+photo_video+" we are going to take photos and videos")
                                    total_bill += 50
                                    parking = st.selectbox("Is parking required?", ["--select--", "Yes", "No"])
                                    if parking == "Yes":
                                        st.info("BOT: Yes we need parking facility")
                                        total_bill += 50
                                        payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                        if payment == "Yes":
                                            st.success("BOT: Proceeding to payment gateway...")
                                        elif payment=="No":
                                            st.warning("BOT: Booking not completed.")
                                    elif parking=="No":
                                        st.info("BOT: Not needed any parking facility")
                                        payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                        if payment == "Yes":
                                            st.success("BOT: Proceeding to payment gateway...")
                                        elif payment=="No":
                                            st.warning("BOT: Booking not completed.")
                                elif photo_video=="No":
                                    st.info("BOT: Not Needed")
                                    parking = st.selectbox("Is parking required?", ["--select--", "Yes", "No"])
                                    if parking == "Yes":
                                        st.info("BOT: Yes we need parking facility")
                                        total_bill += 50
                                        payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                        if payment == "Yes":
                                            st.success("BOT: Proceeding to payment gateway...")
                                        elif payment=="No":
                                            st.warning("BOT: Booking not completed.")
                                    elif parking=="No":
                                        st.info("BOT: Not needed any parking facility")
                                        payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                        if payment == "Yes":
                                            st.success("BOT: Proceeding to payment gateway...")
                                        elif payment=="No":
                                            st.warning("BOT: Booking not completed.")
                            else:
                                st.text("Please Upload the Id proof")   
                        elif foreign_visitor=="No":
                            st.info("BOT: "+foreign_visitor+" Foreigns")
                            photo_video = st.selectbox("Are you looking to take photos and videos in the museum?", ["--select--", "Yes", "No"])
                            if photo_video == "Yes":
                                st.info("BOT: "+photo_video+" we are going to take photos and videos")
                                total_bill += 50
                                parking = st.selectbox("Is parking required?", ["--select--", "Yes", "No"])
                                if parking == "Yes":
                                    st.info("BOT: Yes we need parking facility")
                                    total_bill += 50
                                    payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                    if payment == "Yes":
                                        st.success("BOT: Proceeding to payment gateway...")
                                    elif payment=="No":
                                        st.warning("BOT: Booking not completed.")
                                elif parking=="No":
                                    st.info("BOT: Not needed any parking facility")
                                    payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                    if payment == "Yes":
                                        st.success("BOT: Proceeding to payment gateway...")
                                    elif payment=="No":
                                        st.warning("BOT: Booking not completed.")
                            elif photo_video=="No":
                                st.info("BOT: Not Needed")
                                parking = st.selectbox("Is parking required?", ["--select--", "Yes", "No"])
                                if parking == "Yes":
                                    st.info("BOT: Yes we need parking facility")
                                    total_bill += 50
                                    payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                    if payment == "Yes":
                                        st.success("BOT: Proceeding to payment gateway...")
                                    elif payment=="No":
                                        st.warning("BOT: Booking not completed.")
                                elif parking=="No":
                                    st.info("BOT: Not needed any parking facility")
                                    payment = st.selectbox("Are you willing to process the payment?", ["--select--", "Yes", "No"])
                                    if payment == "Yes":
                                        st.success("BOT: Proceeding to payment gateway...")
                                    elif payment=="No":
                                        st.warning("BOT: Booking not completed.")
                        st.info(f"BOT: Total bill amount: ₹{total_bill}")
        elif booking_option == "No":
            st.info("BOT: Thank you for visiting! Please reach out when you're ready to book.")

if __name__ == "__main__":
    main()
