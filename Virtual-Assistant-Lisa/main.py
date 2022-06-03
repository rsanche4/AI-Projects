import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import aiml
from PyDictionary import PyDictionary

print("Initializing VAL")
dictionary=PyDictionary()
BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

MASTER = "MASTER"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[1].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning " + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon " + MASTER)

    else:
        speak("good evening " + MASTER)

    speak("Hey there. I am Lisa. How may I help?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rsanzek25@gmail.com', 'password')
    server.sendmail("rsanzek25@gmail.com", to, content)
    server.close()

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = ""

    return query

#main program starting
def main():
    query = takeCommand()
    query = query.lower()
    if query.startswith("lisa"):
        query = query.replace("lisa ", "")
        query = query.replace("lisa,", "")
        query = query.replace("lisa.", "")
        query = query.replace("lisa", "")
        #Logic for executing tasks as per the query
        if 'define ' in query:
            query = query.replace("define ", "")
            found = dictionary.meaning(query)
            answer = list(found.values())[0][0]
            print(query + " means: " + answer)
            speak(query + " means: " + answer)
            # speak('searching wikipedia...')
            # query = query.replace("define ", "")
            # results = wikipedia.summary(query, sentences =2)
            # print(results)
            # speak(results)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif 'see your brain' in query:
            codePath = __file__
            os.startfile(codePath)

        elif 'shutdown' in query:
            speak("Goodbye")
            exit()

        else:
            answer = k.respond(query)
            print("Lisa responded: " + answer)
            speak(answer)

        # elif 'open youtube' in query.lower():
        #     #webbrowser.open('youtube.com')
        #     url = "youtube.com"
        #     chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #     webbrowser.get(chrome_path).open(url)

        # elif 'open google' in query.lower():
        #     #webbrowser.open('youtube.com')
        #     url = "google.com"
        #     chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #     webbrowser.get(chrome_path).open(url)

        # elif 'play music' in query.lower():
        #     songs_dir = "C:\\Users\\Dell\\Desktop\\Photos\\audio"
        #     songs = os.listdir(songs_dir)
        #     print(songs)
        #     os.startfile(os.path.join(songs_dir, songs[0]))
        
        # elif 'email to' in query.lower():
        #     try:
        #         speak("what should i send")
        #         content = takeCommand()
        #         to = "harry@gmail.ocm"
        #         sendEmail(to, content)
        #         speak("Email has been sent to raj")
        #     except Exception as e:
        #         print(e)

speak("Initializing VAL...")
wishMe()
while True:
    main()