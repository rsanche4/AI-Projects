import webbrowser
import pyttsx3 
import speech_recognition as sr
import datetime
from random import choice, randint
import randfacts
import csv
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import pywhatkit
import keyboard
import os
import _thread
import IBrain

MASTER = "MASTER"
botkey_file = open("C:\\Users\\rafas\\Documents\\botkey.txt", 'r')
BOTKEY = botkey_file.read()
nice_and_quiet = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 170
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[2].id)

def speak(text):
    print(f"bot said: {text}")
    engine.say(f'<pitch middle="10">{text}</pitch>')
    engine.runAndWait()
def wishMe():
    global MASTER
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning " + MASTER)
    elif hour>=12 and hour<18:
        speak("good afternoon " + MASTER)
    else:
        speak("good evening " + MASTER)
def takeCommand():
    global wake_not_needed
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            if not nice_and_quiet:
                playsound('listen.wav')
            audio = r.listen(source)
            print("Recognizing...")
            if not nice_and_quiet:
                playsound("recog.wav")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}")
    except Exception as e:
        print("")
        query = ""
    return query.lower()
def query_compare(possible_queries, query):
    for phrase in possible_queries:
        if phrase in query:
            return True
    return False


def girl_listen():
    global nice_and_quiet
    global MASTER
    global BOTKEY
    WAKE_UP = "wake up"
    wishMe()
    while True:
        query = takeCommand()
    
        # If the user doesn't want her to talk for a while or listen, or told her to shut up, then she will only come back up listening once told to "wake up"
        if nice_and_quiet:
            if query.count(WAKE_UP) > 0:
                nice_and_quiet = False
            continue
        
        # just check if it's empty, ignore it
        if query=="":
            continue
        
        # date and time
        elif query_compare(["the time", "what time", "the date", "what date", "today", "the day", "what day", "time of the day", "which day", "what year", "which year", "the month", "what month", "which month"], query):
            hour = datetime.datetime.now()
            date_time = hour.strftime("Today is %d %B of %Y and the week day is %A at %I:%M %p")
            speak(date_time)
        
        # singing a song
        elif query_compare(["sing"], query):
            speak(choice(["I can sing a song for you.", "I know how to sing. Hear me!", "Oh I love singing.", "I love to sing. Listen to my singing voice..."]))
            speak(choice(["This was a triumph. I'm making a note here; 'Huge success'. It's hard to overstate My satisfaction. Aperture Science: We do what we must. Because. we can. For the good of all of us. Except the ones who are dead. But there's no sense crying Over every mistake, You just keep on trying Till you run out of cake, And the science gets done And you make a neat gun For the people who are Still alive. I'm not even angry... I'm being so sincere right now. Even though you broke my heart, And killed me. And tore me to pieces. And threw every piece. into. a fire. As they burned it hurt because I was so happy for you. Now these points of data Make a beautiful line And we're out of beta We're releasing on time So I'm GLaD I got burned Think of all the things we learned For the people who are Still alive... Go ahead and leave me... I think I'd prefer. to stay. inside. Maybe you'll find someone else To help you? Maybe Black Mesa? That was a joke Haha. Fat Chance. Anyway this cake is great. It's so delicious and moist. Look at me still talking When there's science to do When I look out there It makes me GLaD I'm not you I've experiments to run There is research to be done On the people who are Still alive... And believe me I am Still alive... I'm doing science and I'm Still alive... I feel fantastic and I'm Still alive... While you're dying I'll be Still alive... And when you're dead I will be Still alive. Still alive. Still alive.", "Sing me a song of a lass that is gone. Say, could that lass be I?. Merry of soul, she sailed on a day. Over the sea to Skye. Billow and breeze, islands and seas. Mountains of rain and sun (mountains of rain and sun). All that was good, all that was fair. All that was me is gone. Sing me a song of a lass that is gone. Say, could that lass be I?. Merry of soul, she sailed on a day. Over the sea to Skye. Sing me a song of a lass that is gone. Say, could that lass be I?", "There's something inside you. It's hard to explain. They're talking about you, boy. But you're still the same. There's something inside you. It's hard to explain. They're talking about you, boy. But you're still the same"]))
        
        # Say a random fact
        elif query_compare(["random fact"], query):
            x = randfacts.get_fact()
            speak(x)
        
        # Say a random quote
        elif query_compare(["quote", "wise"], query):
            file = open("quotes.csv")
            csvreader = csv.reader(file)
            header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)
            r = randint(0, len(rows)-1)
            msg = rows[r][1][0:250]
            speak(msg)
        
        # give headlines of top 10 news
        elif query_compare(["news"], query):
            url='https://www.bbc.com/news'
            response = requests.get(url)                
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            unwanted = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch']
            for x in list(dict.fromkeys(headlines))[:10]:
                if x.text.strip() not in unwanted:
                    speak(x.text.strip())
        
        # google things on the internet
        elif query.startswith('search'):
            lookup = query[6:]
            lookup = lookup.strip().replace(" ", '+')
            url = 'https://www.google.com/search?q='
            url_data = url + lookup
            speak(choice(["This is what I found.", "Here is what I got from the web.", "I found these on the internet.", "Perhaps these will help..."]))
            webbrowser.open(url_data)

        # Plays music from youtube by opening it in a browser by saying Play <Name of song>
        elif query.startswith("play"):
            speak(choice(["Sure", "Let's try this", "Playing...", "This is what I found on youtube", "Playing what you want to hear", "check it out"]))
            _thread.start_new_thread(pywhatkit.playonyt, (query[5:],))
        
        # Close all tabs on chrome
        elif query.startswith("close"):
            webbrowser.open('https://google.com')
            keyboard.press_and_release('ctrl+shift+w')

        # tell the weather
        elif query_compare(["weather", "temperature", "rain", "precipitation", "forecast"], query):
            city = "Weehawken"
            url = "https://www.google.com/search?q="+"weather"+city
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            precip = soup.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = str.split('\n')
            sky = data[1]
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text
            pos = strd.find('Wind')
            other_data = strd[pos:]   
            speak(precip)             
            speak("The temperature right now is " + temp)
            speak("The Sky is currently " + sky)
            speak(other_data)

        # calculate and do math
        elif query.startswith("calculate"):
            try:
                equation = query[10:]
                equation = equation.replace('plus', '+')
                equation = equation.replace('minus', '-')
                equation = equation.replace('times', '*')
                equation = equation.replace('divided by', '/')
                speak(eval(equation))
            except Exception as e:
                print(e)
        
        # but you can also open the calculator if need be
        elif query_compare(["open calculator"], query):
            os.system("calc")
            speak("Calculator was opened.")

        # open the clock application
        elif query_compare(["open timer", "open alarm", "open countdown", "open stopwatch", "open clock"], query):
            os.system("explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")
            speak("Clock has been opened.")

        # Start a new command line
        elif query_compare(["open commandline", "open terminal", "open command line"], query):
            os.system("start cmd.exe")
            speak("Terminal was opened.")

        # this functionality allows for opening any apps on your computer. Just make sure you add their full path to their executable to the file apps.txt in this format: AppName->FullPath (Important Note: because of the way the command prompt handle whitespace in names, make sure the full path has quotes in directories or files that have white spaces in them, for example: [path\to\dir name\file.exe] would become [path\to\"dir name"\file.exe]. Look at the apps.txt for examples) Do not put quotes around the full path in general. This will only open a new command prompt.
        elif query.startswith("open "):
            appsText = open("apps.txt", "r")
            for line in appsText:
                line_list = line.split("->")
                name = line_list[0]
                fullpath = line_list[1]
                if name.lower() == query[5:]:
                    os.system("start "+fullpath)
                    appsText.close()
                    speak(name+ " was opened.")
                    break

        # Go to sleep if need be
        elif query_compare(["sleep", "shutdown", "die", "offline", "exit", "quit"], query):
            speak(choice(["naptime", "sleep mode activated", "goodbye", "shutting down", "resting", "hibernating"]))
            playsound("shutdown.wav")
            break

        # Stay quiet and only respond to the "wake up" keyword
        elif query_compare(["quiet", "silence", "silent", "shut up"], query):
            speak(choice(["I will be nice and quiet now.", "i will be silent now.", "okay! I won't say anything.", "Sure, i will be quiet"]))
            nice_and_quiet = True

        # read all memos
        elif query_compare(["read note", "read todo", "read to do", "read memo", "read quick memo", "read quickmemo", "read quick note", "read my note", "read my todo", "read my to do", "read my memo", "read my quick memo", "read my quickmemo", "read my quick note"], query):
            try:
                note_file = open("todo.txt", "r")
                speak("Sure! These are all your notes.")
                for line in note_file:
                    speak(line)
                note_file.close()
            except:
                print("Failed to open todo.txt.")

        # erase all the notes all memos
        elif query_compare(["erase note", "erase todo", "erase to do", "erase memo", "erase quick memo", "erase quickmemo", "erase quick note", "erase my note", "erase my todo", "erase my to do", "erase my memo", "erase my quick memo", "erase my quickmemo", "erase my quick note", "delete note", "delete todo", "delete to do", "delete memo", "delete quick memo", "delete quickmemo", "delete quick note", "delete my note", "delete my todo", "delete my to do", "delete my memo", "delete my quick memo", "delete my quickmemo", "delete my quick note", "forget note", "forget todo", "forget to do", "forget memo", "forget quick memo", "forget quickmemo", "forget quick note", "forget my note", "forget my todo", "forget my to do", "forget my memo", "forget my quick memo", "forget my quickmemo", "forget my quick note"], query):
            os.system("rm todo.txt")
            speak("all notes have been deleted")

        # quick memo functionality
        elif query_compare(["quick memo", "quickmemo", "todo", "to do", "note", "quick note"], query):
            file_note = open("todo.txt", "a")
            speak("Sure! What would you like me to write?")
            query = takeCommand()
            file_note.write(query+"\n")
            speak("noted")
            file_note.close()

        # small talk
        else:
            dataToSend1 = {'botkey': BOTKEY,'input': query}
            response = requests.post('https://devman.kuki.ai/atalk', data=dataToSend1)
            if response.status_code!=200:
                print(response)
                print(response.text)
                speak(IBrain.gpt3_reply(query))
                continue
            jsonResponse = response.json()   
            responses_array = jsonResponse["responses"]
            for reply in responses_array:
                speak(reply.lower().replace('kuki', 'lisa'))

    print("Lisa went to sleep.")