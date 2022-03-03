# Author: Rafael Sanchez
# Desc: GUI of ALIZA
from tkinter import *
from PIL import ImageTk, Image
import os
import pygame
import random
from datetime import datetime
import brain

pygame.mixer.init()
number_of_tracks = 6
rand = random.randint(0, number_of_tracks-1)
pygame.mixer.music.load("track"+str(rand)+".mp3")
pygame.mixer.music.play(-1)

loading=True
ind=0
root = Tk()
root.title('Aliza Chatbot')
root.iconbitmap('z.ico')
root.geometry("900x600")
root.config(cursor="heart")
bgimg=ImageTk.PhotoImage(Image.open("bg.png"))
bg = Label( root, image = bgimg, relief="solid")
bg.place(x = 0, y = 0)
root.resizable(False, False)
e = Entry(root, width=71, borderwidth=5, font=('Courier', 15, 'bold'))
e.place(x=12, y=550)
d3 = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
file = open("chatlogs"+os.sep+"CONVERSATION_"+d3+".txt", "a") 
file.write("-----------| CHAT "+d3+" STARTED |----------------------------------------------\n\n")
def myClick():
    global e
    z_mes=brain.aliza_says(e.get())
    file.write("User: "+e.get()+'\n\n')
    file.write("Aliza: "+z_mes+'\n\n')
    abel.configure(text=z_mes)
    e.delete(0, END)
    

def func(event):
    myClick()
root.bind('<Return>', func)
displayed_message=brain.start()
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
    rand=((rand+1) % number_of_tracks)
    pygame.mixer.music.load("track"+str(rand)+".mp3")
    pygame.mixer.music.play(-1)
musicTurnOff = Button(root, text="TURN OFF", command=turnoff, relief='raised',bg='black', fg="violet", borderwidth=6, font="Courier 12")
musicTurnOff.place(x=12, y=15)
musicTurnOn = Button(root, text=" CHANGE ", command=turnon, relief='raised',bg='black', fg="violet",borderwidth=6, font="Courier 12")
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