from tkinter import *
from PIL import ImageTk, Image
import os
from PyDictionary import PyDictionary
import aiml
import pygame
import random
import getpass
from datetime import datetime

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

# if os.path.isfile("bot_brain.brn"):
#     kernel.bootstrap(brainFile = "bot_brain.brn")
# else:
#     kernel.bootstrap(learnFiles = "brain"+os.sep+"alice"+os.sep+"*.aiml")
#     kernel.bootstrap(learnFiles = "brain"+os.sep+"standard"+os.sep+"*.aiml")
#     kernel.saveBrain("bot_brain.brn")


kernel.learn("brain"+os.sep+"alicefl"+os.sep+"*.aiml")
kernel.learn("brain"+os.sep+"standardfl"+os.sep+"*.aiml")
kernel.learn("brain"+os.sep+"mitsukufl"+os.sep+"*.aiml")
kernel.learn("brain"+os.sep+"zoeyfl"+os.sep+"*.aiml")
kernel.learn("brain"+os.sep+"professorfl"+os.sep+"*.aiml")


x="************************************************************************"
b="..%%.......%%%%....%%%%...%%%%%...%%%%%%..%%..%%...%%%%................."
c="..%%......%%..%%..%%..%%..%%..%%....%%....%%%.%%..%%...................."
d="..%%......%%..%%..%%%%%%..%%..%%....%%....%%.%%%..%%.%%%................"
e="..%%......%%..%%..%%..%%..%%..%%....%%....%%..%%..%%..%%................"
f="..%%%%%%...%%%%...%%..%%..%%%%%...%%%%%%..%%..%%...%%%%................."
p="........................................................................"
h="************************************************************************"
for i in range(1, 5):
    if i==4:
        os.system("clear")
        break
    os.system("clear")
    os.system("echo "+ x[0:i*21])
    os.system("echo "+ b[0:i*21])
    os.system("echo "+ c[0:i*21])
    os.system("echo "+ d[0:i*21])
    os.system("echo "+ e[0:i*21])
    os.system("echo "+ f[0:i*21])
    os.system("echo "+ p[0:i*21])
    os.system("echo "+ h[0:i*21])
    

pygame.mixer.init()
number_of_tracks = 8
rand = random.randint(1, number_of_tracks)
pygame.mixer.music.load("gui"+os.sep+"track"+str(rand)+".mp3")
pygame.mixer.music.play(-1)

def zoey_says(m, kernel):
    dictionary=PyDictionary()
    if ("what is" in m.lower() or "define" in m.lower() or "definition of" in m.lower() or "meaning of" in m.lower()) and ('rafael sanchez' not in m.lower() and 'what is your' not in m.lower()):
        r=dictionary.meaning(m.split()[-1])
        if dictionary.meaning(m.split()[-1],True) is None:
            return "I don't know... sorry."
        a=list(r.values())
        g=a[0][0]
        return g[0].upper()+g[1:]+"."
    elif 'shell command' in m.lower():
        os.system(m[14:])
        return "Command executed!" 
    elif "+" in m:
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

d3 = datetime.now().strftime("%d%m%Y%H%M%S")
file = open("brain"+os.sep+"memory"+os.sep+"chatlog_"+d3+".txt", "a") 
file.write("-----------| CHAT "+d3+" STARTED |----------------------------------------------\n\n")

def myClick():
    global e
    global kernel
    z_mes=zoey_says(e.get(), kernel)
    file.write(getpass.getuser()+": "+e.get()+'\n')
    file.write("Zoey: "+z_mes+'\n')
    abel.configure(text=z_mes)
    e.delete(0, END)




def func(event):
    myClick()
root.bind('<Return>', func)

greetings=["Hey there..."]
displayed_message=random.choice(greetings)
abel = Label(root,width=24,height=16, text=displayed_message,justify=LEFT,anchor=NW, wraplength=340, font=('Courier', 18, 'bold'), bg="black",fg="red", borderwidth=10, relief="ridge")
abel.place(x=530, y=80)

zo = Label(root,text="ZOEY CHATBOT", width=17,font=('Courier', 23, 'bold'),bg='black',fg="violet",borderwidth=10,relief="ridge")
zo.place(x=534, y=20)

typehere = Label(root,text="Type your message here:",font=('Courier', 13, 'bold'),bg='black',fg="violet",borderwidth=3,relief="ridge")
typehere.place(x=13, y=510)

def on_closing():
    file.write("\n-----------| CHAT "+d3+" ENDED | CONVERSATION ARCHIVED SUCCESSFULLY |-----------\n")
    file.close()
    root.destroy()

def endit(event):
    on_closing()
root.bind('<Escape>', endit)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()