import os;
import speech_recognition as sr;
import datetime;
import pyttsx3;
import webbrowser;
import pyaudio

engine=pyttsx3.init('sapi5');
voices=engine.getProperty('voices');
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am siree ,how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio=r.listen(source)

        
        try:
            print("recognizing")
            query=r.recognize_google(audio)
            print(f"user said:{query}\n")

        except Exception as e:
            print("please repeat")
            return "none"
    return query
if __name__=='__main__':
    wishMe()
    x=True
    while x: 
        query=takecommand().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opened youtube")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opened google")
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strtime}\n")   
        elif 'hai' in query:
            speak("hello my lord")
        elif 'bye' in query:
            speak("bye")
            x=False
        
