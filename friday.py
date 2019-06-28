import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<3 :
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I'm FRIDAY version 1.0 designed by saumendu das your personal assistant.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
        speak("You said {}".format(query))
    
    except Exception as e:
        print("Say that again...")
        return "none"
    return query

def wiki(query):
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia ")
    print(results)
    speak(results)
    
def openWebsite(query):
    if 'google' in query:
        webbrowser.open("google.com")
    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'wikipedia' in query:
        webbrowser.open("wikipedia.com")
    elif 'facebook' in query:
        webbrowser.open("facebook.com")
    
def showTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("Sir, the time is {}".format(strTime))
    speak("Sir, the time is {}".format(strTime))

if __name__ == '__main__':
    wishMe()
    while True:
        query= takeCommand().lower()
        speak("What you want me to do?")
        if('exit' or 'terminate' or 'off' or 'leave' or 'thank you') in query:
            break

        elif 'wikipedia' in query:
            wiki(query)
        
        elif 'open' in query:
            openWebsite(query)
        
        elif 'time' in query:
            showTime()
        
        elif 'play music' in query:
            music_dir = 'F:\\Music video\\fav\\'  #Enter your file path where music audio or video is present
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        

