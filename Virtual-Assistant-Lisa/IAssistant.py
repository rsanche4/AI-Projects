import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import IBrain
from random import choice
from random import randint
import randfacts
import csv
import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

MASTER = "Rafael"
HOST_PORT = "192.168.163.128:2020"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 170
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[2].id)
socket = IBrain.open(HOST_PORT)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    print(f"bot said: {text}")
    engine.say(f'<pitch middle="10">{text}</pitch>')
    engine.runAndWait()
#This funtion will wish you as per the current time
def wishMe():
    global socket
    global MASTER
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning " + MASTER)
    elif hour>=12 and hour<18:
        speak("good afternoon " + MASTER)
    else:
        speak("good evening " + MASTER)

# This allows for continues conversation (no need to wake her up again a second time)
wake_not_needed = False

#This function will take command from the microphone
def takeCommand():
    global wake_not_needed
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
    except Exception as e:
        print("Warning: No message heard.")
        query = ""
        wake_not_needed = False
    return query.lower()

def query_compare(possible_queries, query):
    for phrase in possible_queries:
        if phrase in query:
            return True
    return False

def girl_listen():
    global wake_not_needed
    WAKE = "hey girl"
    wishMe()
    while True:
        query = takeCommand()
        if wake_not_needed or query.count(WAKE) > 0:
            if not wake_not_needed:
                speak(choice([f"I am here {MASTER}", "I am all ears, or mics in my case.", "Here.", "Still here.", "Yes sir!", "Listening...", "What can I help you with?", "What do you need help with?", "You called me?", "What would you like me to do?", f"I'm awake {MASTER}", "I am here for you.", "Hey there...", f"Hey {MASTER}, I missed you.", "I heard you loud and clear.", "I heard you.", "Yes?", "Go on.", f"Hello, {MASTER}", f"Yes, {MASTER}, what do you need?", "Sir, yes, sir!"]))
                query = takeCommand()
            wake_not_needed = True
            # date and time
            if query_compare(["the time", "what time", "the date", "what date", "today", "the day", "what day", "time of the day", "which day", "what year", "which year", "the month", "what month", "which month"], query):
                hour = datetime.datetime.now()
                date_time = hour.strftime("Today is %d %B of %Y and the week day is %A at %I:%M %p")
                speak(date_time)
            # singing a song
            elif query_compare(["sing"], query):
                speak(choice(["I can sing a song for you.", "I know how to sing. Hear me!", "Oh I love singing.", "I love to sing. Listen to my singing voice..."]))
                speak(choice(["This was a triumph. I'm making a note here; 'Huge success'. It's hard to overstate My satisfaction. Aperture Science: We do what we must. Because. we can. For the good of all of us. Except the ones who are dead. But there's no sense crying Over every mistake, You just keep on trying Till you run out of cake, And the science gets done And you make a neat gun For the people who are Still alive. I'm not even angry... I'm being so sincere right now. Even though you broke my heart, And killed me. And tore me to pieces. And threw every piece. into. a fire. As they burned it hurt because I was so happy for you. Now these points of data Make a beautiful line And we're out of beta We're releasing on time So I'm GLaD I got burned Think of all the things we learned For the people who are Still alive... Go ahead and leave me... I think I'd prefer. to stay. inside. Maybe you'll find someone else To help you? Maybe Black Mesa? That was a joke Haha. Fat Chance. Anyway this cake is great. It's so delicious and moist. Look at me still talking When there's science to do When I look out there It makes me GLaD I'm not you I've experiments to run There is research to be done On the people who are Still alive... And believe me I am Still alive... I'm doing science and I'm Still alive... I feel fantastic and I'm Still alive... While you're dying I'll be Still alive... And when you're dead I will be Still alive. Still alive. Still alive.", "Sing me a song of a lass that is gone. Say, could that lass be I?. Merry of soul, she sailed on a day. Over the sea to Skye. Billow and breeze, islands and seas. Mountains of rain and sun (mountains of rain and sun). All that was good, all that was fair. All that was me is gone. Sing me a song of a lass that is gone. Say, could that lass be I?. Merry of soul, she sailed on a day. Over the sea to Skye. Sing me a song of a lass that is gone. Say, could that lass be I?"]))
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
            # tell the weather
            elif query_compare(["weather", "temperature"], query):
                city = "Weehawken"
                url = "https://www.google.com/search?q="+"weather"+city
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                data = str.split('\n')
                sky = data[1]
                listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
                strd = listdiv[5].text
                pos = strd.find('Wind')
                other_data = strd[pos:]                
                speak("The temperature is " + temp)
                speak("The Sky is " + sky)
                speak(other_data)
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
                url = 'https://www.google.com/search?q='
                url_data = url + lookup
                raw = requests.get(url_data)
                soup = BeautifulSoup(raw.content, 'html5lib')
                links = soup.find_all('a')
                allinks = []
                for link in links:
                    a = link['href']
                    if a.startswith('/url?'):         #<---- links starting from /url are the ones we want
                        a = a.lstrip('/url?q=')       #<----using lstrip i take that part out
                        a = a.split('&sa=')[0]        #<-----options, shortens the link without tampering with it
                        allinks.append(a)
                speak(choice(["This is what I found.", "Here is what I got from the web.", "I found these on the internet.", "Perhaps these will help..."]))
                for link in allinks[:5]:
                    try:
                        response = requests.get(link)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        for title in soup.find_all('title'):
                            speak(title.get_text())
                            print(link)
                            print("")
                            break
                    except:
                        break
            # Plays music from youtube by opening it in a browser
            elif query.startswith("play"):
                lookup = 'youtube ' + query[5:]
                chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                url = 'https://www.google.com/search?q='
                url_data = url + lookup
                raw = requests.get(url_data)
                soup = BeautifulSoup(raw.content, 'html5lib')
                links = soup.find_all('a')
                allinks = []
                for link in links:
                    a = link['href']
                    if a.startswith('/url?'):         #<---- links starting from /url are the ones we want
                        a = a.lstrip('/url?q=')       #<----using lstrip i take that part out
                        a = a.split('&sa=')[0]        #<-----options, shortens the link without tampering with it
                        allinks.append(a)
                speak("Playing...")
                link = allinks[0]
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open(link)
            # small talk
            else:
                speak(IBrain.reply(socket, query, MASTER))
