import speech_recognition as sr
import noisereduce as nr
import numpy as np
from pydub import AudioSegment
import pyttsx3 
import pyaudio
import wave
import whisper
import os
import google.generativeai as genai

AudioSegment.converter ='C:\\Users\\navab\\Downloads\\SIH-Musuem\\ffmpeg'
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAQ5wyvY_UFB0R5fO_iZG3-ZcERW6brT08'
llm = genai.GenerativeModel(model_name='gemini-pro')
genai.configure(api_key = 'AIzaSyBo8kIw9YzdcB4cLgx0sKs1qnfndY_7Lmc')
listener = sr.Recognizer()
command = None


prompt = """Hey now you are a voice assistant for museum ticket booking applications 
               here your task is to assist user to collect the required information for booking the ticket you should perform as it was a human in place
               VA : Hey user , how can i assist you 
                User  : I am here to book two tickets for the chennai museum on date [you have to ask] for n number of person
                (VA analyses the text and gets the detail - (place, booking ticket, date no)
                (VA still needs info about the no.of child and adults, ………)
                VA : How many child and adults ?
                (Books ticket)
                VA: Do yoou want to have lunch
                (Promoting small scale tourism)
                VA : Suggesting new places

                you should acts as va , your responses have to more similar to human
                dont mention va and user in response 
                your response should like [...........]
                after collecting all the information you have to end the  servis means after collecting required details for ticket booking end the conversation
                should generate the reponse apt to the conversatioon should only consists of brief required information
                ensure your response should have to be very short and crisp and end the conversation by greeting after collected the details
               """
def preprocess_audio(audio_data):
    audio_array = np.array(audio_data.get_array_of_samples())
    reduced_noise = nr.reduce_noise(y=audio_array, sr=audio_data.frame_rate)
    processed_audio = AudioSegment(
        reduced_noise.tobytes(), 
        frame_rate=audio_data.frame_rate,
        sample_width=audio_data.sample_width,
        channels=audio_data.channels
    )
    return processed_audio

def record_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording")
        audio_data = r.listen(source)
        print("Preprocessing audio...")
        raw_audio = audio_data.get_raw_data()
        audio_segment = AudioSegment(
            raw_audio, 
            frame_rate=source.SAMPLE_RATE, 
            sample_width=2, 
            channels=1
        )
        audio_segment.export("original_audio.wav", format="wav")
        processed_audio = preprocess_audio(audio_segment)
        processed_audio.export("processed_audio.wav", format="wav")
        print("Transcribing audio...")
        recognizer_audio = sr.AudioData(
            processed_audio.raw_data, 
            sample_rate=processed_audio.frame_rate, 
            sample_width=processed_audio.sample_width
        )
        try:
            
            recognized_text = r.recognize_google(recognizer_audio,language="en")
            print(recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    



def activate_voice_assistant():
    op = 1
    result = ''
    while 'bye' not in result :
        result = record_audio()
        print(result)
        res = llm.generate_content(prompt+result)
        text_to_speech(res.text)


activate_voice_assistant()
