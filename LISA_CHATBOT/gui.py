# Author: Rafael Sanchez
# Desc: GUI of Lisa
from tkinter import *
from PIL import ImageTk, Image
import pygame
import random
import json
import socket
import gpt3
host_port = input("Let's connect to the server. Input the IP Address and port (Ex: 192.168.163.128:2020): ")
hp_list = host_port.split(':')
HOST, PORT = hp_list[0], int(hp_list[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("What should the bot call you? ")
sock.connect((HOST, PORT))
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
#root.geometry("900x600")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry(str(screen_width-150)+"x"+str(screen_height-150))
root.attributes('-fullscreen',True)
root.configure(background='black')
root.config(cursor="heart")
offset_left_w=450
offset_up_h=300
bgimg=ImageTk.PhotoImage(Image.open("bg.png"))
bg = Label( root, image = bgimg, relief="solid")
bg.place(x = 0+int((screen_width/2)-offset_left_w), y = 0+int((screen_height/2)-offset_up_h))
root.resizable(True, True)
e = Entry(root, width=71, borderwidth=5, font=('Courier', 15, 'bold'))
e.place(x=12+int((screen_width/2)-offset_left_w), y=550+int((screen_height/2)-offset_up_h))
def print_slow(widget: Label, text, delay, index=1, start_index=0):
    widget.config(text=text[start_index: index])
    index += 1
    return root.after(delay, print_slow, widget, text, delay, index) if index <= len(text) else None
def myClick():
    z_mes="I don't know."
    if random.randint(0, 2)==0:
        dataJson = {"username":"localuser","message": e.get(), "vars": {"name": name}}
        data = json.dumps(dataJson)
        data = str(data)+"\n"+"__END__"
        sock.sendall(bytes(data,encoding="utf-8"))
        received = sock.recv(4096)
        received = received.decode("utf-8")
        received = received.replace("__END__", "")
        parsed_data = json.loads(received)
        answer = parsed_data["reply"].upper()
        if answer.strip()=="}" or answer.strip()=="":
            z_mes=gpt3.gpt3_reply(e.get()).upper()
        else:
            z_mes=parsed_data["reply"].upper()
    else:
        z_mes=gpt3.gpt3_reply(e.get()).upper()
    e.delete(0, END)
    print_slow(abel, z_mes.upper(), 50)
def func(event):
    myClick()
root.bind('<Return>', func)
displayed_message="HEY THERE :)"
abel = Label(root,width=24,height=16, text=displayed_message,justify=LEFT,anchor=NW, wraplength=340, font=('Courier', 18, 'bold'), bg="black",fg="green", borderwidth=10, relief="ridge")
abel.place(x=530+int((screen_width/2)-offset_left_w), y=80+int((screen_height/2)-offset_up_h))
zo = Label(root,text="LISA CHATBOT", width=17,font=('Courier', 23, 'bold'),bg='black',fg="violet",borderwidth=10,relief="ridge")
zo.place(x=534+int((screen_width/2)-offset_left_w), y=20+int((screen_height/2)-offset_up_h))
typehere = Label(root,text="Type your message here:",font=('Courier', 13, 'bold'),bg='black',fg="violet",borderwidth=3,relief="ridge")
typehere.place(x=13+int((screen_width/2)-offset_left_w), y=520+int((screen_height/2)-offset_up_h))
def turnoff():
    pygame.mixer.music.stop()
def turnon():
    global number_of_tracks
    global rand
    rand=((rand+1) % number_of_tracks)
    pygame.mixer.music.load("track"+str(rand)+".mp3")
    pygame.mixer.music.play(-1)
musicTurnOff = Button(root, text="TURN OFF", command=turnoff, relief='raised',bg='black', fg="violet", borderwidth=6, font="Courier 12")
musicTurnOff.place(x=12+int((screen_width/2)-offset_left_w), y=15+int((screen_height/2)-offset_up_h))
musicTurnOn = Button(root, text=" CHANGE ", command=turnon, relief='raised',bg='black', fg="violet",borderwidth=6, font="Courier 12")
musicTurnOn.place(x=12+int((screen_width/2)-offset_left_w), y=55+int((screen_height/2)-offset_up_h))
def on_closing():
    root.destroy()
    sock.close()
def endit(event):
    on_closing()
root.bind('<Escape>', endit)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()