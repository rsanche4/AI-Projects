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
kernel.learn("brain"+os.sep+"pinafl"+os.sep+"*.aiml")

pygame.mixer.init()
number_of_tracks = 4
rand = random.randint(1, number_of_tracks)
if rand==1:
    pygame.mixer.music.load("gui"+os.sep+"track1.mp3")
    pygame.mixer.music.play(-1)
elif rand==2:
    pygame.mixer.music.load("gui"+os.sep+"track2.mp3")
    pygame.mixer.music.play(-1)
elif rand==3:
    pygame.mixer.music.load("gui"+os.sep+"track3.mp3")
    pygame.mixer.music.play(-1)
elif rand==4:
    pygame.mixer.music.load("gui"+os.sep+"track4.mp3")
    pygame.mixer.music.play(-1)

def pina_says(m, kernel):
    
    dictionary=PyDictionary()
    if ("what is" in m.lower() or "define" in m.lower() or "definition of" in m.lower() or "meaning of" in m.lower()) and ('rafael sanchez' not in m.lower() and 'what is your' not in m.lower()):
        r=dictionary.meaning(m.split()[-1])
        if dictionary.meaning(m.split()[-1],True) is None:
            return "uuhhh... I don't know."
        g=list(r.values())[0][0]
        return g.capitalize()
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
            return "Pina: If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
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
                    return "Pina: Can't divide by zero... I think."  
                else:
                    return str(n1/n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    else:
        r=kernel.respond(m)
        if 'Nameless' in r:
            r = r.replace('Nameless', 'Pina')
        return r

loading=True
ind=0

root = Tk()
root.title('Pinabot Ver 1.0')
root.iconbitmap('gui'+os.sep+'icon.ico')
root.geometry("570x460")
root.resizable(False, False)
root.configure(background='#d0f8f7')


e = Entry(root, width=40, borderwidth=5)
e.place(x=5, y=5)

d3 = datetime.now().strftime("%d%m%Y%H%M%S")
file = open("brain"+os.sep+"memory"+os.sep+"chatlog_"+d3+".txt", "a") 

def myClick():
    global e
    global kernel
    pina_mes=pina_says(e.get(), kernel)
    cutoff=408
    file.write(getpass.getuser()+": "+e.get()+'\n')
    file.write("Pina: "+pina_mes[0:cutoff]+'\n')
    abel.configure(text=pina_mes[0:cutoff])
    abel.place(x=8, y=90)
    e.delete(0, END)


def func(event):
    myClick()
root.bind('<Return>', func)
abel = Label(root, text="", wraplength=240, font="Courier 13", fg="#ff60a9", borderwidth=3, relief="raised")
myButton = Button(root, text="Send message!", padx=80, pady=2, command= lambda: myClick(), bg="#fcd6e8", font="Courier 7")
myButton.place(x=10, y=38)


my_img1 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame05.png"))
my_img2 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame06.png"))
my_img3 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame07.png"))
my_img4 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame08.png"))
my_img5 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame09.png"))
my_img6 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame10.png"))
my_img7 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame11.png"))
my_img8 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame12.png"))
my_img9 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame13.png"))
my_img10 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame14.png"))
my_img11 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame15.png"))
my_img12 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame16.png"))
my_img13 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame17.png"))
my_img14 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame18.png"))
my_img15 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame19.png"))
my_img16 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame20.png"))
my_img17 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame21.png"))

my_img100 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame00.png"))
my_img110 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame01.png"))
my_img120 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame02.png"))
my_img130 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame03.png"))
my_img140 = ImageTk.PhotoImage(Image.open("gui"+os.sep+"gui_frame04.png"))


img_l = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12, my_img13, my_img14, my_img15, my_img16, my_img17]

sprite_l = [my_img100, my_img110, my_img120, my_img130, my_img140, my_img130, my_img120, my_img110]


def change_image(label, imagelist, nextindex, time_to_wait, spritelist):
    global loading
    label.place_forget()
    if not loading:
        label = Label(image=spritelist[nextindex], borderwidth=3, relief="raised")
    elif loading:
        label = Label(image=imagelist[nextindex])    
    label.place(x=260, y=2)
    if not loading:
        root.after(time_to_wait, lambda: change_image(label, imagelist, (nextindex+1) % len(spritelist), 250, spritelist))
    elif loading and (nextindex != len(imagelist)-1):
        root.after(time_to_wait, lambda: change_image(label, imagelist, (nextindex+1), 50, spritelist))
    elif nextindex == len(imagelist)-1:
        label.place_forget()
        loading = False
        change_image(label, imagelist, 0, time_to_wait, spritelist)

myLabel = Label(image=img_l[ind])
myLabel.place(x=260, y=2)

change_image(myLabel, img_l, ind, 1000, sprite_l)

def on_closing():
    file.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()