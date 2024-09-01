import streamlit as st
from PIL import Image
def translate(text, lang):
    translations = {
    "française": { # french language
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "Bienvenue sur notre service de réservation basé sur la sélection de Ticket Buddy Bot",
        "Choose Your Language": "Choisissez votre langue",
        "Are you looking to book a museum ticket?": "Cherchez-vous à réserver un billet pour un musée?",
        "Yes": "Oui",
        "No": "Non",
        "Continue the next Steps to get your tickets": "Continuez les étapes suivantes pour obtenir vos billets",
        "You Preferred ": "Vous avez préféré ",
        "Select a museum:": "Sélectionnez un musée:",
        "You have selected": "Vous avez sélectionné",
        "Number of adult tickets (₹15 each):": "Nombre de billets adultes (₹15 chacun):",
        "Adult Ticket Count is Completed": "Le décompte des billets adultes est terminé",
        "You need": "Vous avez besoin de",
        "number of Adult Tickets": "billets adultes",
        "Number of children tickets (₹5 each):": "Nombre de billets pour enfants (₹5 chacun):",
        "Child Ticket Count is Completed": "Le décompte des billets pour enfants est terminé",
        "number of Child Tickets": "billets pour enfants",
        "Is there any foreign visitor?": "Y a-t-il des visiteurs étrangers?",
        "Upload ID proof (for foreign visitors):": "Téléchargez une pièce d'identité (pour les visiteurs étrangers):",
        "Uploaded ID Proof": "Pièce d'identité téléchargée",
        "ID proof recognized successfully.": "Pièce d'identité reconnue avec succès.",
        "Please Upload the Id proof": "Veuillez télécharger la pièce d'identité",
        "No foreign visitors": "Pas de visiteurs étrangers",
        "Are you looking to take photos and videos in the museum?": "Souhaitez-vous prendre des photos et des vidéos dans le musée?",
        "You are going to take photos and videos": "Vous allez prendre des photos et des vidéos",
        "Not Needed": "Pas nécessaire",
        "Is parking required?": "Le stationnement est-il nécessaire?",
        "Yes we need parking facility": "Oui, nous avons besoin d'une installation de stationnement",
        "Not needed any parking facility": "Pas besoin d'une installation de stationnement",
        "Total bill amount": "Montant total de la facture",
        "Are you willing to process the payment?": "Êtes-vous prêt à procéder au paiement?",
        "Proceeding to payment gateway...": "Accès au portail de paiement en cours...",
        "Booking not completed.": "Réservation non terminée.",
        "Thank you for visiting! Please reach out when you are ready to book.": "Merci de votre visite ! N'hésitez pas à revenir lorsque vous êtes prêt à réserver."
    },
    "española": { #spanish
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "Bienvenido a nuestro servicio de reserva basado en la selección de Ticket Buddy Bot",
        "Choose Your Language": "Elija su idioma",
        "Are you looking to book a museum ticket?": "¿Está buscando reservar un boleto para un museo?",
        "Yes": "Sí",
        "No": "No",
        "Continue the next Steps to get your tickets": "Continúe con los siguientes pasos para obtener sus boletos",
        "You Preferred ": "Usted prefirió ",
        "Select a museum:": "Seleccione un museo:",
        "You have selected": "Ha seleccionado",
        "Number of adult tickets (₹15 each):": "Número de boletos para adultos (₹15 cada uno):",
        "Adult Ticket Count is Completed": "El conteo de boletos para adultos está completado",
        "You need": "Necesita",
        "number of Adult Tickets": "número de boletos para adultos",
        "Number of children tickets (₹5 each):": "Número de boletos para niños (₹5 cada uno):",
        "Child Ticket Count is Completed": "El conteo de boletos para niños está completado",
        "number of Child Tickets": "número de boletos para niños",
        "Is there any foreign visitor?": "¿Hay algún visitante extranjero?",
        "Upload ID proof (for foreign visitors):": "Suba prueba de identificación (para visitantes extranjeros):",
        "Uploaded ID Proof": "Prueba de identificación subida",
        "ID proof recognized successfully.": "Prueba de identificación reconocida con éxito.",
        "Please Upload the Id proof": "Por favor, suba la prueba de identificación",
        "No foreign visitors": "No hay visitantes extranjeros",
        "Are you looking to take photos and videos in the museum?": "¿Está buscando tomar fotos y videos en el museo?",
        "You are going to take photos and videos": "Va a tomar fotos y videos",
        "Not Needed": "No es necesario",
        "Is parking required?": "¿Se requiere estacionamiento?",
        "Yes we need parking facility": "Sí, necesitamos instalación de estacionamiento",
        "Not needed any parking facility": "No se necesita ninguna instalación de estacionamiento",
        "Total bill amount": "Monto total de la factura",
        "Are you willing to process the payment?": "¿Está dispuesto a procesar el pago?",
        "Proceeding to payment gateway...": "Procediendo al portal de pago...",
        "Booking not completed.": "Reserva no completada.",
        "Thank you for visiting! Please reach out when you are ready to book.": "Gracias por su visita! No dude en volver cuando esté listo para reservar."
    },
    "Русский": { #Russian
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "Добро пожаловать в наш сервис бронирования на основе выбора Ticket Buddy Bot",
        "Choose Your Language": "Выберите ваш язык",
        "Are you looking to book a museum ticket?": "Вы хотите забронировать билет в музей?",
        "Yes": "Да",
        "No": "Нет",
        "Continue the next Steps to get your tickets": "Продолжайте следующие шаги, чтобы получить свои билеты",
        "You Preferred ": "Вы выбрали ",
        "Select a museum:": "Выберите музей:",
        "You have selected": "Вы выбрали",
        "Number of adult tickets (₹15 each):": "Количество билетов для взрослых (₹15 за каждый):",
        "Adult Ticket Count is Completed": "Подсчет билетов для взрослых завершен",
        "You need": "Вам нужно",
        "number of Adult Tickets": "количество билетов для взрослых",
        "Number of children tickets (₹5 each):": "Количество билетов для детей (₹5 за каждый):",
        "Child Ticket Count is Completed": "Подсчет билетов для детей завершен",
        "number of Child Tickets": "количество билетов для детей",
        "Is there any foreign visitor?": "Есть ли иностранный посетитель?",
        "Upload ID proof (for foreign visitors):": "Загрузите удостоверение личности (для иностранных посетителей):",
        "Uploaded ID Proof": "Загруженное удостоверение личности",
        "ID proof recognized successfully.": "Удостоверение личности успешно распознано.",
        "Please Upload the Id proof": "Пожалуйста, загрузите удостоверение личности",
        "No foreign visitors": "Нет иностранных посетителей",
        "Are you looking to take photos and videos in the museum?": "Вы хотите делать фото и видео в музее?",
        "You are going to take photos and videos": "Вы собираетесь делать фото и видео",
        "Not Needed": "Не нужно",
        "Is parking required?": "Требуется ли парковка?",
        "Yes we need parking facility": "Да, нам нужна парковка",
        "Not needed any parking facility": "Парковка не требуется",
        "Total bill amount": "Общая сумма счета",
        "Are you willing to process the payment?": "Вы готовы совершить оплату?",
        "Proceeding to payment gateway...": "Переход к платежному шлюзу...",
        "Booking not completed.": "Бронирование не завершено.",
        "Thank you for visiting! Please reach out when you are ready to book.": "Спасибо за посещение! Возвращайтесь, когда будете готовы забронировать."
    },
    "বাংলা": { #Bangla
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "আমাদের টিকেট বাডি বট নির্বাচন ভিত্তিক বুকিং পরিষেবাতে স্বাগতম",
        "Choose Your Language": "আপনার ভাষা নির্বাচন করুন",
        "Are you looking to book a museum ticket?": "আপনি কি মিউজিয়ামের টিকিট বুক করতে চান?",
        "Yes": "হ্যাঁ",
        "No": "না",
        "Continue the next Steps to get your tickets": "আপনার টিকিট পেতে পরবর্তী ধাপগুলি চালিয়ে যান",
        "You Preferred ": "আপনি পছন্দ করেছেন ",
        "Select a museum:": "একটি মিউজিয়াম নির্বাচন করুন:",
        "You have selected": "আপনি নির্বাচন করেছেন",
        "Number of adult tickets (₹15 each):": "প্রাপ্তবয়স্কদের টিকিটের সংখ্যা (₹15 প্রতি):",
        "Adult Ticket Count is Completed": "প্রাপ্তবয়স্কদের টিকিটের গণনা সম্পন্ন হয়েছে",
        "You need": "আপনার প্রয়োজন",
        "number of Adult Tickets": "প্রাপ্তবয়স্কদের টিকিটের সংখ্যা",
        "Number of children tickets (₹5 each):": "শিশুদের টিকিটের সংখ্যা (₹5 প্রতি):",
        "Child Ticket Count is Completed": "শিশুদের টিকিটের গণনা সম্পন্ন হয়েছে",
        "number of Child Tickets": "শিশুদের টিকিটের সংখ্যা",
        "Is there any foreign visitor?": "কোনো বিদেশী দর্শক আছে কি?",
        "Upload ID proof (for foreign visitors):": "আইডি প্রমাণ আপলোড করুন (বিদেশী দর্শকদের জন্য):",
        "Uploaded ID Proof": "আপলোড করা আইডি প্রমাণ",
        "ID proof recognized successfully.": "আইডি প্রমাণ সফলভাবে স্বীকৃত হয়েছে।",
        "Please Upload the Id proof": "অনুগ্রহ করে আইডি প্রমাণ আপলোড করুন",
        "No foreign visitors": "কোনো বিদেশী দর্শক নেই",
        "Are you looking to take photos and videos in the museum?": "আপনি কি মিউজিয়ামে ছবি এবং ভিডিও নিতে চান?",
        "You are going to take photos and videos": "আপনি ছবি এবং ভিডিও নিতে যাচ্ছেন",
        "Not Needed": "প্রয়োজন নেই",
        "Is parking required?": "পার্কিং প্রয়োজন কি?",
        "Yes we need parking facility": "হ্যাঁ, আমাদের পার্কিং সুবিধা প্রয়োজন",
        "Not needed any parking facility": "কোনো পার্কিং সুবিধা প্রয়োজন নেই",
        "Total bill amount": "মোট বিলের পরিমাণ",
        "Are you willing to process the payment?": "আপনি কি পেমেন্ট প্রক্রিয়াকরণ করতে চান?",
        "Proceeding to payment gateway...": "পেমেন্ট গেটওয়েতে এগিয়ে যাওয়া হচ্ছে...",
        "Booking not completed.": "বুকিং সম্পন্ন হয়নি।",
        "Thank you for visiting! Please reach out when you are ready to book.": "ধন্যবাদ আমাদের সফরে আসার জন্য! আপনি যখন বুক করতে প্রস্তুত হবেন তখন ফিরে আসুন।"
    },
    "bahasa Melayu": { #Malay
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "Selamat datang ke perkhidmatan tempahan berasaskan pilihan Ticket Buddy Bot kami",
        "Choose Your Language": "Pilih bahasa anda",
        "Are you looking to book a museum ticket?": "Adakah anda mencari untuk menempah tiket muzium?",
        "Yes": "Ya",
        "No": "Tidak",
        "Continue the next Steps to get your tickets": "Teruskan langkah seterusnya untuk mendapatkan tiket anda",
        "You Preferred ": "Anda memilih ",
        "Select a museum:": "Pilih sebuah muzium:",
        "You have selected": "Anda telah memilih",
        "Number of adult tickets (₹15 each):": "Bilangan tiket dewasa (₹15 setiap satu):",
        "Adult Ticket Count is Completed": "Pengiraan tiket dewasa selesai",
        "You need": "Anda memerlukan",
        "number of Adult Tickets": "bilangan tiket dewasa",
        "Number of children tickets (₹5 each):": "Bilangan tiket kanak-kanak (₹5 setiap satu):",
        "Child Ticket Count is Completed": "Pengiraan tiket kanak-kanak selesai",
        "number of Child Tickets": "bilangan tiket kanak-kanak",
        "Is there any foreign visitor?": "Adakah terdapat pelawat asing?",
        "Upload ID proof (for foreign visitors):": "Muat naik bukti pengenalan (untuk pelawat asing):",
        "Uploaded ID Proof": "Bukti pengenalan yang dimuat naik",
        "ID proof recognized successfully.": "Bukti pengenalan berjaya dikenalpasti.",
        "Please Upload the Id proof": "Sila muat naik bukti pengenalan",
        "No foreign visitors": "Tiada pelawat asing",
        "Are you looking to take photos and videos in the museum?": "Adakah anda ingin mengambil gambar dan video di muzium?",
        "You are going to take photos and videos": "Anda akan mengambil gambar dan video",
        "Not Needed": "Tidak perlu",
        "Is parking required?": "Adakah parkir diperlukan?",
        "Yes we need parking facility": "Ya, kami memerlukan kemudahan parkir",
        "Not needed any parking facility": "Tidak memerlukan sebarang kemudahan parkir",
        "Total bill amount": "Jumlah bil keseluruhan",
        "Are you willing to process the payment?": "Adakah anda bersedia untuk memproses pembayaran?",
        "Proceeding to payment gateway...": "Sedang bergerak ke gerbang pembayaran...",
        "Booking not completed.": "Tempahan tidak selesai.",
        "Thank you for visiting! Please reach out when you are ready to book.": "Terima kasih kerana melawat! Sila kembali apabila anda bersedia untuk menempah."
    },
    "Deutsch": { #German
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "Willkommen bei unserem Ticket Buddy Bot Auswahlbasierten Buchungsservice",
        "Choose Your Language": "Wählen Sie Ihre Sprache",
        "Are you looking to book a museum ticket?": "Möchten Sie ein Museumsticket buchen?",
        "Yes": "Ja",
        "No": "Nein",
        "Continue the next Steps to get your tickets": "Fahren Sie mit den nächsten Schritten fort, um Ihre Tickets zu erhalten",
        "You Preferred ": "Sie bevorzugten ",
        "Select a museum:": "Wählen Sie ein Museum:",
        "You have selected": "Sie haben ausgewählt",
        "Number of adult tickets (₹15 each):": "Anzahl der Erwachsenentickets (₹15 pro Stück):",
        "Adult Ticket Count is Completed": "Die Zählung der Erwachsenentickets ist abgeschlossen",
        "You need": "Sie benötigen",
        "number of Adult Tickets": "Anzahl der Erwachsenentickets",
        "Number of children tickets (₹5 each):": "Anzahl der Kindertickets (₹5 pro Stück):",
        "Child Ticket Count is Completed": "Die Zählung der Kindertickets ist abgeschlossen",
        "number of Child Tickets": "Anzahl der Kindertickets",
        "Is there any foreign visitor?": "Gibt es ausländische Besucher?",
        "Upload ID proof (for foreign visitors):": "Laden Sie einen Identitätsnachweis hoch (für ausländische Besucher):",
        "Uploaded ID Proof": "Hochgeladener Identitätsnachweis",
        "ID proof recognized successfully.": "Identitätsnachweis erfolgreich erkannt.",
        "Please Upload the Id proof": "Bitte laden Sie den Identitätsnachweis hoch",
        "No foreign visitors": "Keine ausländischen Besucher",
        "Are you looking to take photos and videos in the museum?": "Möchten Sie im Museum Fotos und Videos machen?",
        "You are going to take photos and videos": "Sie werden Fotos und Videos machen",
        "Not Needed": "Nicht erforderlich",
        "Is parking required?": "Wird ein Parkplatz benötigt?",
        "Yes we need parking facility": "Ja, wir benötigen eine Parkmöglichkeit",
        "Not needed any parking facility": "Keine Parkmöglichkeit benötigt",
        "Total bill amount": "Gesamtbetrag der Rechnung",
        "Are you willing to process the payment?": "Sind Sie bereit, die Zahlung abzuwickeln?",
        "Proceeding to payment gateway...": "Weiterleitung zum Zahlungsportal...",
        "Booking not completed.": "Buchung nicht abgeschlossen.",
        "Thank you for visiting! Please reach out when you are ready to book.": "Danke für Ihren Besuch! Melden Sie sich gerne, wenn Sie bereit sind zu buchen."
    },
    "සිංහල": { #Sinhala
        "Welcome to our Ticket Buddy Bot Selection Based booking service": "අපගේ ටිකට් බඩි බොට් තේරීම් මත පදනම්වූ සෙව්වා සේවයට පිළිගනිමු",
        "Choose Your Language": "ඔබගේ භාෂාව තෝරන්න",
        "Are you looking to book a museum ticket?": "ඔබ කෞතුකාගාර ප්‍රවේශ පත්‍රයක් වෙන්කර ගැනීමට සොයනවාද?",
        "Yes": "ඔව්",
        "No": "නැත",
        "Continue the next Steps to get your tickets": "ඔබගේ ප්‍රවේශ පත්‍ර ලබා ගැනීමට මීළඟ පියවර ඉදිරියට ගෙන යන්න",
        "You Preferred ": "ඔබ කැමති ",
        "Select a museum:": "කෞතුකාගාරයක් තෝරන්න:",
        "You have selected": "ඔබ තෝරාගෙන ඇත",
        "Number of adult tickets (₹15 each):": "වැඩිහිටි ප්‍රවේශ පත්‍ර ගණන (₹15 යි එක් පත්‍රයකට):",
        "Adult Ticket Count is Completed": "වැඩිහිටි ප්‍රවේශ පත්‍ර ගණන සම්පූර්ණයි",
        "You need": "ඔබට අවශ්‍යයි",
        "number of Adult Tickets": "වැඩිහිටි ප්‍රවේශ පත්‍ර ගණන",
        "Number of children tickets (₹5 each):": "ළමුන්ගේ ප්‍රවේශ පත්‍ර ගණන (₹5 යි එක් පත්‍රයකට):",
        "Child Ticket Count is Completed": "ළමුන්ගේ ප්‍රවේශ පත්‍ර ගණන සම්පූර්ණයි",
        "number of Child Tickets": "ළමුන්ගේ ප්‍රවේශ පත්‍ර ගණන",
        "Is there any foreign visitor?": "විදේශීය සංචාරකයින් කිසිවෙක් ඇත්ද?",
        "Upload ID proof (for foreign visitors):": "හැඳුනුම් පත්‍රය උඩුගත කරන්න (විදේශීය සංචාරකයින් සඳහා):",
        "Uploaded ID Proof": "හැඳුනුම් පත්‍රය සාර්ථකව උඩුගත කරන ලදී",
        "ID proof recognized successfully.": "හැඳුනුම් පත්‍රය සාර්ථකව හඳුනාගන්නා ලදී.",
        "Please Upload the Id proof": "කරුණාකර හැඳුනුම් පත්‍රය උඩුගත කරන්න",
        "No foreign visitors": "විදේශීය සංචාරකයින් නොමැත",
        "Are you looking to take photos and videos in the museum?": "ඔබ කෞතුකාගාරයේ ඡායාරූප සහ වීඩියෝ ගැනීමට බලාපොරොත්තු ද?",
        "You are going to take photos and videos": "ඔබ ඡායාරූප සහ වීඩියෝ ගන්න යනවා",
        "Not Needed": "අවශ්‍ය නොවේ",
        "Is parking required?": "රථගාර පහසුකම් අවශ්‍යද?",
        "Yes we need parking facility": "ඔව්, අපට රථගාර පහසුකම් අවශ්‍යයි",
        "Not needed any parking facility": "රථගාර පහසුකම් අවශ්‍ය නොවේ",
        "Total bill amount": "මුළු බිල්පතේ මුදල",
        "Are you willing to process the payment?": "ඔබ ගෙවීමේ ක්‍රියාවලිය ක්‍රියත්මක කිරීමට කැමතිද?",
        "Proceeding to payment gateway...": "ගෙවීමේ ද්වාරය වෙත ගමන් කරමින් පවතී...",
        "Booking not completed.": "ප්‍රවේශ පත්‍ර වෙන්කරීම සම්පූර්ණ නැත.",
        "Thank you for visiting! Please reach out when you are ready to book.": "අප හා එක්වීම ගැන ස්තූතියි! ඔබට වෙන්කර ගැනීමට සූදානම් වීමේදී කරුණාකර අප අමතන්න."
    },      
        "کشمیری": {  # Kashmiri translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "ٹِکٹ بڈی بَوٹ انتخاب بُنیاد بُکنگ خِدمت چُھ تہَندُک سوگہت",
            "Choose Your Language": "تُیہار زُبان چھیو نندے",
            "Are you looking to book a museum ticket?": "کیا تُیہ موزیم ٹِکٹ بُک کرن ؤنداہو؟",
            "Yes": "ہٕو",
            "No": "نَہ",
            "Continue the next Steps to get your tickets": "ٹِکٹ حاصل کرنے خاطر اگلا اَقدام جاری رکھو",
            "You Preferred ": "تُیہ پَسند کرت ",
            "Select a museum:": "ایک موزیم چھیو نندے:",
            "You have selected": "تُیہار انتخاب چھی",
            "Number of adult tickets (₹15 each):": "بوٚزُر ٹِکٹوَنک عدد (ہرہ زٕ بانہہ ۱۵ روپے):",
            "Adult Ticket Count is Completed": "بوٚزُر ٹِکٹوَنک عدد پوٚر تہِ آمت",
            "You need": "تُیہہ چو ضرورت",
            "number of Adult Tickets": "بوٚزُر ٹِکٹوَنک عدد",
            "Number of children tickets (₹5 each):": "بچے ٹِکٹوَنک عدد (ہرہ زٕ بانہہ ۵ روپے):",
            "Child Ticket Count is Completed": "بچے ٹِکٹوَنک عدد پوٚر تہِ آمت",
            "number of Child Tickets": "بچے ٹِکٹوَنک عدد",
            "Is there any foreign visitor?": "کیا کوئی بٔیہرنک دوراہ ز موجود چھے؟",
            "Upload ID proof (for foreign visitors):": "آئی ڈی سابوت اپلوڈ کرہ (بٔیہرنک دوراہ ز):",
            "Uploaded ID Proof": "آئی ڈی سابوت اپلوڈ کرمژ",
            "ID proof recognized successfully.": "آئی ڈی سابوت کامیابیت ساں پہچان کرمژ.",
            "Please Upload the Id proof": "براہ کرم آئی ڈی سابوت اپلوڈ کرہ",
            "No foreign visitors": "کونہہ بٔیہرنک دوراہ ز موجود چھہ نَہ",
            "Are you looking to take photos and videos in the museum?": "کیا تُیہ موزیمس منز فوٹو تہِ ویڈیو گرہن ؤنداہو؟",
            "You are going to take photos and videos": "تُیہ فوٹو تہِ ویڈیو گرہن گووند",
            "Not Needed": "ضرورت چھہ نَہ",
            "Is parking required?": "کیا پارکنگک ضرورت چھے؟",
            "Yes we need parking facility": "ہٕو، اسیہہ پارکنگ سہولتک ضرورت چھے",
            "Not needed any parking facility": "پارکنگ سہولتک ضرورت چھہ نَہ",
            "Total bill amount": "کل بِل رقم",
            "Are you willing to process the payment?": "کیا تُیہہ ادایگیچ پرکریا کرن ہژمُت چھیو؟",
            "Proceeding to payment gateway...": "ادایگی گیٹوی پًٹھ گٔچھو...",
            "Booking not completed.": "بُکنگ پوٚر نَہ ژمت.",
            "Thank you for visiting! Please reach out when you are ready to book.": "سوگہت کرن کٔتھ پٲنزے شکریہ! براہ کرم تُیہہ بُکنگچ خاطر تیّار ژمنس پٹھہ ہمہ رابطہ کرہ."
        },

        "मराठी": {  # Marathi translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "आमच्या टिकीट बडी बॉट निवड आधारित बुकिंग सेवे मध्ये आपले स्वागत आहे",
            "Choose Your Language": "तुमची भाषा निवडा",
            "Are you looking to book a museum ticket?": "आपण संग्रहालयाचे तिकीट बुक करण्याचा विचार करत आहात का?",
            "Yes": "होय",
            "No": "नाही",
            "Continue the next Steps to get your tickets": "आपले तिकीट मिळवण्यासाठी पुढील पावले चालू ठेवा",
            "You Preferred ": "तुम्ही प्राधान्य दिले ",
            "Select a museum:": "संग्रहालय निवडा:",
            "You have selected": "तुम्ही निवडले आहे",
            "Number of adult tickets (₹15 each):": "प्रौढ तिकीटांची संख्या (प्रत्येक ₹15):",
            "Adult Ticket Count is Completed": "प्रौढ तिकीट संख्या पूर्ण झाली आहे",
            "You need": "तुम्हाला गरज आहे",
            "number of Adult Tickets": "प्रौढ तिकीटांची संख्या",
            "Number of children tickets (₹5 each):": "मुलांच्या तिकीटांची संख्या (प्रत्येक ₹5):",
            "Child Ticket Count is Completed": "मुलांच्या तिकीटांची संख्या पूर्ण झाली आहे",
            "number of Child Tickets": "मुलांच्या तिकीटांची संख्या",
            "Is there any foreign visitor?": "कोणता विदेशी पाहुणा आहे का?",
            "Upload ID proof (for foreign visitors):": "ओळखपत्र अपलोड करा (विदेशी पाहुण्यांसाठी):",
            "Uploaded ID Proof": "ओळखपत्र अपलोड झाले आहे",
            "ID proof recognized successfully.": "ओळखपत्र यशस्वीरित्या ओळखले गेले.",
            "Please Upload the Id proof": "कृपया ओळखपत्र अपलोड करा",
            "No foreign visitors": "कोणतेही विदेशी पाहुणे नाहीत",
            "Are you looking to take photos and videos in the museum?": "तुम्ही संग्रहालयात फोटो आणि व्हिडिओ घेण्याचा विचार करत आहात का?",
            "You are going to take photos and videos": "तुम्ही फोटो आणि व्हिडिओ घेणार आहात",
            "Not Needed": "आवश्यक नाही",
            "Is parking required?": "पार्किंग आवश्यक आहे का?",
            "Yes we need parking facility": "होय, आम्हाला पार्किंगची सुविधा आवश्यक आहे",
            "Not needed any parking facility": "पार्किंगची कोणतीही सुविधा आवश्यक नाही",
            "Total bill amount": "एकूण बिल रक्कम",
            "Are you willing to process the payment?": "तुम्ही पेमेंट प्रक्रिया करण्यास तयार आहात का?",
            "Proceeding to payment gateway...": "पेमेंट गेटवेकडे पुढे जात आहे...",
            "Booking not completed.": "बुकिंग पूर्ण झाले नाही.",
            "Thank you for visiting! Please reach out when you are ready to book.": "भेट दिल्याबद्दल धन्यवाद! कृपया बुकिंगसाठी तयार असताना संपर्क साधा."
        },

        "नेपाली": {  # Nepali translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "हाम्रो टिकट बडी बोट छनोटमा आधारित बुकिंग सेवामा स्वागत छ",
            "Choose Your Language": "आफ्नो भाषा छान्नुहोस्",
            "Are you looking to book a museum ticket?": "के तपाईं संग्राहलयको टिकट बुक गर्न चाहनुहुन्छ?",
            "Yes": "हो",
            "No": "होइन",
            "Continue the next Steps to get your tickets": "तपाईंको टिकट प्राप्त गर्नका लागि अर्को चरणहरू जारी राख्नुहोस्",
            "You Preferred ": "तपाईंले मन पराउनुभयो ",
            "Select a museum:": "संग्राहलय छान्नुहोस्:",
            "You have selected": "तपाईंले चयन गर्नुभएको छ",
            "Number of adult tickets (₹15 each):": "प्रौढ टिकटहरूको संख्या (प्रति टिकट ₹15):",
            "Adult Ticket Count is Completed": "प्रौढ टिकटहरूको गणना पूरा भयो",
            "You need": "तपाईंलाई आवश्यकता छ",
            "number of Adult Tickets": "प्रौढ टिकटहरूको संख्या",
            "Number of children tickets (₹5 each):": "बालबालिकाका टिकटहरूको संख्या (प्रति टिकट ₹5):",
            "Child Ticket Count is Completed": "बालबालिकाका टिकटहरूको गणना पूरा भयो",
            "number of Child Tickets": "बालबालिकाका टिकटहरूको संख्या",
            "Is there any foreign visitor?": "के कुनै विदेशी आगन्तुक छ?",
            "Upload ID proof (for foreign visitors):": "पहिचान प्रमाण अपलोड गर्नुहोस् (विदेशी आगन्तुकहरूको लागि):",
            "Uploaded ID Proof": "पहिचान प्रमाण अपलोड भयो",
            "ID proof recognized successfully.": "पहिचान प्रमाण सफलतापूर्वक पहिचान भयो।",
            "Please Upload the Id proof": "कृपया पहिचान प्रमाण अपलोड गर्नुहोस्",
            "No foreign visitors": "कुनै विदेशी आगन्तुक छैन",
            "Are you looking to take photos and videos in the museum?": "के तपाईं संग्रहालयमा फोटो र भिडियोहरू लिन चाहनुहुन्छ?",
            "You are going to take photos and videos": "तपाईं फोटो र भिडियोहरू लिन जाँदै हुनुहुन्छ",
            "Not Needed": "आवश्यक छैन",
            "Is parking required?": "के पार्किङ आवश्यक छ?",
            "Yes we need parking facility": "हो, हामीलाई पार्किङ सुविधा आवश्यक छ",
            "Not needed any parking facility": "कुनै पनि पार्किङ सुविधा आवश्यक छैन",
            "Total bill amount": "कुल बिल रकम",
            "Are you willing to process the payment?": "के तपाईं भुक्तानी प्रक्रिया गर्न तयार हुनुहुन्छ?",
            "Proceeding to payment gateway...": "भुक्तानी गेटवेमा जाँदैछ...",
            "Booking not completed.": "बुकिंग पूरा भएन।",
            "Thank you for visiting! Please reach out when you are ready to book.": "भेट्नुभएकोमा धन्यवाद! कृपया बुक गर्न तयार हुँदा हामीलाई सम्पर्क गर्नुहोस्।"
        },

        "ਪੰਜਾਬੀ": {  # Punjabi translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "ਸਾਡੀ ਟਿਕਟ ਬੱਡੀ ਬੋਟ ਚੋਣ ਅਧਾਰਤ ਬੁਕਿੰਗ ਸੇਵਾ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ",
            "Choose Your Language": "ਆਪਣੀ ਭਾਸ਼ਾ ਚੁਣੋ",
            "Are you looking to book a museum ticket?": "ਕੀ ਤੁਸੀਂ ਇੱਕ ਮਿਊਜ਼ੀਅਮ ਟਿਕਟ ਬੁੱਕ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
            "Yes": "ਹਾਂ",
            "No": "ਨਹੀਂ",
             "Continue the next Steps to get your tickets": "ਆਪਣੀਆਂ ਟਿਕਟਾਂ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਅਗਲੇ ਕਦਮ ਜਾਰੀ ਰੱਖੋ",
            "You Preferred ": "ਤੁਸੀਂ ਤਰਜੀਹ ਦਿੱਤੀ ",
            "Select a museum:": "ਇੱਕ ਮਿਊਜ਼ੀਅਮ ਚੁਣੋ:",
            "You have selected": "ਤੁਸੀਂ ਚੁਣਿਆ ਹੈ",
            "Number of adult tickets (₹15 each):": "ਵੱਡਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ (₹15 ਪ੍ਰਤੀ ਟਿਕਟ):",
            "Adult Ticket Count is Completed": "ਵੱਡਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ ਪੂਰੀ ਹੋ ਗਈ ਹੈ",
            "You need": "ਤੁਹਾਨੂੰ ਲੋੜ ਹੈ",
            "number of Adult Tickets": "ਵੱਡਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ",
            "Number of children tickets (₹5 each):": "ਬੱਚਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ (₹5 ਪ੍ਰਤੀ ਟਿਕਟ):",
            "Child Ticket Count is Completed": "ਬੱਚਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ ਪੂਰੀ ਹੋ ਗਈ ਹੈ",
            "number of Child Tickets": "ਬੱਚਿਆਂ ਦੇ ਟਿਕਟਾਂ ਦੀ ਗਿਣਤੀ",
            "Is there any foreign visitor?": "ਕੀ ਕੋਈ ਵਿਦੇਸ਼ੀ ਮਹਿਮਾਨ ਹੈ?",
            "Upload ID proof (for foreign visitors):": "ID ਸਬੂਤ ਅੱਪਲੋਡ ਕਰੋ (ਵਿਦੇਸ਼ੀ ਮਹਿਮਾਨਾਂ ਲਈ):",
            "Uploaded ID Proof": "ID ਸਬੂਤ ਅੱਪਲੋਡ ਹੋ ਗਿਆ ਹੈ",
            "ID proof recognized successfully.": "ID ਸਬੂਤ ਸਫਲਤਾਪੂਰਵਕ ਪਛਾਣਿਆ ਗਿਆ ਹੈ।",
            "Please Upload the Id proof": "ਕਿਰਪਾ ਕਰਕੇ ID ਸਬੂਤ ਅੱਪਲੋਡ ਕਰੋ",
            "No foreign visitors": "ਕੋਈ ਵਿਦੇਸ਼ੀ ਮਹਿਮਾਨ ਨਹੀਂ",
            "Are you looking to take photos and videos in the museum?": "ਕੀ ਤੁਸੀਂ ਮਿਊਜ਼ੀਅਮ ਵਿੱਚ ਫੋਟੋਆਂ ਅਤੇ ਵੀਡੀਓਜ਼ ਖਿੱਚਣੇ ਚਾਹੁੰਦੇ ਹੋ?",
            "You are going to take photos and videos": "ਤੁਸੀਂ ਫੋਟੋਆਂ ਅਤੇ ਵੀਡੀਓਜ਼ ਖਿੱਚਣੇ ਜਾ ਰਹੇ ਹੋ",
            "Not Needed": "ਜਰੂਰਤ ਨਹੀਂ",
            "Is parking required?": "ਕੀ ਪਾਰਕਿੰਗ ਦੀ ਲੋੜ ਹੈ?",
            "Yes we need parking facility": "ਹਾਂ, ਸਾਨੂੰ ਪਾਰਕਿੰਗ ਸਹੂਲਤ ਦੀ ਲੋੜ ਹੈ",
            "Not needed any parking facility": "ਕੋਈ ਪਾਰਕਿੰਗ ਸਹੂਲਤ ਦੀ ਜ਼ਰੂਰਤ ਨਹੀਂ",
            "Total bill amount": "ਕੁੱਲ ਬਿਲ ਰਕਮ",
            "Are you willing to process the payment?": "ਕੀ ਤੁਸੀਂ ਭੁਗਤਾਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ?",
            "Proceeding to payment gateway...": "ਭੁਗਤਾਨ ਗੇਟਵੇ 'ਤੇ ਜਾ ਰਿਹਾ ਹੈ...",
            "Booking not completed.": "ਬੁਕਿੰਗ ਪੂਰੀ ਨਹੀਂ ਹੋਈ।",
            "Thank you for visiting! Please reach out when you are ready to book.": "ਮੁਲਾਕਾਤ ਲਈ ਧੰਨਵਾਦ! ਜਦੋਂ ਤੁਸੀਂ ਬੁੱਕ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋਵੋ ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਸੰਪਰਕ ਕਰੋ।"
        },

        "संस्कृत": {  # Sanskrit translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "टिकट बडी बोट चयन आधारित बुकिंग सेवा में स्वागतं अस्ति",
            "Choose Your Language": "तव भाषा चयनय",
            "Are you looking to book a museum ticket?": "किं त्वं संग्रहालयस्य टिकटं बुक करतुं इच्छसि?",
            "Yes": "आम्",
            "No": "न",
            "Continue the next Steps to get your tickets": "तव टिकटं प्राप्स्यते यावत् अनुवर्तमानं क्रियते",
            "You Preferred ": "त्वं प्राधान्यं अकरोत् ",
            "Select a museum:": "संग्रहालयं चयनय:",
            "You have selected": "त्वं चयनितवान्",
            "Number of adult tickets (₹15 each):": "प्रौढ टिकटानां संख्या (प्रत्येकं ₹15):",
            "Adult Ticket Count is Completed": "प्रौढ टिकटानां गणना समाप्ता अस्ति",
            "You need": "त्वं आवश्यकं",
            "number of Adult Tickets": "प्रौढ टिकटानां संख्या",
            "Number of children tickets (₹5 each):": "बालकानां टिकटानां संख्या (प्रत्येकं ₹5):",
            "Child Ticket Count is Completed": "बालकानां टिकटानां गणना समाप्ता अस्ति",
            "number of Child Tickets": "बालकानां टिकटानां संख्या",
            "Is there any foreign visitor?": "किं कश्चित् विदेशीयः आगन्ता अस्ति?",
            "Upload ID proof (for foreign visitors):": "ID प्रमाणं अपलोड कुरु (विदेशीय आगन्तुकार्थे):",
            "Uploaded ID Proof": "ID प्रमाणं अपलोडम् अस्ति",
            "ID proof recognized successfully.": "ID प्रमाणं सफलतया अभिज्ञातम्।",
            "Please Upload the Id proof": "कृपया ID प्रमाणं अपलोड कुरु",
            "No foreign visitors": "कश्चित् विदेशीयः आगन्ता नास्ति",
            "Are you looking to take photos and videos in the museum?": "किं त्वं संग्रहालये चित्राणि च वीडियो च ग्रहीतुं इच्छसि?",
            "You are going to take photos and videos": "त्वं चित्राणि च वीडियो च ग्रहीतुं गच्छसि",
            "Not Needed": "न आवश्यकम्",
            "Is parking required?": "किं पार्किंग आवश्यकता अस्ति?",
            "Yes we need parking facility": "आम्, अस्माकं पार्किंग सुविधा आवश्यकम् अस्ति",
            "Not needed any parking facility": "कोऽपि पार्किंग सुविधा न आवश्यकः",
            "Total bill amount": "संपूर्णं बिल् माण्यम्",
            "Are you willing to process the payment?": "किं त्वं भुगतान प्रक्रिया कुरु इच्छसि?",
            "Proceeding to payment gateway...": "भुगतान गेटवे प्रत्यगच्छामः...",
            "Booking not completed.": "बुकिंग समाप्तं न अस्ति।",
            "Thank you for visiting! Please reach out when you are ready to book.": "आगमनाय धन्यवादः! कृपया यदा बुकिंगं कर्तुं इच्छसि तदा सम्पर्कं कुरु।"
        },       
        "অসমীয়া": {  # Assamese translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "আমাৰ টিকট বাডী বট নিৰ্বাচন ভিত্তিক বুকিং সেৱালৈ স্বাগতম",
            "Choose Your Language": "আপোনাৰ ভাষা বাছনি কৰক",
            "Are you looking to book a museum ticket?": "আপুনি এটা মিউজিয়ামৰ টিকট বুক কৰাৰ সুঁতি কৰিছে নেকি?",
            "Yes": "হয়",
            "No": "না",
            "Continue the next Steps to get your tickets": "আপোনাৰ টিকট পাবলৈ পৰৱর্তী পদক্ষেপ অব্যাহত ৰাখক",
            "You Preferred ": "আপুনি পচন্দ কৰিছে ",
            "Select a museum:": "এটা মিউজিয়াম বাছনি কৰক:",
            "You have selected": "আপুনি বাছনি কৰিছে",
            "Number of adult tickets (₹15 each):": "প্ৰাপ্তবয়স্ক টিকটৰ সংখ্যা (₹15 প্ৰতিটো):",
            "Adult Ticket Count is Completed": "প্ৰাপ্তবয়স্ক টিকটৰ গণনা সম্পূৰ্ণ হৈছে",
            "You need": "আপোনাৰ প্ৰয়োজন",
            "number of Adult Tickets": "প্ৰাপ্তবয়স্ক টিকটৰ সংখ্যা",
            "Number of children tickets (₹5 each):": "শিশুৰ টিকটৰ সংখ্যা (₹5 প্ৰতিটো):",
            "Child Ticket Count is Completed": "শিশুৰ টিকটৰ গণনা সম্পূৰ্ণ হৈছে",
            "number of Child Tickets": "শিশুৰ টিকটৰ সংখ্যা",
            "Is there any foreign visitor?": "কোনো বৈদেশিক পৰ্যটক আছে নেকি?",
            "Upload ID proof (for foreign visitors):": "ID প্ৰমাণ আপলোড কৰক (বৈদেশিক পৰ্যটকৰ বাবে):",
            "Uploaded ID Proof": "ID প্ৰমাণ আপলোড কৰা হৈছে",
            "ID proof recognized successfully.": "ID প্ৰমাণ সফলতাৰে স্বীকৃত হৈছে।",
            "Please Upload the Id proof": "অনুগ্ৰহ কৰি ID প্ৰমাণ আপলোড কৰক",
            "No foreign visitors": "কোনো বৈদেশিক পৰ্যটক নাই",
            "Are you looking to take photos and videos in the museum?": "আপুনি মিউজিয়ামত ফটো আৰু ভিডিও লব বিচাৰিছে নেকি?",
            "You are going to take photos and videos": "আপুনি ফটো আৰু ভিডিও ল'বলৈ গৈছে",
            "Not Needed": "প্ৰয়োজন নাই",
            "Is parking required?": "পাৰ্কিংৰ প্ৰয়োজন আছে নেকি?",
            "Yes we need parking facility": "হয়, আমাৰ পাৰ্কিং সুবিধাৰ প্ৰয়োজন",
            "Not needed any parking facility": "কোনো পাৰ্কিং সুবিধাৰ প্ৰয়োজন নাই",
            "Total bill amount": "মুঠ বিল পৰিমাণ",
            "Are you willing to process the payment?": "আপুনি পৰিশোধ প্ৰক্ৰিয়া আৰম্ভ কৰিব বিচাৰে নেকি?",
            "Proceeding to payment gateway...": "পৰিশোধ গেটৱেলৈ আগবাঢ়িছে...",
            "Booking not completed.": "বুকিং সম্পূৰ্ণ হোৱা নাই।",
            "Thank you for visiting! Please reach out when you are ready to book.": "ভিজিট কৰিবলৈ ধন্যবাদ! বুক কৰিবলৈ সাজু হ'লে অনুগ্ৰহ কৰি যোগাযোৰ কৰক।"
        },

        "ಕನ್ನಡ": {  # Kannada translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "ನಮ್ಮ ಟಿಕೆಟ್ ಬಡ್ಡಿ ಬಾಟ್ ಆಯ್ಕೆಯ ಆಧಾರದ ಮೇಲೆ ಬುಕ್ಕಿಂಗ್ ಸೇವೆಗೆ ಸ್ವಾಗತ",
            "Choose Your Language": "ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆರಿಸಿ",
            "Are you looking to book a museum ticket?": "ನೀವು ಮ್ಯೂಸಿಯಂ ಟಿಕೆಟ್ ಬುಕ್ ಮಾಡಲು ನೋಡುತ್ತಿದ್ದೀರಾ?",
            "Yes": "ಹೌದು",
            "No": "ಇಲ್ಲ",
            "Continue the next Steps to get your tickets": "ನಿಮ್ಮ ಟಿಕೆಟ್ ಪಡೆಯಲು ಮುಂದಿನ ಹಂತಗಳನ್ನು ಮುಂದುವರಿಸಿ",
            "You Preferred ": "ನೀವು ಆದ್ಯತೆ ನೀಡಿದ್ದೀರಿ ",
            "Select a museum:": "ಒಂದು ಮ್ಯೂಸಿಯಂ ಆಯ್ಕೆ ಮಾಡಿ:",
            "You have selected": "ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ್ದೀರಿ",
            "Number of adult tickets (₹15 each):": "ವಯಸ್ಕರ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ (₹15 ಪ್ರತಿ ಟಿಕೆಟ್):",
            "Adult Ticket Count is Completed": "ವಯಸ್ಕರ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ ಪೂರ್ತಿಯಾಗಿದೆ",
            "You need": "ನೀವು ಬೇಕು",
            "number of Adult Tickets": "ವಯಸ್ಕರ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ",
            "Number of children tickets (₹5 each):": "ಮಕ್ಕಳ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ (₹5 ಪ್ರತಿ ಟಿಕೆಟ್):",
            "Child Ticket Count is Completed": "ಮಕ್ಕಳ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ ಪೂರ್ತಿಯಾಗಿದೆ",
            "number of Child Tickets": "ಮಕ್ಕಳ ಟಿಕೆಟ್ ಸಂಖ್ಯೆ",
            "Is there any foreign visitor?": "ಯಾವುದಾದರೂ ವಿದೇಶಿ ಪ್ರವಾಸಿಗನಿದೆಯೇ?",
            "Upload ID proof (for foreign visitors):": "ID ಪುರಾವೆ ಅಪ್ಲೋಡ್ ಮಾಡಿ (ವಿದೇಶಿ ಪ್ರವಾಸಿಗರಿಗೆ):",
            "Uploaded ID Proof": "ID ಪುರಾವೆ ಅಪ್ಲೋಡ್ ಮಾಡಲಾಗಿದೆ",
            "ID proof recognized successfully.": "ID ಪುರಾವೆ ಯಶಸ್ವಿಯಾಗಿ ಗುರುತಿಸಲಾಗಿದೆ.",
            "Please Upload the Id proof": "ದಯವಿಟ್ಟು ID ಪುರಾವೆ ಅಪ್ಲೋಡ್ ಮಾಡಿ",
            "No foreign visitors": "ಯಾವುದೇ ವಿದೇಶಿ ಪ್ರವಾಸಿಗರಿಲ್ಲ",
            "Are you looking to take photos and videos in the museum?": "ನೀವು ಮ್ಯೂಸಿಯಂನಲ್ಲಿ ಫೋಟೋಗಳು ಮತ್ತು ವಿಡಿಯೋಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಬಯಸುತ್ತೀರಾ?",
            "You are going to take photos and videos": "ನೀವು ಫೋಟೋಗಳು ಮತ್ತು ವಿಡಿಯೋಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಹೋಗುತ್ತಿದ್ದೀರಿ",
            "Not Needed": "ಬೇಡ",
            "Is parking required?": "ಪಾರ್ಕಿಂಗ್ ಬೇಕು?",
            "Yes we need parking facility": "ಹೌದು, ನಮಗೆ ಪಾರ್ಕಿಂಗ್ ಸೌಲಭ್ಯ ಬೇಕು",
            "Not needed any parking facility": "ಯಾವುದೇ ಪಾರ್ಕಿಂಗ್ ಸೌಲಭ್ಯ ಅಗತ್ಯವಿಲ್ಲ",
            "Total bill amount": "ಒಟ್ಟು ಬಿಲ್ ಮೊತ್ತ",
            "Are you willing to process the payment?": "ನೀವು ಪಾವತಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಸಿದ್ಧವಾಗಿದ್ದೀರಾ?",
            "Proceeding to payment gateway...": "ಪಾವತಿ ಗೇಟ್ವೇಗೆ ಮುಂದುವರಿಯುತ್ತಿದೆ...",
            "Booking not completed.": "ಬುಕ್ಕಿಂಗ್ ಪೂರ್ಣಗೊಂಡಿಲ್ಲ.",
            "Thank you for visiting! Please reach out when you are ready to book.": "ಸಂದರ್ಶನಕ್ಕೆ ಧನ್ಯವಾದಗಳು! ಬುಕ್ಕಿಂಗ್ ಮಾಡಲು ಸಿದ್ಧವಿದ್ದಾಗ ದಯವಿಟ್ಟು ಸಂಪರ್ಕಿಸಿ."
        },

        "മലയാളം": {  # Malayalam translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "ഞങ്ങളുടെ ടിക്കറ്റ് ബഡ്ഡി ബോട്ട് തിരഞ്ഞെടുപ്പിനെ അടിസ്ഥാനമാക്കി ബുക്കിംഗ് സേവനത്തിലേക്ക് സ്വാഗതം",
            "Choose Your Language": "നിങ്ങളുടെ ഭാഷ തിരഞ്ഞെടുക്കുക",
            "Are you looking to book a museum ticket?": "നിങ്ങൾ ഒരു മ്യൂസിയം ടിക്കറ്റ് ബുക്ക് ചെയ്യാൻ ഉദ്ദേശിക്കുന്നുണ്ടോ?",
            "Yes": "അതെ",
            "No": "ഇല്ല",
            "Continue the next Steps to get your tickets": "നിങ്ങളുടെ ടിക്കറ്റ് ലഭിക്കാൻ അടുത്ത ഘട്ടങ്ങൾ തുടരുക",
            "You Preferred ": "നിങ്ങൾ ഇഷ്ടപ്പെട്ടത് ",
            "Select a museum:": "ഒരു മ്യൂസിയം തിരഞ്ഞെടുക്കുക:",
            "You have selected": "നിങ്ങൾ തിരഞ്ഞെടുക്കിയിരിക്കുന്നു",
            "Number of adult tickets (₹15 each):": "വയോജന ടിക്കറ്റുകളുടെ എണ്ണം (₹15 ഓരോ ടിക്കറ്റിനും):",
            "Adult Ticket Count is Completed": "വയോജന ടിക്കറ്റുകളുടെ എണ്ണം പൂർത്തിയാക്കപ്പെട്ടു",
            "You need": "നിങ്ങള്ക്ക് ആവശ്യമുണ്ട്",
            "number of Adult Tickets": "വയോജന ടിക്കറ്റുകളുടെ എണ്ണം",
            "Number of children tickets (₹5 each):": "മക്കളുടെ ടിക്കറ്റുകളുടെ എണ്ണം (₹5 ഓരോ ടിക്കറ്റിനും):",
            "Child Ticket Count is Completed": "മക്കളുടെ ടിക്കറ്റുകളുടെ എണ്ണം പൂർത്തിയാക്കപ്പെട്ടു",
            "number of Child Tickets": "മക്കളുടെ ടിക്കറ്റുകളുടെ എണ്ണം",
            "Is there any foreign visitor?": "എന്തെങ്കിലും വിദേശ സന്ദർശകനുണ്ടോ?",
            "Upload ID proof (for foreign visitors):": "ID പ്രൂഫ് അപ്‌ലോഡ് ചെയ്യുക (വിദേശ സന്ദർശകർക്ക്):",
            "Uploaded ID Proof": "ID പ്രൂഫ് അപ്‌ലോഡ് ചെയ്തിരിക്കുന്നു",
            "ID proof recognized successfully.": "ID പ്രൂഫ് വിജയകരമായി തിരിച്ചറിഞ്ഞു.",
            "Please Upload the Id proof": "ദയവായി ID പ്രൂഫ് അപ്‌ലോഡ് ചെയ്യുക",
            "No foreign visitors": "വിദേശ സന്ദർശകർ ഇല്ല",
            "Are you looking to take photos and videos in the museum?": "നിങ്ങൾ മ്യൂസിയത്തിൽ ഫോട്ടോകളും വീഡിയോകളും എടുക്കാൻ ആഗ്രഹിക്കുന്നുണ്ടോ?",
            "You are going to take photos and videos": "നിങ്ങൾ ഫോട്ടോകളും വീഡിയോകളും എടുക്കാൻ പോകുന്നു",
            "Not Needed": "ആവശ്യമില്ല",
            "Is parking required?": "പാർക്കിംഗ് ആവശ്യമാണ്?",
            "Yes we need parking facility": "അതെ, ഞങ്ങൾക്ക് പാർക്കിംഗ് സൗകര്യം ആവശ്യമുണ്ട്",
            "Not needed any parking facility": "ഏതെങ്കിലും പാർക്കിംഗ് സൗകര്യം ആവശ്യമില്ല",
            "Total bill amount": "മൊത്തം ബിൽ തുക",
            "Are you willing to process the payment?": "നിങ്ങൾ പണമടയ്ക്കൽ പ്രക്രിയ ആരംഭിക്കാനൊരുങ്ങുന്നുണ്ടോ?",
            "Proceeding to payment gateway...": "പെയ്മെന്റ് ഗേറ്റ്വേയിലേക്ക് നീങ്ങുന്നു...",
            "Booking not completed.": "ബുക്കിംഗ് പൂർത്തിയാക്കാത്തത്.",
            "Thank you for visiting! Please reach out when you are ready to book.": "സന്ദർശിച്ചതിന് നന്ദി! ബുക്ക് ചെയ്യാൻ തയാറായപ്പോൾ ദയവായി ഞങ്ങളെ ബന്ധപ്പെടുക."
        },

        "اردو": {  # Urdu translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "ہمارے ٹکٹ بڈی بوٹ سلیکشن بیسڈ بکنگ سروس میں خوش آمدید",
            "Choose Your Language": "اپنی زبان کا انتخاب کریں",
            "Are you looking to book a museum ticket?": "کیا آپ میوزیم کا ٹکٹ بک کرنا چاہتے ہیں؟",
            "Yes": "جی ہاں",
            "No": "نہیں",
            "Continue the next Steps to get your tickets": "اپنے ٹکٹ حاصل کرنے کے لئے اگلے مراحل جاری رکھیں",
            "You Preferred ": "آپ نے ترجیح دی ",
            "Select a museum:": "ایک میوزیم کا انتخاب کریں:",
            "You have selected": "آپ نے منتخب کیا ہے",
            "Number of adult tickets (₹15 each):": "بالغوں کے ٹکٹوں کی تعداد (₹15 فی ٹکٹ):",
            "Adult Ticket Count is Completed": "بالغوں کے ٹکٹوں کی گنتی مکمل ہو چکی ہے",
            "You need": "آپ کو ضرورت ہے",
            "number of Adult Tickets": "بالغوں کے ٹکٹوں کی تعداد",
            "Number of children tickets (₹5 each):": "بچوں کے ٹکٹوں کی تعداد (₹5 فی ٹکٹ):",
            "Child Ticket Count is Completed": "بچوں کے ٹکٹوں کی گنتی مکمل ہو چکی ہے",
            "number of Child Tickets": "بچوں کے ٹکٹوں کی تعداد",
            "Is there any foreign visitor?": "کیا کوئی غیر ملکی وزیٹر ہے؟",
            "Upload ID proof (for foreign visitors):": "شناختی ثبوت اپلوڈ کریں (غیر ملکی وزیٹرز کے لئے):",
            "Uploaded ID Proof": "شناختی ثبوت اپلوڈ ہو چکا ہے",
            "ID proof recognized successfully.": "شناختی ثبوت کامیابی سے پہچانا گیا ہے۔",
            "Please Upload the Id proof": "براہ کرم شناختی ثبوت اپلوڈ کریں",
            "No foreign visitors": "کوئی غیر ملکی وزیٹر نہیں",
            "Are you looking to take photos and videos in the museum?": "کیا آپ میوزیم میں تصاویر اور ویڈیوز بنانا چاہتے ہیں؟",
            "You are going to take photos and videos": "آپ تصاویر اور ویڈیوز بنانے جا رہے ہیں",
            "Not Needed": "ضرورت نہیں",
            "Is parking required?": "کیا پارکنگ کی ضرورت ہے؟",
            "Yes we need parking facility": "جی ہاں، ہمیں پارکنگ کی سہولت چاہیے",
            "Not needed any parking facility": "کوئی پارکنگ کی سہولت کی ضرورت نہیں",
            "Total bill amount": "کل بل کی رقم",
            "Are you willing to process the payment?": "کیا آپ ادائیگی کا عمل جاری رکھنا چاہتے ہیں؟",
            "Proceeding to payment gateway...": "ادائیگی کے گیٹ وے کی طرف بڑھ رہا ہے...",
            "Booking not completed.": "بکنگ مکمل نہیں ہوئی۔",
            "Thank you for visiting! Please reach out when you are ready to book.": "تشریف لانے کا شکریہ! جب آپ بکنگ کے لیے تیار ہوں تو براہ کرم رابطہ کریں۔"
        },

        "سنڌي": {  # Sindhi translations
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "اسان جي ٽڪيٽ بڊي بوٽ چونڊ تي ٻڌل بڪنگ سروس ۾ ڀليڪار",
            "Choose Your Language": "پنهنجي ٻولي چونڊيو",
            "Are you looking to book a museum ticket?": "ڇا توهان هڪ ميوزيم جو ٽڪيٽ بڪ ڪرڻ جي ڳولا ۾ آهيو؟",
            "Yes": "ها",
            "No": "نه",
            "Continue the next Steps to get your tickets": "پنھنجا ٽڪيٽ حاصل ڪرڻ لاءِ ايندڙ مرحلا جاري رکو",
            "Select a museum:": "هڪ ميوزيم چونڊيو:",
            "You Preferred ": "توهان پسند ڪيو ",
            "You have selected": "توهان چونڊيو آهي",
            "Number of adult tickets (₹15 each):": "بالغن جي ٽڪيٽن جو تعداد (₹15 في ٽڪيٽ):",
            "Adult Ticket Count is Completed": "بالغن جي ٽڪيٽن جي گنتي مڪمل ٿي وئي آهي",
            "You need": "توهان کي ضرورت آهي",
            "number of Adult Tickets": "بالغن جي ٽڪيٽن جو تعداد",
            "Number of children tickets (₹5 each):": "ٻارن جي ٽڪيٽن جو تعداد (₹5 في ٽڪيٽ):",
            "Child Ticket Count is Completed": "ٻارن جي ٽڪيٽن جي گنتي مڪمل ٿي وئي آهي",
            "number of Child Tickets": "ٻارن جي ٽڪيٽن جو تعداد",
            "Is there any foreign visitor?": "ڇا ڪا ٻاهرين مهمان آهي؟",
            "Upload ID proof (for foreign visitors):": "آئي ڊي ثبوت اپلوڊ ڪريو (ٻاهرين مهمانن لاءِ):",
            "Uploaded ID Proof": "آئي ڊي ثبوت اپلوڊ ٿي وئي آهي",
            "ID proof recognized successfully.": "آئي ڊي ثبوت ڪاميابي سان سڃاتو ويو.",
            "Please Upload the Id proof": "مهرباني ڪري آئي ڊي ثبوت اپلوڊ ڪريو",
            "No foreign visitors": "ڪو ٻاهرين مهمان ناهي",
            "Are you looking to take photos and videos in the museum?": "ڇا توهان ميوزيم ۾ تصويرون ۽ وڊيوز وٺڻ چاهيو ٿا؟",
            "You are going to take photos and videos": "توهان تصويرون ۽ وڊيوز وٺڻ وارا آهيو",
            "Not Needed": "ضرورت ناهي",
            "Is parking required?": "ڇا پارڪنگ جي ضرورت آهي؟",
            "Yes we need parking facility": "ها، اسان کي پارڪنگ جي سهولت گهرجي",
            "Not needed any parking facility": "ڪو پارڪنگ جي سهولت جي ضرورت ناهي",
            "Total bill amount": "ڪل بل جي رقم",
            "Are you willing to process the payment?": "ڇا توهان ادائيگي جي عمل کي جاري رکڻ چاهيو ٿا؟",
            "Proceeding to payment gateway...": "ادائيگي جي گيٽ وي ڏانهن اڳتي وڌي رهيو آهي...",
            "Booking not completed.": "بڪنگ مڪمل نه ٿي.",
            "Thank you for visiting! Please reach out when you are ready to book.": "تشريف آڻڻ لاءِ مهرباني! جڏھن توھان بڪنگ لاءِ تيار آھيو، مھرباني ڪري اسان سان رابطو ڪريو."
        },
            "English": {
                "Welcome to our Ticket Buddy Bot Selection Based booking service": "Welcome to our Ticket Buddy Bot Selection Based booking service",
                "Choose Your Language": "Choose Your Language",
                "Are you looking to book a museum ticket?": "Are you looking to book a museum ticket?",
                "Yes": "Yes",
                "No": "No",
                "Continue the next Steps to get your tickets": "Continue the next Steps to get your tickets",
                "You Preferred ": "You Preferred ",
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
                "Thank you for visiting! Please reach out when you are ready to book.": "Thank you for visiting! Please reach out when you are ready to book."
            },
        "हिंदी": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "हमारी टिकट बडी बॉट चयन आधारित बुकिंग सेवा में आपका स्वागत है",
            "Choose Your Language": "अपनी भाषा चुनें",
            "Are you looking to book a museum ticket?": "क्या आप संग्रहालय का टिकट बुक करना चाहते हैं?",
            "Yes": "हाँ",
            "No": "नहीं",
            "Continue the next Steps to get your tickets": "अपनी टिकट प्राप्त करने के लिए अगले चरणों को जारी रखें",
            "You Preferred ": "आपने हिंदी को प्राथमिकता दी",
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
            "Thank you for visiting! Please reach out when you are ready to book.": "आपके आने के लिए धन्यवाद! कृपया बुक करने के लिए तैयार होने पर संपर्क करें।"
        },
        "ગુજરાતી": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "અમારી ટિકિટ બડી બોટ પસંદગી આધારિત બુકિંગ સેવા માં આપનું સ્વાગત છે",
            "Choose Your Language": "તમારી ભાષા પસંદ કરો",
            "Are you looking to book a museum ticket?": "શું તમે મ્યુઝિયમ ટિકિટ બુક કરવા માંગો છો?",
            "Yes": "હા",
            "No": "ના",
            "Continue the next Steps to get your tickets": "તમારા ટિકિટ મેળવવા માટેના આગળના પગલાં ચાલુ રાખો",
            "You Preferred ": "તમે પસંદ કરી છે ",
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
            "Thank you for visiting! Please reach out when you are ready to book.": "મુલાકાત માટે આભાર! કૃપા કરીને બુકિંગ માટે તૈયાર થો ત્યારે સંપર્ક કરો."
        },
        "தமிழ்": {
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "எங்கள் டிக்கெட் படி போட் தேர்வு அடிப்படையிலான முன்பதிவு சேவைக்கு வருக",
            "Choose Your Language": "உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்",
            "Are you looking to book a museum ticket?": "நீங்கள் ஒரு அருங்காட்சியக டிக்கெட் முன்பதிவு செய்ய விரும்புகிறீர்களா?",
            "Yes": "ஆம்",
            "No": "இல்லை",
            "Continue the next Steps to get your tickets": "உங்கள் சீட்டுகளைப் பெற அடுத்த படிகள் தொடரவும்",
            "You Preferred ": "நீங்கள் விரும்பியது ",
            "Select a museum:": "ஒரு அருங்காட்சியகத்தைத் தேர்ந்தெடுக்கவும்:",
            "You have selected": "நீங்கள் தேர்வு செய்துள்ளீர்கள்",
            "Number of adult tickets (₹15 each):": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை (₹15 ஒவ்வொன்றும்):",
            "Adult Ticket Count is Completed": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை முடிந்தது",
            "You need": "உங்களுக்கு தேவை",
            "number of Adult Tickets": "முதிர்ந்தோர் டிக்கெட் எண்ணிக்கை",
            "Number of children tickets (₹5 each):": "குழந்தை டிக்கெட் எண்ணிக்கை (₹5 ஒவ்வொன்றும்):",
            "Child Ticket Count is Completed": "குழந்தை டிக்கெட் எண்ணிக்கை முடிந்தது",
            "number of Child Tickets": "குழந்தை டிக்கெட் எண்ணிக்கை",
            "Is there any foreign visitor?": "வெளிநாட்டு பயணி யாராவது இருக்கிறார்களா?",
            "Upload ID proof (for foreign visitors):": "ID ஆதாரம் பதிவேற்றவும் (வெளிநாட்டு பயணிகள்):",
            "Uploaded ID Proof": "ID ஆதாரம் பதிவேற்றப்பட்டது",
            "ID proof recognized successfully.": "ID ஆதாரம் வெற்றிகரமாக அடையாளம் காணப்பட்டது.",
            "Please Upload the Id proof": "ID ஆதாரத்தை பதிவேற்றவும்",
            "No foreign visitors": "வெளிநாட்டு பயணிகள் இல்லை",
            "Are you looking to take photos and videos in the museum?": "நீங்கள் அருங்காட்சியகத்தில் புகைப்படங்கள் மற்றும் வீடியோக்களை எடுக்க விரும்புகிறீர்களா?",
            "You are going to take photos and videos": "நீங்கள் புகைப்படங்கள் மற்றும் வீடியோக்களை எடுக்க இருக்கிறீர்கள்",
            "Not Needed": "தேவையில்லை",
            "Is parking required?": "பார்கிங் தேவைப்படுகிறதா?",
            "Yes we need parking facility": "ஆம், பார்க்கிங் வசதி தேவை",
            "Not needed any parking facility": "எந்த பார்கிங் வசதியும் தேவையில்லை",
            "Total bill amount": "மொத்த பில் தொகை",
            "Are you willing to process the payment?": "நீங்கள் கட்டணம் செலுத்த தயாராக இருக்கிறீர்களா?",
            "Proceeding to payment gateway...": "கட்டண கேட்வேக்கு செல்கிறது...",
            "Booking not completed.": "முன்பதிவு முடிந்தது இல்லை.",
            "Thank you for visiting! Please reach out when you are ready to book.": "வருகைக்கு நன்றி! முன்பதிவுக்கு தயாரான போது தயவுசெய்து அணுகவும்."
        },
        "తెలుగు": { #telugu
            "Welcome to our Ticket Buddy Bot Selection Based booking service": "మా టిక్కెట్ బడి బోట్ ఎంపిక ఆధారిత బుకింగ్ సేవకు స్వాగతం",
            "Choose Your Language": "మీ భాషను ఎంచుకోండి",
            "Are you looking to book a museum ticket?": "మీరు మ్యూజియం టికెట్ బుక్ చేయాలనుకుంటున్నారా?",
            "Yes": "అవును",
            "No": "లేదు",
            "Continue the next Steps to get your tickets": "మీ టిక్కెట్లు పొందడానికి తదుపరి చర్యలను కొనసాగించండి",
            "You Preferred ": "మీరు ఇష్టపడ్డారు ",
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
            "Thank you for visiting! Please reach out when you are ready to book.": "మీ సందర్శనకు ధన్యవాదాలు! మీరు బుక్ చేయడానికి సిద్ధంగా ఉన్నప్పుడు దయచేసి సంప్రదించండి."
        }
    }
    if lang in translations and text in translations[lang]:
        return translations[lang][text]
    else:
        return text  


# List of museums from the given Wikipedia link (you can refine this list as needed)
museum_list = ["---", "National Museum, Delhi", "Indian Museum, Kolkata", "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai", "Salar Jung Museum, Hyderabad", "Government Museum, Chennai", "Albert Hall Museum, Jaipur"]
museum_list.sort()
def main():
    lang="English"
    st.subheader(translate("Welcome to our Ticket Buddy Bot Selection Based booking service",lang))
    lang=st.selectbox("Choose Your Language",("---","অসমীয়া","বাংলা","English","française","Deutsch","ગુજરાતી","हिंदी","ಕನ್ನಡ","کشمیری","bahasa Melayu","മലയാളം","मराठी","नेपाली","ਪੰਜਾਬੀ","Русский","संस्कृत","سنڌي","සිංහල","española","தமிழ்","తెలుగు","اردو"))
    if lang!="---":
        st.info(f"BOT: {translate('You Preferred ',lang)}"+lang)
        booking_option = st.selectbox(translate("Are you looking to book a museum ticket?",lang), ["---", translate("Yes",lang),translate("No",lang)])
        if booking_option == translate("Yes",lang):
            st.info(f"BOT: {translate('Continue the next Steps to get your tickets',lang)}")
            museum = st.selectbox(translate("Select a museum:",lang), museum_list)
            if museum != "---":
                st.info(f"BOT: {translate('You have selected',lang)}"+" "+museum)
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
                                    st.info(f"BOT: "+photo_video+f"{translate('You are going to take photos and videos',lang)}")
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
                            st.info("BOT: "+foreign_visitor)
                            photo_video = st.selectbox(translate("Are you looking to take photos and videos in the museum?",lang), ["---", translate("Yes",lang), translate("No",lang)])
                            if photo_video == translate("Yes",lang):
                                st.info("BOT: "+photo_video+" "+f"{translate('You are going to take photos and videos',lang)}")
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
                        st.info(f"BOT: "+f"{translate('Total bill amount',lang)}"+": ₹"+f"{total_bill}")
        elif booking_option == translate("No",lang):
            st.info(f"BOT: {translate('Thank you for visiting! Please reach out when you are ready to book.',lang)}")

if __name__ == "__main__":
    main()
