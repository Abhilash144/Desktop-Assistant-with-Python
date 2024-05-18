
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# Taking voice from my system
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

print(voices)
#print(voices[0].id)
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

#speak Function

def speak(text):
    """This function takes text and return a voice
     Args :
        text : String
    """
    engine.say(text)
    engine.runAndWait()

#speak("Hello I am a programmer, How are You ?")


#Speech Recognition function

def takeCommand():
    """This function will recognize voice and return text
    """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return None
        
        return query
    

text = takeCommand()

speak(text)
