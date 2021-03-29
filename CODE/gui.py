from tkinter import *
import hashlib
import time
import os
import random
import cv2
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter



def browse():
    global filename
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("Text files",
                                                        "*.txt*")))


    label_file_explorer = Label(
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")

    label_file_explorer.configure(text="File Opened: "+filename)
    Label(screen,text = filename).place(x=200,y=200)

    button_exit = Button(
                         text = "Exit",
                         command = exit)


    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x350")
    screen.title("Register")
    global userid
    global stdname
    global path
    global registerid
    global studentname
    global filepath
    
    userid=StringVar()
    stdname=StringVar()
    path=StringVar()

    Label(screen,text="Enter Students Data ").place(x=150,y=50)
    Label(screen,text="").pack()
    Label(screen,text="Resitration Number:").place(x=50,y=100)
    registerid = Entry(screen,textvariable = userid )
    registerid.place(x=200,y=100)
    Label(screen,text="Student Name :").place(x=50,y=150)
    studentname = Entry(screen,textvariable= stdname )
    studentname.place(x=200,y=150)
    Label(screen,text = "Choose Image:").place(x=50,y=200)
    Button(screen,text = "Browse",width="15", command = browse).place(x=200,y=250)

    Button(screen,text = "submit",width="15", command = exit).place(x=50,y=250)
       
    


   

    screen.mainloop()

main_screen()
