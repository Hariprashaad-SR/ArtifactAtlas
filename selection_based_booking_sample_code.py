import streamlit as st
from PIL import Image
def translate(text, lang):
    translations = {
        "English": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "Welcome to our Ticket Buddy Bot Selection Based booking service",
            "Choose Your Language": "Choose Your Language",
            "Are you looking to book a museum ticket?": "Are you looking to book a museum ticket?",
            "Yes": "Yes",
            "No": "No",
            "Select a museum:": "Select a museum:",
            "You have selected": "You have selected",
            "Number of adult tickets (₹15 each):": "Number of adult tickets (₹15 each):",
            "Adult Ticket Count is Completed": "Adult Ticket Count is Completed",
            "You need": "You need",
            "number of Adult Tickets": "number of Adult Tickets",
            "Number of children tickets (₹5 each):": "Number of children tickets (₹5 each):",
            "Child Ticket Count is Completed": "Child Ticket Count is Completed",
            "number of Child Tickets": "number of Child Tickets",
            "Is there any foreign visitor?": "Is there any foreign visitor?",
            "Upload ID proof (for foreign visitors):": "Upload ID proof (for foreign visitors):",
            "Uploaded ID Proof": "Uploaded ID Proof",
            "ID proof recognized successfully.": "ID proof recognized successfully.",
            "Please Upload the Id proof": "Please Upload the Id proof",
            "No foreign visitors": "No foreign visitors",
            "Are you looking to take photos and videos in the museum?": "Are you looking to take photos and videos in the museum?",
            "You are going to take photos and videos": "You are going to take photos and videos",
            "Not Needed": "Not Needed",
            "Is parking required?": "Is parking required?",
            "Yes we need parking facility": "Yes we need parking facility",
            "Not needed any parking facility": "Not needed any parking facility",
            "Total bill amount": "Total bill amount",
            "Are you willing to process the payment?": "Are you willing to process the payment?",
            "Proceeding to payment gateway...": "Proceeding to payment gateway...",
            "Booking not completed.": "Booking not completed.",
            "Thank you for visiting! Please reach out when you're ready to book.": "Thank you for visiting! Please reach out when you're ready to book."
        },
        "हिंदी": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "हमारी टिकट बडी बॉट चयन आधारित बुकिंग सेवा में आपका स्वागत है",
            "Choose Your Language": "अपनी भाषा चुनें",
            "Are you looking to book a museum ticket?": "क्या आप संग्रहालय का टिकट बुक करना चाहते हैं?",
            "Yes": "हाँ",
            "No": "नहीं",
            "Select a museum:": "एक संग्रहालय चुनें:",
            "You have selected": "आपने चुना है",
            "Number of adult tickets (₹15 each):": "वयस्क टिकटों की संख्या (₹15 प्रत्येक):",
            "Adult Ticket Count is Completed": "वयस्क टिकट गिनती पूरी हो गई है",
            "You need": "आपको चाहिए",
            "number of Adult Tickets": "वयस्क टिकटों की संख्या",
            "Number of children tickets (₹5 each):": "बच्चों के टिकटों की संख्या (₹5 प्रत्येक):",
            "Child Ticket Count is Completed": "बच्चों के टिकट की गिनती पूरी हो गई है",
            "number of Child Tickets": "बच्चों के टिकटों की संख्या",
            "Is there any foreign visitor?": "क्या कोई विदेशी आगंतुक है?",
            "Upload ID proof (for foreign visitors):": "आईडी प्रमाण अपलोड करें (विदेशी आगंतुकों के लिए):",
            "Uploaded ID Proof": "अपलोड किया गया आईडी प्रमाण",
            "ID proof recognized successfully.": "आईडी प्रमाण सफलतापूर्वक मान्यता प्राप्त है।",
            "Please Upload the Id proof": "कृपया आईडी प्रमाण अपलोड करें",
            "No foreign visitors": "कोई विदेशी आगंतुक नहीं",
            "Are you looking to take photos and videos in the museum?": "क्या आप संग्रहालय में फोटो और वीडियो लेना चाहते हैं?",
            "You are going to take photos and videos": "आप फोटो और वीडियो लेने वाले हैं",
            "Not Needed": "ज़रूरत नहीं",
            "Is parking required?": "क्या पार्किंग की आवश्यकता है?",
            "Yes we need parking facility": "हाँ हमें पार्किंग की सुविधा चाहिए",
            "Not needed any parking facility": "कोई पार्किंग सुविधा की आवश्यकता नहीं",
            "Total bill amount": "कुल बिल राशि",
            "Are you willing to process the payment?": "क्या आप भुगतान प्रक्रिया के लिए तैयार हैं?",
            "Proceeding to payment gateway...": "भुगतान गेटवे पर जा रहे हैं...",
            "Booking not completed.": "बुकिंग पूरी नहीं हुई।",
            "Thank you for visiting! Please reach out when you're ready to book.": "आपके आने के लिए धन्यवाद! कृपया बुक करने के लिए तैयार होने पर संपर्क करें।"
        },
        "ગુજરાતી": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "અમારી ટિકિટ બડી બોટ પસંદગી આધારિત બુકિંગ સેવા માં આપનું સ્વાગત છે",
            "Choose Your Language": "તમારી ભાષા પસંદ કરો",
            "Are you looking to book a museum ticket?": "શું તમે મ્યુઝિયમ ટિકિટ બુક કરવા માંગો છો?",
            "Yes": "હા",
            "No": "ના",
            "Select a museum:": "મ્યુઝિયમ પસંદ કરો:",
            "You have selected": "તમે પસંદ કર્યું છે",
            "Number of adult tickets (₹15 each):": "મોટેકો ટિકિટોની સંખ્યા (₹15 દર પીસ):",
            "Adult Ticket Count is Completed": "મોટેકો ટિકિટોની ગણતરી પૂર્ણ થઈ",
            "You need": "તમને જોઈએ છે",
            "number of Adult Tickets": "મોટેકો ટિકિટોની સંખ્યા",
            "Number of children tickets (₹5 each):": "બાળક ટિકિટોની સંખ્યા (₹5 દર પીસ):",
            "Child Ticket Count is Completed": "બાળક ટિકિટોની ગણતરી પૂર્ણ થઈ",
            "number of Child Tickets": "બાળક ટિકિટોની સંખ્યા",
            "Is there any foreign visitor?": "શું કોઈ વિદેશી મુલાકાતી છે?",
            "Upload ID proof (for foreign visitors):": "આઈડી પુરાવો અપલોડ કરો (વિદેશી મુલાકાતીઓ માટે):",
            "Uploaded ID Proof": "અપલોડ થયેલ આઈડી પુરાવો",
            "ID proof recognized successfully.": "આઈડી પુરાવાની સફળતાપૂર્વક ઓળખાણ થઈ.",
            "Please Upload the Id proof": "કૃપા કરી આઈડી પુરાવો અપલોડ કરો",
            "No foreign visitors": "કોઈ વિદેશી મુલાકાતી નથી",
            "Are you looking to take photos and videos in the museum?": "શું તમે મ્યુઝિયમમાં ફોટો અને વીડિયો લેવાના છો?",
            "You are going to take photos and videos": "તમે ફોટો અને વીડિયો લેવાના છો",
            "Not Needed": "જરૂર નથી",
            "Is parking required?": "શું પાર્કિંગની જરૂર છે?",
            "Yes we need parking facility": "હા, અમને પાર્કિંગ સુવિધા જોઈએ છે",
            "Not needed any parking facility": "કોઈ પાર્કિંગ સુવિધાની જરૂર નથી",
            "Total bill amount": "કુલ બિલ રકમ",
            "Are you willing to process the payment?": "શું તમે ચૂકવણી પ્રક્રિયા કરવા માંગો છો?",
            "Proceeding to payment gateway...": "ચૂકવણી ગેટવે પર જઈ રહ્યા છે...",
            "Booking not completed.": "બુકિંગ પૂર્ણ થયું નથી.",
            "Thank you for visiting! Please reach out when you're ready to book.": "મુલાકાત માટે આભાર! કૃપા કરીને બુકિંગ માટે તૈયાર થો ત્યારે સંપર્ક કરો."
        },
        "தமிழ்": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "எங்கள் டிக்கெட் படி போட் தேர்வு அடிப்படையிலான முன்பதிவு சேவைக்கு வருக",
            "Choose Your Language": "உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்",
            "Are you looking to book a museum ticket?": "நீங்கள் ஒரு அருங்காட்சியக டிக்கெட் முன்பதிவு செய்ய விரும்புகிறீர்களா?",
            "Yes": "ஆம்",
            "No": "இல்லை",
            "Select a museum:": "ஒரு அருங்காட்சியகத்தைத் தேர்ந்தெடுக்கவும்:",
            "You have selected": "நீங்கள் தேர்வு செய்துள்ளீர்கள்",
            "Number of adult tickets (₹15 each):": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை (₹15 ஒவ்வொன்றும்):",
            "Adult Ticket Count is Completed": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை முடிந்தது",
            "You need": "உங்களுக்கு தேவை",
            "number of Adult Tickets": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை",
            "Number of children tickets (₹5 each):": "குழந்தை டிக்கெட் எண்ணிக்கை (₹5 ஒவ்வொன்றும்):",
            "Child Ticket Count is Completed": "குழந்தை டிக்கெட் எண்ணிக்கை முடிந்தது",
            "number of Child Tickets": "குழந்தை டிக்கெட் எண்ணிக்கை",
            "Is there any foreign visitor?": "எந்த வெளிநாட்டு பயணி உள்ளதா?",
            "Upload ID proof (for foreign visitors):": "ID ஆதாரம் பதிவேற்றவும் (வெளிநாட்டு பயணிகள்):",
            "Uploaded ID Proof": "ID ஆதாரம் பதிவேற்றப்பட்டது",
            "ID proof recognized successfully.": "ID ஆதாரம் வெற்றிகரமாக அடையாளம் காணப்பட்டது.",
            "Please Upload the Id proof": "ID ஆதாரத்தை பதிவேற்றவும்",
            "No foreign visitors": "வெளிநாட்டு பயணிகள் இல்லை",
            "Are you looking to take photos and videos in the museum?": "நீங்கள் அருங்காட்சியகத்தில் புகைப்படங்கள் மற்றும் வீடியோக்களை எடுக்க விரும்புகிறீர்களா?",
            "You are going to take photos and videos": "நீங்கள் புகைப்படங்கள் மற்றும் வீடியோக்களை எடுக்க இருக்கிறீர்கள்",
            "Not Needed": "தேவையில்லை",
            "Is parking required?": "பார்கிங் தேவைப்படுகிறதா?",
            "Yes we need parking facility": "ஆம், நாங்கள் பார்கிங் வசதி வேண்டும்",
            "Not needed any parking facility": "எந்த பார்கிங் வசதியும் தேவையில்லை",
            "Total bill amount": "மொத்த பில் தொகை",
            "Are you willing to process the payment?": "நீங்கள் கட்டணம் செலுத்த தயாராக இருக்கிறீர்களா?",
            "Proceeding to payment gateway...": "கட்டண கேட்வேக்கு செல்கிறது...",
            "Booking not completed.": "முன்பதிவு முடிந்தது இல்லை.",
            "Thank you for visiting! Please reach out when you're ready to book.": "வருகைக்கு நன்றி! முன்பதிவுக்கு தயாரான போது தயவுசெய்து அணுகவும்."
        },
        "తెలుగు": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "మా టిక్కెట్ బడి బోట్ ఎంపిక ఆధారిత బుకింగ్ సేవకు స్వాగతం",
            "Choose Your Language": "మీ భాషను ఎంచుకోండి",
            "Are you looking to book a museum ticket?": "మీరు మ్యూజియం టికెట్ బుక్ చేయాలనుకుంటున్నారా?",
            "Yes": "అవును",
            "No": "లేదు",
            "Select a museum:": "ఒక మ్యూజియం ఎంచుకోండి:",
            "You have selected": "మీరు ఎంచుకున్నారు",
            "Number of adult tickets (₹15 each):": "వయోజన టిక్కెట్ల సంఖ్య (₹15 ఒక్కొక్కటికి):",
            "Adult Ticket Count is Completed": "వయోజన టిక్కెట్ల సంఖ్య పూర్తయింది",
            "You need": "మీకు అవసరం",
            "number of Adult Tickets": "వయోజన టిక్కెట్ల సంఖ్య",
            "Number of children tickets (₹5 each):": "పిల్లల టిక్కెట్ల సంఖ్య (₹5 ఒక్కొక్కటికి):",
            "Child Ticket Count is Completed": "పిల్లల టిక్కెట్ల సంఖ్య పూర్తయింది",
            "number of Child Tickets": "పిల్లల టిక్కెట్ల సంఖ్య",
            "Is there any foreign visitor?": "ఏదైనా విదేశీ సందర్శకుడు ఉన్నాడా?",
            "Upload ID proof (for foreign visitors):": "ID రుజువు అప్లోడ్ చేయండి (విదేశీ సందర్శకుల కోసం):",
            "Uploaded ID Proof": "ID రుజువు అప్లోడ్ చేయబడింది",
            "ID proof recognized successfully.": "ID రుజువు విజయవంతంగా గుర్తించబడింది.",
            "Please Upload the Id proof": "దయచేసి ID రుజువు అప్లోడ్ చేయండి",
            "No foreign visitors": "ఏ విదేశీ సందర్శకుడు లేడు",
            "Are you looking to take photos and videos in the museum?": "మీరు మ్యూజియంలో ఫోటోలు మరియు వీడియోలను తీసుకోవాలనుకుంటున్నారా?",
            "You are going to take photos and videos": "మీరు ఫోటోలు మరియు వీడియోలను తీసుకోబోతున్నారు",
            "Not Needed": "అవసరం లేదు",
            "Is parking required?": "పార్కింగ్ అవసరమా?",
            "Yes we need parking facility": "అవును, మాకు పార్కింగ్ సదుపాయం కావాలి",
            "Not needed any parking facility": "ఏ పార్కింగ్ సదుపాయం అవసరం లేదు",
            "Total bill amount": "మొత్తం బిల్లు మొత్తం",
            "Are you willing to process the payment?": "మీరు చెల్లింపు ప్రక్రియ చేయడానికి సిద్ధంగా ఉన్నారా?",
            "Proceeding to payment gateway...": "చెల్లింపు గేట్‌వేకు వెళ్ళుతుంది...",
            "Booking not completed.": "బుకింగ్ పూర్తికాలేదు.",
            "Thank you for visiting! Please reach out when you're ready to book.": "మీ సందర్శనకు ధన్యవాదాలు! మీరు బుక్ చేయడానికి సిద్ధంగా ఉన్నప్పుడు దయచేసి సంప్రదించండి."
        }
    }
    if lang in translations and text in translations[lang]:
        return translations[lang][text]
    else:
        return text  


# List of museums from the given Wikipedia link (you can refine this list as needed)
museum_list = ["---", "National Museum, Delhi", "Indian Museum, Kolkata", "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai", "Salar Jung Museum, Hyderabad", "Government Museum, Chennai", "Albert Hall Museum, Jaipur"]

def main():
    lang="English"
    st.subheader(translate("Welcome to our Ticket Buddy Bot Selection Based booking service",lang))
    lang=st.selectbox("Choose Your Language",("---","আছা","English","ગુજરાતી","हिंदी","ಕನ್ನಡ","کشمیٖری","മലയാളം","मराठी","नेपाली","ਪੰਜਾਬੀ","سنڌي","தமிழ்","తెలుగు","اردو"))
    if lang!="---":
        st.info(f"BOT: {translate('You Preferred ',lang)}"+lang)
        booking_option = st.selectbox(translate("Are you looking to book a museum ticket?",lang), ["---", translate("Yes",lang),translate("No",lang)])
        if booking_option == translate("Yes",lang):
            st.info(f"BOT: {translate('Continue the next Steps to get your tickets',lang)}")
            museum = st.selectbox(translate("Select a museum:",lang), museum_list)
            if museum != "---":
                st.info(f"BOT: {translate('You have selected ',lang)}"+museum)
                adult_tickets = st.number_input(translate("Number of adult tickets (₹15 each):",lang), min_value=0, step=1)
                adult_bill = adult_tickets * 15
                adultbutton=st.checkbox(translate("Adult Ticket Count is Completed",lang))
                if adultbutton==True:
                    st.success(f"BOT: {translate('You need',lang)}"+" "+str(adult_tickets)+" "+f"{translate('number of Adult Tickets',lang)}")
                    child_tickets = st.number_input(translate("Number of children tickets (₹5 each):",lang), min_value=0, step=1)
                    child_bill = child_tickets * 5
                    childbutton=st.checkbox(translate("Child Ticket Count is Completed",lang))
                    if childbutton==True:
                        st.success(f"BOT: {translate('You need',lang)}"+" "+str(child_tickets)+" "+f"{translate('number of Child Tickets',lang)}")
                        total_bill = adult_bill + child_bill
                        foreign_visitor = st.selectbox(translate("Is there any foreign visitor?",lang), ["---", translate("Yes",lang),translate("No",lang)])
                        if foreign_visitor == translate("Yes",lang):
                            foreign_id = st.file_uploader(translate("Upload ID proof (for foreign visitors):",lang), type=["jpg", "jpeg", "png"])
                            if foreign_id is not None:
                                img = Image.open(foreign_id)
                                st.image(img, caption=translate("Uploaded ID Proof",lang), use_column_width=True)
                                st.success(f"BOT: {translate('ID proof recognized successfully.',lang)}")
                                photo_video = st.selectbox(translate("Are you looking to take photos and videos in the museum?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                if photo_video == translate("Yes",lang):
                                    st.info(f"BOT: "+photo_video+f"{translate('we are going to take photos and videos',lang)}")
                                    total_bill += 50
                                    parking = st.selectbox(translate("Is parking required?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if parking == translate("Yes",lang):
                                        st.info("BOT: {translate('Yes we need parking facility',lang)}")
                                        total_bill += 50
                                        payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                        if payment == translate("Yes",lang):
                                            st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                        elif payment==translate("No",lang):
                                            st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                                    elif parking==translate("No",lang):
                                        st.info(f"BOT: {translate('Not needed any parking facility',lang)}")
                                        payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                        if payment == translate("Yes",lang):
                                            st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                        elif payment==translate("No",lang):
                                            st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                                elif photo_video==translate("No",lang):
                                    st.info(f"BOT: {translate('Not Needed',lang)}")
                                    parking = st.selectbox(translate("Is parking required?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if parking == translate("Yes",lang):
                                        st.info("BOT: {translate('Yes we need parking facility',lang)}")
                                        total_bill += 50
                                        payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                        if payment == translate("Yes",lang):
                                            st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                        elif payment==translate("No",lang):
                                            st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                                    elif parking==translate("No",lang):
                                        st.info(f"BOT: {translate('Not needed any parking facility',lang)}")
                                        payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                        if payment == translate("Yes",lang):
                                            st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                        elif payment==translate("No",lang):
                                            st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                            else:
                                st.text(translate("Please Upload the Id proof",lang))   
                        elif foreign_visitor==translate("No",lang):
                            st.info("BOT: "+foreign_visitor+" "+f"{translate('Foreigns',lang)}")
                            photo_video = st.selectbox(translate("Are you looking to take photos and videos in the museum?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                            if photo_video == translate("Yes",lang):
                                st.info("BOT: "+photo_video+" "+f"{translate('we are going to take photos and videos',lang)}")
                                total_bill += 50
                                parking = st.selectbox(translate("Is parking required?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                if parking == translate("Yes",lang):
                                    st.info(f"BOT: {translate('Yes we need parking facility',lang)}")
                                    total_bill += 50
                                    payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if payment == translate("Yes",lang):
                                        st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                    elif payment==translate("No",lang):
                                        st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                                elif parking==translate("No",lang):
                                    st.info(f"BOT: {translate('Not needed any parking facility',lang)}")
                                    payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if payment == translate("Yes",lang):
                                        st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                    elif payment==translate("No",lang):
                                        st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                            elif photo_video==translate("No",lang):
                                st.info(f"BOT: {translate('Not Needed',lang)}")
                                parking = st.selectbox(translate("Is parking required?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                if parking == translate("Yes",lang):
                                    st.info(f"BOT: {translate('Yes we need parking facility',lang)}")
                                    total_bill += 50
                                    payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if payment == translate("Yes",lang):
                                        st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                    elif payment==translate("No",lang):
                                        st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                                elif parking==translate("No",lang):
                                    st.info(f"BOT: {translate('Not needed any parking facility',lang)}")
                                    payment = st.selectbox(translate("Are you willing to process the payment?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                                    if payment == translate("Yes",lang):
                                        st.success(f"BOT: {translate('Proceeding to payment gateway...',lang)}")
                                    elif payment==translate("No",lang):
                                        st.warning(f"BOT: {translate('Booking not completed.',lang)}")
                        st.info(f"BOT: "+f"{translate('Total bill amount:',lang)}"+" ₹"+f"{total_bill}")
        elif booking_option == translate("No",lang):
            st.info(f"BOT: {translate('Thank you for visiting! Please reach out when you are ready to book.',lang)}")

if __name__ == "__main__":
    main()
