# Author: Rafael Sanchez
# Desc: The GUI of Zoey

from tkinter import *
from PIL import ImageTk, Image
import os
from PyDictionary import PyDictionary
import aiml
import pygame
import random
import getpass
from datetime import datetime
import calculator
from translate import Translator
from googlesearch import search
import webbrowser
import json

kernel = aiml.Kernel()

# if os.path.isfile("brain"+os.sep+"zbrain.brn"):
#     kernel.bootstrap(brainFile = "brain"+os.sep+"zbrain.brn")
# else:
#     kernel.bootstrap(learnFiles = "brain"+os.sep+"aiml"+os.sep+"MASTER_AIML_ALICE.aiml")
#     kernel.saveBrain("brain"+os.sep+"zbrain.brn")

#kernel.learn("brain"+os.sep+"aiml"+os.sep+"3-zoeyfl"+os.sep+"helloz.aiml")
# kernel.learn("brain"+os.sep+"aiml"+os.sep+"testing.aiml")
kernel.learn("brain"+os.sep+"*.aiml")

# x="************************************************************************"
# b="..%%.......%%%%....%%%%...%%%%%...%%%%%%..%%..%%...%%%%................."
# c="..%%......%%..%%..%%..%%..%%..%%....%%....%%%.%%..%%...................."
# d="..%%......%%..%%..%%%%%%..%%..%%....%%....%%.%%%..%%.%%%................"
# e="..%%......%%..%%..%%..%%..%%..%%....%%....%%..%%..%%..%%................"
# f="..%%%%%%...%%%%...%%..%%..%%%%%...%%%%%%..%%..%%...%%%%................."
# p="........................................................................"
# h="************************************************************************"
# for i in range(1, 5):
#     if i==4:
#         os.system("clear")
#         break
#     os.system("clear")
#     os.system("echo "+ x[0:i*21])
#     os.system("echo "+ b[0:i*21])
#     os.system("echo "+ c[0:i*21])
#     os.system("echo "+ d[0:i*21])
#     os.system("echo "+ e[0:i*21])
#     os.system("echo "+ f[0:i*21])
#     os.system("echo "+ p[0:i*21])
#     os.system("echo "+ h[0:i*21])
    

pygame.mixer.init()
number_of_tracks = 6
rand = random.randint(0, number_of_tracks-1)
pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
pygame.mixer.music.play(-1)

def zoey_says(m, kernel):
    global number_of_tracks
    global rand
    dictionary=PyDictionary()
    m=m.replace('?', '')
    m=m.replace('!', '')
    m=m.replace(',', '')
    m=m.replace('.', '')
    m=m.strip()
    if 'can you tell the time' in m.lower() or 'tell me the time' in m.lower() or 'what time is it' in m.lower() or 'what is the time' in m.lower() or 'tell me the date' in m.lower() or 'what date is today' in m.lower() or "what's the date" in m.lower() or "what day is today" in m.lower()or "what is today's date" in m.lower() or "what's today's date" in m.lower():
        da = datetime.now().strftime("Today is: %d/%m/%Y. The time is %H:%M:%S.")
        return da
    elif ("define" in m.lower() or "definition of" in m.lower() or "meaning of" in m.lower()):
        r=dictionary.meaning(m.split()[-1])
        if dictionary.meaning(m.split()[-1],True) is None:
            return "I don't know... sorry."
        a=list(r.values())
        g=a[0][0]
        return g[0].upper()+g[1:]+"."
    elif "what" in m.lower() or "when" in m.lower() or "why" in m.lower() or "which" in m.lower() or "who" in m.lower() or "how" in m.lower() or "whose" in m.lower() or "whom" in m.lower():
        query=m+"+ wikipedia"
        search(query)
        url_list=[]
        for j in search(query):
            if "wikipedia.org" not in j:
                continue
            url_list=url_list+[j]
        url = random.choice(url_list)
        webbrowser.open_new(url)
        notsure=["I'm not sure. Here is what I found online...", "I might just look that up. Here is what I found.", "I searched that question and this is the result."]
        return random.choice(notsure)
    elif m.lower()=='goodbye' or m.lower()=='bye' or m.lower()=='bye bye' or m.lower()=='take care' or m.lower()=='see you later' or m.lower()=='catch you later' or m.lower()=='talk to you later'or m.lower()=='until next time' or m.lower()=='see ya' or m.lower()=='peace out' or m.lower()=='have a good day' or m.lower()=='have a nice day':
        leaving=["Nice talking to you!", "I'll be here when you decide to launch me again :)", "See ya.", "Bye bye!"]
        return random.choice(leaving)
    elif m.lower()=='alright' or m.lower()=='ok' or m.lower()=='got it':
        sure=["Alright then.", "OK.", "Yeah.", "Cool."]
        return random.choice(sure)
    elif (m.split()[0].lower()=='do' or m.split()[0].lower()=='are' or m.split()[0].lower()=='is' or m.split()[0].lower()=='does') and (not 'you' in m.lower() or not 'I' in m.lower() or not 'they' in m.lower() or not 'his' in m.lower() or not 'her' in m.lower() or not 'my' in m.lower() or not 'their' in m.lower() or not 'its' in m.lower() or not 'it' in m.lower() or not 'she' in m.lower() or not 'he' in m.lower() or not 'your' in m.lower()):
        with open('brain'+os.sep+'data.json') as f:
            data = json.load(f)
        print(data)

        return "TESTING DATA"
    elif 'shell command' in m.lower():
        os.system(m[14:])
        execut=["Command executed.", "SUCCESS.", "No errors when executing command.", "Your terminal should be running now."]
        return random.choice(execut)
    elif '+' in m or "-" in m or "/" in m or "*" in m:
        return calculator.calcut(m)
    elif ':)'== m:
        return ';)'
    elif ';)'== m:
        return ':)'
    elif 'switch music' in m.lower() or 'switch song' in m.lower() or 'change song' in m.lower() or 'change music' in m.lower() or 'switch the music' in m.lower() or 'switch the song' in m.lower() or 'change the song' in m.lower() or 'change the music' in m.lower():
        pygame.mixer.stop()
        rand = (rand+1) % number_of_tracks
        pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
        pygame.mixer.music.play(-1)
        messages_song=["Changing music... there you go.", "Music changed as requested.", "Yeah... that one was getting old.", "You know, I hear these tracks in my universe everyday. Sometimes, I feel melancholic.", "Song changed!", "Digital Universe, may you please change the song? Thank you."]
        return random.choice(messages_song)
    elif 'translate' in m.lower():
        if m[-1]=='.':
            m=m.replace(".","")
        mes_l = m.split()
        if len(mes_l)!=4 or mes_l[0].lower()!='translate' or mes_l[2].lower()!='to':
            return "Are you trying to translate something? To translate you should use this format: Translate <english word> to <language> (Ex: Translate hello to spanish)"
        langl=['spanish','german','italian','french','portuguese']
        if mes_l[3] not in langl:
            return "I can't translate that. I only know Spanish, German, Italian, French, and Portuguese. Though I am not too comfortable speaking it."
        translator= Translator(from_lang="english",to_lang=mes_l[3])
        translation = translator.translate(mes_l[1])
        finish_remark=["I could be wrong though.", "I'd check that translation with a more reliable translator.","I'm not too good at translations.", "Honestly, I don't know if I'm right."]
        start_remark=["Perhaps: ", "Something like this: ", "Problably this: ", "I think you say it like this: ", "I'm sure is this: ", "Maybe... this: "]
        return random.choice(start_remark)+translation+". "+random.choice(finish_remark)
    else:
        r=kernel.respond(m)
        return r

loading=True
ind=0

root = Tk()
root.title('Zoey Chatbot')
root.iconbitmap('gui'+os.sep+'z.ico')
root.geometry("900x600")
bgimg=ImageTk.PhotoImage(Image.open("gui"+os.sep+"bg.png"))
bg = Label( root, image = bgimg, relief="solid")
bg.place(x = 0, y = 0)
root.resizable(False, False)

e = Entry(root, width=61, borderwidth=8, font=('Courier', 18, 'bold'), bg="black",fg="red")
e.place(x=12, y=540)

d3 = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
file = open("brain"+os.sep+"chatlogs"+os.sep+"conversation_"+d3+".txt", "a") 
file.write("-----------| CHAT "+d3+" STARTED |----------------------------------------------\n\n")

def myClick():
    global e
    global kernel
    z_mes=zoey_says(e.get(), kernel)
    file.write(getpass.getuser()+": "+e.get()+'\n\n')
    file.write("Zoey: "+z_mes+'\n\n')
    abel.configure(text=z_mes)
    e.delete(0, END)

def func(event):
    myClick()
root.bind('<Return>', func)

greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA."]
displayed_message=random.choice(greetings)
abel = Label(root,width=24,height=16, text=displayed_message,justify=LEFT,anchor=NW, wraplength=340, font=('Courier', 18, 'bold'), bg="black",fg="red", borderwidth=10, relief="ridge")
abel.place(x=530, y=80)
file.write("Zoey: "+displayed_message+"\n\n")

zo = Label(root,text="ZOEY CHATBOT", width=17,font=('Courier', 23, 'bold'),bg='black',fg="violet",borderwidth=10,relief="ridge")
zo.place(x=534, y=20)

typehere = Label(root,text="Type your message here:",font=('Courier', 13, 'bold'),bg='black',fg="violet",borderwidth=3,relief="ridge")
typehere.place(x=13, y=510)

def turnoff():
    pygame.mixer.music.stop()

def turnon():
    global number_of_tracks
    global rand
    pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
    pygame.mixer.music.play(-1)

musicTurnOff = Button(root, text="TURN OFF", command=turnoff, relief='raised',bg='black', fg="violet", borderwidth=6, font="Courier 12")
musicTurnOff.place(x=12, y=15)
musicTurnOn = Button(root, text="TURN  ON", command=turnon, relief='raised',bg='black', fg="violet",borderwidth=6, font="Courier 12")
musicTurnOn.place(x=12, y=55)

def on_closing():
    file.write("-----------| CHAT "+d3+" ENDED | CONVERSATION ARCHIVED SUCCESSFULLY |-----------\n")
    file.close()
    root.destroy()

def endit(event):
    on_closing()
root.bind('<Escape>', endit)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()