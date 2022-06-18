# Author: Rafael Sanchez
# Desc: GUI of Lisa
from tkinter import *
from PIL import ImageTk, Image
import pygame

pygame.mixer.init()
sboot = pygame.mixer.Sound("bootup.mp3")
pygame.mixer.Sound.play(sboot)

splash_root = Tk()
splash_root.title("Lisa Chatbot Loading...")
splash_root.geometry("900x600")
splash_label = Label(splash_root)
bgimg=ImageTk.PhotoImage(Image.open("splash_img.png"))
bg = Label(splash_root, image = bgimg)
bg.place(x = 0, y = 0)
splash_root.resizable(False, False)


def main_window():
    splash_root.destroy()
    import gui

splash_root.after(5000, main_window)

splash_root.mainloop()