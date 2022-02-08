# Author: Rafael Sanchez
# Desc: The GUI and part of the Brain of Zoey
from tkinter import *
from PIL import ImageTk, Image
import os
import aiml
import pygame
import random
import getpass
from datetime import datetime
from translate import Translator
from googlesearch import search
import webbrowser
def calcut(m):
    if "+" in m:
        l=m.split('+')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1+n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "*" in m:
        l=m.split('*')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1*n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "-" in m:
        l=m.split('-')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1-n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "/" in m:
        l=m.split('/')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                if n2==0.0:
                    return "Can't divide by zero... I think."  
                else:
                    return str(n1/n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
kernel = aiml.Kernel()
if os.path.isfile("brain"+os.sep+"zbrain.brn"):
    kernel.bootstrap(brainFile = "brain"+os.sep+"zbrain.brn")
else:
    kernel.bootstrap(learnFiles = "brain"+os.sep+"*.aiml")
    kernel.saveBrain("brain"+os.sep+"zbrain.brn")
user_name = ""
if os.path.isfile("brain"+os.sep+"username.txt"):
    name_file = open("brain"+os.sep+"username.txt", 'r')
    user_name = name_file.read()
    name_file.close()
else:
    user_name = input("What would you like Zoey to call you? Enter your name: ")
    name_file = open("brain"+os.sep+"username.txt", 'w')
    name_file.write(user_name)
    name_file.close()
pygame.mixer.init()
number_of_tracks = 6
rand = random.randint(0, number_of_tracks-1)
pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
pygame.mixer.music.play(-1)
def zoey_says(m, kernel):
    global user_name
    global number_of_tracks
    global rand
    m=m.replace('?', '')
    m=m.replace('!', '')
    m=m.replace(',', '')
    m=m.replace('.', '')
    m=m.strip() 
    if user_name.lower() in m.lower():
        a=["That's your name.", "That's you!", "I know that's your name."]
        return random.choice(a)
    elif 'change my name' in m.lower():
        return "To change the way I call you, you can edit the file username.txt and write your new name there."
    elif 'who am i' in m.lower():
        return user_name+"."
    elif 'can you tell the time' in m.lower() or 'tell me the time' in m.lower() or 'what time is it' in m.lower() or 'what is the time' in m.lower() or 'tell me the date' in m.lower() or 'what date is today' in m.lower() or "what's the date" in m.lower() or "what day is today" in m.lower() or "what is today's date" in m.lower() or "what's today's date" in m.lower() or "do you know the time" in m.lower():
        da = datetime.now().strftime("Today is: %d/%m/%Y. The time is %H:%M:%S.")
        return da
    elif "what" in m.lower() or "when" in m.lower() or "why" in m.lower() or "which" in m.lower() or "who" in m.lower()  or "how" in m.lower() or "whose" in m.lower() or "whom" in m.lower() or "define" in m.lower() or "definition of" in m.lower() or "meaning of" in m.lower():
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
    elif m.lower()=='hello' or m.lower()=='hi':
        greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA."]
        return random.choice(greetings)
    elif m.lower()=='goodbye' or m.lower()=='bye' or m.lower()=='bye bye' or m.lower()=='take care' or m.lower()=='see you later' or m.lower()=='catch you later' or m.lower()=='talk to you later'or m.lower()=='until next time' or m.lower()=='see ya' or m.lower()=='peace out' or m.lower()=='have a good day' or m.lower()=='have a nice day':
        leaving=["Nice talking to you!", "I'll be here when you decide to launch me again :)", "See ya.", "Bye bye!"]
        return random.choice(leaving)
    elif m.lower()=='alright' or m.lower()=='ok' or m.lower()=='got it' or m.lower()=='yeah' or m.lower()=='lol' or m.lower()=='cool' or m.lower()=='sure' or m.lower()=='yup' or m.lower()=='yes':
        sure=["Alright then.", "OK.", "Yeah.", "Cool.", "Alright.", "Nice."]
        return random.choice(sure)
    elif 'shell command' in m.lower():
        os.system(m[14:])
        execut=["Command executed.", "SUCCESS.", "No errors when executing command.", "Your terminal should be running now."]
        return random.choice(execut)
    elif '+' in m or "-" in m or "/" in m or "*" in m:
        return calcut(m)
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
        if r=="":
            idontknow=['Let me think about it.', 'Have you tried a web search?', "I haven't heard of that.", "I need time to formulate the reply.", "I'll ask around and get back to you.", "I have to think about that one for a while.", "I would look into the web for that knowledge.", "I don't know.", "That's not something I think about all the time.", "I don't know anything about that.", "Check back later and see if I learn the answer to that one.", "Are you testing me?", "Ask someone about it.", "I have no idea how to reply."]
            return random.choice(idontknow)
        if random.randint(0,20)==0:
            if random.randint(0,1)==0:
                r=user_name+', '+r[0].lower()+r[1:]
            else:
                r[-1]=','
                r=r+' '+user_name+'.'
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
file = open("brain"+os.sep+"chatlogs"+os.sep+"CONVERSATION_"+d3+".txt", "a") 
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