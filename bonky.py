import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Sir")

    elif hour >= 12 and hour < 16:
        speak("Good afternoon Sir")

    else:
        speak("Good evening Sir")

    speak("Bonky at your service. How may I assist you Sir?")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say That again please..")
        return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play' in query :
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')    
            speak(f'Sir, The time is {strTime}')

        elif 'open vs code' in query:
            vscodePath = "C:\\Users\\Charlie\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)

        elif 'open chess.com' in query:
            webbrowser.open("chess.com")

        elif 'tell me a joke' in query:
            result = pyjokes.get_joke()
            print(result)
            speak(result)  
            
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open blog' in query:
            webbrowser.open("codercharlie.blogspot.com")    

        elif "how's it going" in query:
            speak('All good sir, Thanks to you. I hope your day is going well too.')    

        elif 'thank you' in query :
            speak('My Pleasure Sir') 
            quit()
