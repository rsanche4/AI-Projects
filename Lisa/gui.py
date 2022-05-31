# Author: Rafael Sanchez
# Desc: GUI of Lisa
from tkinter import *
from PIL import ImageTk, Image
import pygame
import random
import os
import aiml

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

pygame.mixer.init()
number_of_tracks = 2
rand = random.randint(0, number_of_tracks-1)
pygame.mixer.music.load("track"+str(rand)+".mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

loading=True
ind=0
root = Tk()
root.title('Lisa Chatbot')
root.iconbitmap('z.ico')
root.geometry("900x600")
root.config(cursor="heart")
bgimg=ImageTk.PhotoImage(Image.open("bg.png"))
bg = Label( root, image = bgimg, relief="solid")
bg.place(x = 0, y = 0)
root.resizable(False, False)
e = Entry(root, width=71, borderwidth=5, font=('Courier', 15, 'bold'))
e.place(x=12, y=550)
def myClick():
    global e
    global k
    z_mes=k.respond(e.get())
    e.delete(0, END)
    abel.configure(text=z_mes.upper())
def func(event):
    myClick()
root.bind('<Return>', func)
displayed_message="HEY THERE :)"
abel = Label(root,width=24,height=16, text=displayed_message,justify=LEFT,anchor=NW, wraplength=340, font=('Courier', 18, 'bold'), bg="black",fg="green", borderwidth=10, relief="ridge")
abel.place(x=530, y=80)
zo = Label(root,text="LISA CHATBOT", width=17,font=('Courier', 23, 'bold'),bg='black',fg="violet",borderwidth=10,relief="ridge")
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
    root.destroy()
def endit(event):
    on_closing()
root.bind('<Escape>', endit)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()