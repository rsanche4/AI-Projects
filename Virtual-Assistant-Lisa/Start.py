from tkinter import *
from PIL import ImageTk, Image
import _thread
import IAssistant

root = Tk()
target = []
for i in range(30):
    bgimg=ImageTk.PhotoImage(Image.open("resources\\frame_"+str(i)+"_delay-0.07s.png"))
    target.append(bgimg)
root.geometry('250x200')
root.iconbitmap("Icon.ico")
root.configure(bg="WHITE")
root.title("GIRL")
bg = Label( root, image=target[0], relief="solid", borderwidth=0)
bg.place(relx=0.5, rely=0.5, anchor=CENTER)
def countdown(i, widget):
    if i>29:
        i=0
    widget.configure(image=target[i])
    root.after(40, countdown, i+1, widget)

countdown(0, bg) # start count loop.

def on_closing():
    root.destroy()
def endit(event):
    on_closing()
root.bind('<Escape>', endit)
root.protocol("WM_DELETE_WINDOW", on_closing)
_thread.start_new_thread(IAssistant.girl_listen, ())
root.mainloop()