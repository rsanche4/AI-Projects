# Author: Rafael Sanchez
# Desc: Brain of Aliza + GUI
import json
from tkinter import *
from PIL import ImageTk, Image
import os
import pygame
import random
from datetime import datetime
from translate import Translator
import fnmatch
from textblob import TextBlob
def match(text, pattern):
    if fnmatch.fnmatch(text, pattern) or fnmatch.fnmatch(text, pattern+" *") or fnmatch.fnmatch(text, "* "+pattern) or fnmatch.fnmatch(text, "* "+pattern+" *"):
        return True
    else:
        return False
def turn_loweri_toI(m):
    m_list=m.split()
    m_list.insert(0, " ")
    for i in range(1, len(m_list)):
        if m_list[i]=="i":
            m_list[i]="I"
    m=" ".join(m_list)
    m=m.strip()
    return m
def chatbot(m):
    rand=random.randint(0, 7)
    if rand==0:
        m=turn_loweri_toI(m)
        if match(m, "I am"):
            m=m.replace('I am', 'YOU ARE')
        elif match(m, 'I'):
            m=m.replace('I', 'YOU')
        if match(m, "you are"):
            m=m.replace('you are', 'I AM')     
        elif match(m, "you"):
            m=m.replace('you', 'I')
        if match(m, "me"):
            m=m.replace('me', 'YOU')
        m_list=m.split()
        q=["Why do you think ", "Why do you say that ", "What makes you say that ", "Any reason why you think ", "Could you explain why "]
        m=" ".join(m_list)
        m=m.strip()
        m=m.lower()
        m=turn_loweri_toI(m)
        return random.choice(q)+m+"?"
    else:
        m=turn_loweri_toI(m)
        # go through json file and return the answers
        with open('data'+os.sep+'brain.json', 'r') as f:
            data = json.load(f)
        for key, value in data.items():
            for patterns, replies in value.items():
                if match(m, str(patterns)):
                    return random.choice(replies)
        return ""

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

pygame.mixer.init()
number_of_tracks = 6
rand = random.randint(0, number_of_tracks-1)
pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
pygame.mixer.music.play(-1)
warns = 0
def aliza_says(m):
    global warns
    global number_of_tracks
    global rand
    if ">" in m:
        m_list=m.split(">")
        for i in range(len(m_list)):
            m_list[i]=m_list[i].strip()
        m_list[0]=m_list[0].replace('?', '')
        m_list[0]=m_list[0].replace('!', '')
        m_list[0]=m_list[0].replace(',', '')
        m_list[0]=m_list[0].replace('.', '')
        m_list[0]=m_list[0].lower()
        mypattern = str(m_list[0])
        with open('data'+os.sep+'brain.json', 'r+') as f:
            data = json.load(f)
            string = '{"'+str(m_list[0])+'": ['
            for i in range(1, len(m_list)):
                string= string+'"'+str(m_list[i])
                if i!=len(m_list)-1:
                    string=string+'", '
            string = string+'"]}'
            new_stuff=json.loads(string)
            data["others"].update(new_stuff)
            f.seek(0)
            json.dump(data, f, indent = 3)
        learn=["Fact learned.", "I will remember that.", "Ok, I will make sure to remember that.", "Got it!", "Fact was saved to my brain.", "One new fact a day keeps... the mindless chatbot at bay?", "Parsed successfully.", "Ok ok...", "Learning... learning..."]
        return random.choice(learn)
    
    m=m.replace('?', '')
    m=m.replace('!', '')
    m=m.replace(',', '')
    m=m.replace('.', '')
    m=m.strip() 
    m=m.lower()
    if 'can you tell the time' in m or 'tell me the time' in m or 'what time is it' in m or 'what is the time' in m or 'tell me the date' in m or 'what date is today' in m or "what's the date" in m or "what day is today" in m or "what is today's date" in m or "what's today's date" in m or "do you know the time" in m:
        da = datetime.now().strftime("Today is: %d/%m/%Y. The time is %H:%M:%S.")
        return da
    elif '+' in m or "-" in m or "/" in m or "*" in m:
        return calcut(m)
    elif 'switch music' in m or 'switch song' in m or 'change song' in m or 'change music' in m or 'switch the music' in m or 'switch the song' in m or 'change the song' in m or 'change the music' in m:
        pygame.mixer.stop()
        rand = (rand+1) % number_of_tracks
        pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
        pygame.mixer.music.play(-1)
        messages_song=["Changing music... there you go.", "Music changed as requested.", "Yeah... that one was getting old.", "You know, I hear these tracks in my universe everyday. Sometimes, I feel melancholic.", "Song changed!", "Digital Universe, may you please change the song? Thank you.", "These songs go on and on and on and on...", "If you get tired of the music you can always turn it off!"]
        return random.choice(messages_song)
    elif 'translate' in m:
        mes_l = m.split()
        if len(mes_l)!=4 or mes_l[0].lower()!='translate' or mes_l[2].lower()!='to':
            return "Are you trying to translate something? To translate you should use this format: Translate <english word> to <language>. I can only translate to Spanish, German, Italian, French, and Portuguese."
        langl=['spanish','german','italian','french','portuguese']
        if mes_l[3] not in langl:
            return "I can't translate that. I only know Spanish, German, Italian, French, and Portuguese. Though I am not too comfortable speaking it."
        translator= Translator(from_lang="english",to_lang=mes_l[3].lower())
        translation = translator.translate(mes_l[1])
        finish_remark=["I could be wrong though.", "I'd check that translation with a more reliable translator.","I'm not too good at translations.", "Honestly, I don't know if I'm right."]
        start_remark=["Perhaps: ", "Something like this: ", "Problably this: ", "I think you say it like this: ", "I'm sure is this: ", "Maybe... this: "]
        return random.choice(start_remark)+translation+". "+random.choice(finish_remark)
    
    elif m == "":
        noresp=["Are you busy?", "Is anyone there?", "You haven't said anything.", "I'm here waiting for you.", "Get back to me when you are ready.", "Hello?", "I'm waiting.", "Did you mean to send me a blank message?", "Your message was blank."]
        return random.choice(noresp)
    else:
        r=chatbot(m)
        if r=="":
            a=["You say '", "It's true that '", "I didn't know that '", "Well, I like the fact that '", "Who would have thought that '", "You said that '", "Let me think about '", "I haven't heard that '", "I didn't know that '", "I never thought that '"]
            b=["'; I think that's kind of cool.", "'; I find that interesting.", "'; That's interesting.", "'; Sounds peculiar.", "'; That's cool, I guess.", "'; I've never been told that before.", "'; I've never heard of of that.", "'; I don't know anything about that."]
            return random.choice(a)+turn_loweri_toI(m)+random.choice(b) 
        if r=="INSULT DETECTED":
            insult_answers=["That's not nice.", "Oh you are so critical.", "What a pessimist.", "You are an asshole.", "Abusive is a word that describes you.", "That was mean.", "Rude.", "No need to curse.", "That language will get you nowhere.", "You can leave anytime.", "I will not tolarate that language."]
            warns+=1
            return random.choice(insult_answers)+". WARNING "+str(warns)+"."
        elif r=="COMPLEMENT DETECTED":
            nice=["Umm... I am just a chatbot, but thanks! You are looking swell yourself.", "Oh my... did I turn you on?", "You are too.", "Thank you.", "Aww... you make me blush.", "I think you look good too ;)", "My creator never tells me compliments. Thank you!", "You keep telling me that, and I might just fall for you :)", "I... you think... I... do I look good? T-Thanks! I-I think you look good too. There, I said it.", "Thanks :)"]
            return random.choice(nice)
        elif r=="JOKE MODE":
            joke=["Why did the chatbot cross the road? Chatbots can't cross roads, they are called chatbots for a reason. Seriously, this is the worst joke I have been programmed to say."]
            return random.choice(joke)
        elif r=="SALUTE MODE":
            greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA.", "How have you been?", "Thanks for talking to me again...", "You are awesome company ;)", "It's fun talking to you.", "Welcome!"]
            return random.choice(greetings)
        elif r=="END IT":
            leaving=["Nice talking to you!", "I'll be here when you decide to launch me again :)", "See ya.", "Bye bye!", "Take care!", "I'll see you again! Hopefully.", "Over and out.", "Fun conversation.", "As always, thanks for chatting!"]
            return random.choice(leaving)
        elif r=="EMOJI MODE":
            emoj=[":)","B)",";)","8)","XD","X)","XP",":P",":D",";D",";P"]
            return random.choice(emoj)
        return r
loading=True
ind=0
root = Tk()
root.title('Aliza Chatbot')
root.iconbitmap('gui'+os.sep+'z.ico')
root.geometry("900x600")
root.config(cursor="heart")
bgimg=ImageTk.PhotoImage(Image.open("gui"+os.sep+"bg.png"))
bg = Label( root, image = bgimg, relief="solid")
bg.place(x = 0, y = 0)
root.resizable(False, False)
e = Entry(root, width=71, borderwidth=5, font=('Courier', 15, 'bold'), bg="grey")
e.place(x=12, y=550)
d3 = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
file = open("data"+os.sep+"chatlogs"+os.sep+"CONVERSATION_"+d3+".txt", "a") 
file.write("-----------| CHAT "+d3+" STARTED |----------------------------------------------\n\n")
def myClick():
    global warns
    global e
    z_mes=""
    if warns>=3:
        z_mes = "PERMANENT SLEEP MODE ACTIVATED"
    else:
        z_mes=aliza_says(e.get())
    file.write("User: "+e.get()+'\n\n')
    file.write("Aliza: "+z_mes+'\n\n')
    abel.configure(text=z_mes)
    e.delete(0, END)
    

def func(event):
    myClick()
root.bind('<Return>', func)
greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA."]
displayed_message=random.choice(greetings)
abel = Label(root,width=24,height=16, text=displayed_message,justify=LEFT,anchor=NW, wraplength=340, font=('Courier', 18, 'bold'), bg="black",fg="red", borderwidth=10, relief="ridge")
abel.place(x=530, y=80)
file.write("Aliza: "+displayed_message+"\n\n")
zo = Label(root,text="ALIZA CHATBOT", width=17,font=('Courier', 23, 'bold'),bg='black',fg="violet",borderwidth=10,relief="ridge")
zo.place(x=534, y=20)
typehere = Label(root,text="Type your message here:",font=('Courier', 13, 'bold'),bg='black',fg="violet",borderwidth=3,relief="ridge")
typehere.place(x=13, y=520)
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