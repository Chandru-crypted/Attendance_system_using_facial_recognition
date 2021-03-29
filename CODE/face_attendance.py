from tkinter import *
import os
import cv2
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter

#face_detect packages

from imutils import face_utils
import dlib
import cv2

import face_recognition



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



def send_data():
    

    print(userid.get(),"\n")
    print(stdname.get(),"\n")
    print(filename,"\n")


    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor


    detector = dlib.get_frontal_face_detector()

    # load the input image and convert it to grayscale
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
    rects = detector(gray, 0)

#result list
    res = []

# loop over the face detections
    for (i, rect) in enumerate(rects):
        
    
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            print(i, rect)
	
            # Window name in which image is displayed 
            window_name = 'Image'
	  
            # Start coordinate, here (5, 5) 
            # represents the top left corner of rectangle 
            lis = []
            lis.append(rect.left())
            lis.append(rect.top())
            start_point = tuple(map(int, lis))
	
	  
            # Ending coordinate, here (220, 220) 
            # represents the bottom right corner of rectangle 
            lis = []
            lis.append(rect.right())
            lis.append(rect.bottom())
            end_point = tuple(map(int, lis))

            # Blue color in BGR 
            color = (255, 0, 0) 
	  
            # Line thickness of 2 px 
            thickness = 2
	  
            # Using cv2.rectangle() method 
            # Draw a rectangle with blue line borders of thickness of 2 px 
            # i added this line for cropping the detected image
            crop_img = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
            img = cv2.rectangle(image, start_point, end_point, color, thickness) 

            path="D:\kabil\project\detected faces\img{}.jpg"
            
            status = cv2.imwrite(path.format(i), img)
            status = cv2.imwrite(path.format(i), crop_img)

            res.append(tuple(face_recognition.face_encodings(img)[0]))
           
            

            
    if status:
            print("Image saved sucessful\n")
    else:
            print("Image save failed\n")

  
    

    
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

    Button(screen,text = "submit",width="15", command = send_data).place(x=50,y=250)
    
    


   

    screen.mainloop()

main_screen()
