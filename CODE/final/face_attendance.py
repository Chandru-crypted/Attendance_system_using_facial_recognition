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
import numpy as np

#database connection
import sqlite3

reslt1 = []
reslt2 = []
    
dbase = sqlite3.connect(r'db/attendance.db')
print ('attendance Database opened')

dbase.execute('''CREATE TABLE IF NOT EXISTS students_record(
    ID CHAR PRIMARY KEY NOT NULL,
    NAME CHAR NOT NULL,
    SUBJECT CHAR NOT NULL,
    ATTENDANCE CHAR NOT NULL)''')

print ('TABLE CREATED')

def read_data(m):
    dbase = sqlite3.connect('STUDENTSDATA.db')
    print ('studentsdata Database opened')
    
    data=dbase.execute(''' SELECT FACE_ARR_0, FACE_ARR_1, FACE_ARR_2, FACE_ARR_3, FACE_ARR_4, FACE_ARR_5, FACE_ARR_6, FACE_ARR_7, FACE_ARR_8, FACE_ARR_9, FACE_ARR_10, FACE_ARR_11, FACE_ARR_12, FACE_ARR_13, FACE_ARR_14, FACE_ARR_15, FACE_ARR_16, FACE_ARR_17, FACE_ARR_18, FACE_ARR_19, FACE_ARR_20, FACE_ARR_21, FACE_ARR_22, FACE_ARR_23, FACE_ARR_24, FACE_ARR_25, FACE_ARR_26, FACE_ARR_27, FACE_ARR_28, FACE_ARR_29, FACE_ARR_30, FACE_ARR_31, FACE_ARR_32, FACE_ARR_33, FACE_ARR_34, FACE_ARR_35, FACE_ARR_36, FACE_ARR_37, FACE_ARR_38, FACE_ARR_39, FACE_ARR_40, FACE_ARR_41, FACE_ARR_42, FACE_ARR_43, FACE_ARR_44, FACE_ARR_45, FACE_ARR_46, FACE_ARR_47, FACE_ARR_48, FACE_ARR_49, FACE_ARR_50, FACE_ARR_51, FACE_ARR_52, FACE_ARR_53, FACE_ARR_54, FACE_ARR_55, FACE_ARR_56, FACE_ARR_57, FACE_ARR_58, FACE_ARR_59, FACE_ARR_60, FACE_ARR_61, FACE_ARR_62, FACE_ARR_63, FACE_ARR_64, FACE_ARR_65, FACE_ARR_66, FACE_ARR_67, FACE_ARR_68, FACE_ARR_69, FACE_ARR_70, FACE_ARR_71, FACE_ARR_72, FACE_ARR_73, FACE_ARR_74, FACE_ARR_75, FACE_ARR_76, FACE_ARR_77, FACE_ARR_78, FACE_ARR_79, FACE_ARR_80, FACE_ARR_81, FACE_ARR_82, FACE_ARR_83, FACE_ARR_84, FACE_ARR_85, FACE_ARR_86, FACE_ARR_87, FACE_ARR_88, FACE_ARR_89, FACE_ARR_90, FACE_ARR_91, FACE_ARR_92, FACE_ARR_93, FACE_ARR_94, FACE_ARR_95, FACE_ARR_96, FACE_ARR_97, FACE_ARR_98, FACE_ARR_99, FACE_ARR_100, FACE_ARR_101, FACE_ARR_102, FACE_ARR_103, FACE_ARR_104, FACE_ARR_105, FACE_ARR_106, FACE_ARR_107, FACE_ARR_108, FACE_ARR_109, FACE_ARR_110, FACE_ARR_111, FACE_ARR_112, FACE_ARR_113, FACE_ARR_114, FACE_ARR_115, FACE_ARR_116, FACE_ARR_117, FACE_ARR_118, FACE_ARR_119, FACE_ARR_120, FACE_ARR_121, FACE_ARR_122, FACE_ARR_123, FACE_ARR_124, FACE_ARR_125, FACE_ARR_126, FACE_ARR_127 FROM students_record ''')
    i=0
    n=0
    j=0
    for record in data:
        reslt2.append(record)
        n=n+1


    '''while(i<n):
        arr1[i]=np.array(reslt1[i])
        i=i+1

    while(j<m):
        arr2[j]=np.array(reslt2[j])
        j=j+1'''

    compare(m,n)


def compare(m,n):

    arr1=np.array(reslt1)
    arr2=np.array(reslt2)
    for i in range(m):
         for j in range(n):
            kencode=arr2[j]
            ukencode=arr1[i]
            results = face_recognition.compare_faces([arr2[j]],arr1[i])
            print(i)
            print(j)
            print(results)
            if results == [True]:
                print("PRESENT\n")
                break
    print(m)
    print(n)

'''
    kencode=arr2[5]
    ukencode=arr1[0]
    results = face_recognition.compare_faces([arr2[5]],arr1[2])
    print(results)
    print(arr2[5])
    print("\n")
    print(arr1[0])

'''
'''
    for i in range(m):
        for j in range(n):
            kencode=arr2[j]
            ukencode=arr1[i]
            results = face_recognition.compare_faces([arr2[j]],arr1[i])
            print(i)
            print(j)
            print(results)
            if results == [True]:
                print("PRESENT\n")
                break

'''
'''
print(m)
print(n)
print(arr2[4])
print(arr1[0])

          
print("\n\n")
print(arr1[0])
print("\n\n")
print(arr2[0])
print(results)
print(m)
print(n)
'''

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
    Label(screen,text = filename).place(x=150,y=100)

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

    m=0
    
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
            res2=face_recognition.face_encodings(img)[0]
            result1=tuple(res2)
            reslt1.append(result1)
            m=m+1
           
            

    if status:
            print("Image saved sucessful\n")
    else:
            print("Image save failed\n")



    read_data(m)
    

    
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

    Label(screen,text="Browse Image to mark attendance ").place(x=100,y=50)
    Label(screen,text="").pack()
    #Label(screen,text="Resitration Number:").place(x=50,y=100)
    #registerid = Entry(screen,textvariable = userid )
    #registerid.place(x=200,y=100)
    #Label(screen,text="Student Name :").place(x=50,y=150)
    #studentname = Entry(screen,textvariable= stdname )
    #studentname.place(x=200,y=150)
    Label(screen,text = "Choose Image:").place(x=50,y=100)
    Button(screen,text = "Browse",width="15", command = browse).place(x=150,y=150)

    Button(screen,text = "submit",width="15", command = send_data).place(x=150,y=200)
    
    


   

    screen.mainloop()

main_screen()