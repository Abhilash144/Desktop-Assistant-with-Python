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
    


#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Abhilash sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon Abhilash sir. How are you doing")

    else:
        speak("Good evening Abhilash sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")



if __name__ == "__main__":

    wish_me()

    while True:
        query = takeCommand().lower()
        print(query)
    
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            print(query)

            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif "goodbye" in query:
            speak("ok sir, I am always here for you. Bye Bye!")
            exit()


