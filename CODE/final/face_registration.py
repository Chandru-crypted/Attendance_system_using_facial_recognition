from tkinter import *
import os
import cv2
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter
import sqlite3
import json
#face_detect packages

from imutils import face_utils
import dlib
import cv2

import face_recognition


#database connection

dbase = sqlite3.connect('STUDENTSDATA.db')
print ('Database opened')

dbase.execute('''CREATE TABLE IF NOT EXISTS students_record(
    ID CHAR PRIMARY KEY NOT NULL,
    NAME CHAR NOT NULL,
    FACE_ARR_0 FLOAT NOT NULL,
    FACE_ARR_1 FLOAT NOT NULL,
    FACE_ARR_2 FLOAT NOT NULL,
    FACE_ARR_3 FLOAT NOT NULL,
    FACE_ARR_4 FLOAT NOT NULL,
    FACE_ARR_5 FLOAT NOT NULL,
    FACE_ARR_6 FLOAT NOT NULL,
    FACE_ARR_7 FLOAT NOT NULL,
    FACE_ARR_8 FLOAT NOT NULL,
    FACE_ARR_9 FLOAT NOT NULL,
    FACE_ARR_10 FLOAT NOT NULL,
    FACE_ARR_11 FLOAT NOT NULL,
    FACE_ARR_12 FLOAT NOT NULL,
    FACE_ARR_13 FLOAT NOT NULL,
    FACE_ARR_14 FLOAT NOT NULL,
    FACE_ARR_15 FLOAT NOT NULL,
    FACE_ARR_16 FLOAT NOT NULL,
    FACE_ARR_17 FLOAT NOT NULL,
    FACE_ARR_18 FLOAT NOT NULL,
    FACE_ARR_19 FLOAT NOT NULL,
    FACE_ARR_20 FLOAT NOT NULL,
    FACE_ARR_21 FLOAT NOT NULL,
    FACE_ARR_22 FLOAT NOT NULL,
    FACE_ARR_23 FLOAT NOT NULL,
    FACE_ARR_24 FLOAT NOT NULL,
    FACE_ARR_25 FLOAT NOT NULL,
    FACE_ARR_26 FLOAT NOT NULL,
    FACE_ARR_27 FLOAT NOT NULL,
    FACE_ARR_28 FLOAT NOT NULL,
    FACE_ARR_29 FLOAT NOT NULL,
    FACE_ARR_30 FLOAT NOT NULL,
    FACE_ARR_31 FLOAT NOT NULL,
    FACE_ARR_32 FLOAT NOT NULL,
    FACE_ARR_33 FLOAT NOT NULL,
    FACE_ARR_34 FLOAT NOT NULL,
    FACE_ARR_35 FLOAT NOT NULL,
    FACE_ARR_36 FLOAT NOT NULL,
    FACE_ARR_37 FLOAT NOT NULL,
    FACE_ARR_38 FLOAT NOT NULL,
    FACE_ARR_39 FLOAT NOT NULL,
    FACE_ARR_40 FLOAT NOT NULL,
    FACE_ARR_41 FLOAT NOT NULL,
    FACE_ARR_42 FLOAT NOT NULL,
    FACE_ARR_43 FLOAT NOT NULL,
    FACE_ARR_44 FLOAT NOT NULL,
    FACE_ARR_45 FLOAT NOT NULL,
    FACE_ARR_46 FLOAT NOT NULL,
    FACE_ARR_47 FLOAT NOT NULL,
    FACE_ARR_48 FLOAT NOT NULL,
    FACE_ARR_49 FLOAT NOT NULL,
    FACE_ARR_50 FLOAT NOT NULL,
    FACE_ARR_51 FLOAT NOT NULL,
    FACE_ARR_52 FLOAT NOT NULL,
    FACE_ARR_53 FLOAT NOT NULL,
    FACE_ARR_54 FLOAT NOT NULL,
    FACE_ARR_55 FLOAT NOT NULL,
    FACE_ARR_56 FLOAT NOT NULL,
    FACE_ARR_57 FLOAT NOT NULL,
    FACE_ARR_58 FLOAT NOT NULL,
    FACE_ARR_59 FLOAT NOT NULL,
    FACE_ARR_60 FLOAT NOT NULL,
    FACE_ARR_61 FLOAT NOT NULL,
    FACE_ARR_62 FLOAT NOT NULL,
    FACE_ARR_63 FLOAT NOT NULL,
    FACE_ARR_64 FLOAT NOT NULL,
    FACE_ARR_65 FLOAT NOT NULL,
    FACE_ARR_66 FLOAT NOT NULL,
    FACE_ARR_67 FLOAT NOT NULL,
    FACE_ARR_68 FLOAT NOT NULL,
    FACE_ARR_69 FLOAT NOT NULL,
    FACE_ARR_70 FLOAT NOT NULL,
    FACE_ARR_71 FLOAT NOT NULL,
    FACE_ARR_72 FLOAT NOT NULL,
    FACE_ARR_73 FLOAT NOT NULL,
    FACE_ARR_74 FLOAT NOT NULL,
    FACE_ARR_75 FLOAT NOT NULL,
    FACE_ARR_76 FLOAT NOT NULL,
    FACE_ARR_77 FLOAT NOT NULL,
    FACE_ARR_78 FLOAT NOT NULL,
    FACE_ARR_79 FLOAT NOT NULL,
    FACE_ARR_80 FLOAT NOT NULL,
    FACE_ARR_81 FLOAT NOT NULL,
    FACE_ARR_82 FLOAT NOT NULL,
    FACE_ARR_83 FLOAT NOT NULL,
    FACE_ARR_84 FLOAT NOT NULL,
    FACE_ARR_85 FLOAT NOT NULL,
    FACE_ARR_86 FLOAT NOT NULL,
    FACE_ARR_87 FLOAT NOT NULL,
    FACE_ARR_88 FLOAT NOT NULL,
    FACE_ARR_89 FLOAT NOT NULL,
    FACE_ARR_90 FLOAT NOT NULL,
    FACE_ARR_91 FLOAT NOT NULL,
    FACE_ARR_92 FLOAT NOT NULL,
    FACE_ARR_93 FLOAT NOT NULL,
    FACE_ARR_94 FLOAT NOT NULL,
    FACE_ARR_95 FLOAT NOT NULL,
    FACE_ARR_96 FLOAT NOT NULL,
    FACE_ARR_97 FLOAT NOT NULL,
    FACE_ARR_98 FLOAT NOT NULL,
    FACE_ARR_99 FLOAT NOT NULL,
    FACE_ARR_100 FLOAT NOT NULL,
    FACE_ARR_101 FLOAT NOT NULL,
    FACE_ARR_102 FLOAT NOT NULL,
    FACE_ARR_103 FLOAT NOT NULL,
    FACE_ARR_104 FLOAT NOT NULL,
    FACE_ARR_105 FLOAT NOT NULL,
    FACE_ARR_106 FLOAT NOT NULL,
    FACE_ARR_107 FLOAT NOT NULL,
    FACE_ARR_108 FLOAT NOT NULL,
    FACE_ARR_109 FLOAT NOT NULL,
    FACE_ARR_110 FLOAT NOT NULL,
    FACE_ARR_111 FLOAT NOT NULL,
    FACE_ARR_112 FLOAT NOT NULL,
    FACE_ARR_113 FLOAT NOT NULL,
    FACE_ARR_114 FLOAT NOT NULL,
    FACE_ARR_115 FLOAT NOT NULL,
    FACE_ARR_116 FLOAT NOT NULL,
    FACE_ARR_117 FLOAT NOT NULL,
    FACE_ARR_118 FLOAT NOT NULL,
    FACE_ARR_119 FLOAT NOT NULL,
    FACE_ARR_120 FLOAT NOT NULL,
    FACE_ARR_121 FLOAT NOT NULL,
    FACE_ARR_122 FLOAT NOT NULL,
    FACE_ARR_123 FLOAT NOT NULL,
    FACE_ARR_124 FLOAT NOT NULL,
    FACE_ARR_125 FLOAT NOT NULL,
    FACE_ARR_126 FLOAT NOT NULL,
    FACE_ARR_127 FLOAT NOT NULL)''')

print ('TABLE CREATED')


def insert_record(ID,NAME,FACE_ARR_0, FACE_ARR_1, FACE_ARR_2, FACE_ARR_3, FACE_ARR_4, FACE_ARR_5, FACE_ARR_6, FACE_ARR_7, FACE_ARR_8, FACE_ARR_9, FACE_ARR_10, FACE_ARR_11, FACE_ARR_12, FACE_ARR_13, FACE_ARR_14, FACE_ARR_15, FACE_ARR_16, FACE_ARR_17, FACE_ARR_18, FACE_ARR_19, FACE_ARR_20, FACE_ARR_21, FACE_ARR_22, FACE_ARR_23, FACE_ARR_24, FACE_ARR_25, FACE_ARR_26, FACE_ARR_27, FACE_ARR_28, FACE_ARR_29, FACE_ARR_30, FACE_ARR_31, FACE_ARR_32, FACE_ARR_33, FACE_ARR_34, FACE_ARR_35, FACE_ARR_36, FACE_ARR_37, FACE_ARR_38, FACE_ARR_39, FACE_ARR_40, FACE_ARR_41, FACE_ARR_42, FACE_ARR_43, FACE_ARR_44, FACE_ARR_45, FACE_ARR_46, FACE_ARR_47, FACE_ARR_48, FACE_ARR_49, FACE_ARR_50, FACE_ARR_51, FACE_ARR_52, FACE_ARR_53, FACE_ARR_54, FACE_ARR_55, FACE_ARR_56, FACE_ARR_57, FACE_ARR_58, FACE_ARR_59, FACE_ARR_60, FACE_ARR_61, FACE_ARR_62, FACE_ARR_63, FACE_ARR_64, FACE_ARR_65, FACE_ARR_66, FACE_ARR_67, FACE_ARR_68, FACE_ARR_69, FACE_ARR_70, FACE_ARR_71, FACE_ARR_72, FACE_ARR_73, FACE_ARR_74, FACE_ARR_75, FACE_ARR_76, FACE_ARR_77, FACE_ARR_78, FACE_ARR_79, FACE_ARR_80, FACE_ARR_81, FACE_ARR_82, FACE_ARR_83, FACE_ARR_84, FACE_ARR_85, FACE_ARR_86, FACE_ARR_87, FACE_ARR_88, FACE_ARR_89, FACE_ARR_90, FACE_ARR_91, FACE_ARR_92, FACE_ARR_93, FACE_ARR_94, FACE_ARR_95, FACE_ARR_96, FACE_ARR_97, FACE_ARR_98, FACE_ARR_99, FACE_ARR_100, FACE_ARR_101, FACE_ARR_102, FACE_ARR_103, FACE_ARR_104, FACE_ARR_105, FACE_ARR_106, FACE_ARR_107, FACE_ARR_108, FACE_ARR_109, FACE_ARR_110, FACE_ARR_111, FACE_ARR_112, FACE_ARR_113, FACE_ARR_114, FACE_ARR_115, FACE_ARR_116, FACE_ARR_117, FACE_ARR_118, FACE_ARR_119, FACE_ARR_120, FACE_ARR_121, FACE_ARR_122, FACE_ARR_123, FACE_ARR_124, FACE_ARR_125, FACE_ARR_126, FACE_ARR_127):
    dbase.execute('''INSERT INTO students_record(ID,NAME,FACE_ARR_0, FACE_ARR_1, FACE_ARR_2, FACE_ARR_3, FACE_ARR_4, FACE_ARR_5, FACE_ARR_6, FACE_ARR_7, FACE_ARR_8, FACE_ARR_9, FACE_ARR_10, FACE_ARR_11, FACE_ARR_12, FACE_ARR_13, FACE_ARR_14, FACE_ARR_15, FACE_ARR_16, FACE_ARR_17, FACE_ARR_18, FACE_ARR_19, FACE_ARR_20, FACE_ARR_21, FACE_ARR_22, FACE_ARR_23, FACE_ARR_24, FACE_ARR_25, FACE_ARR_26, FACE_ARR_27, FACE_ARR_28, FACE_ARR_29, FACE_ARR_30, FACE_ARR_31, FACE_ARR_32, FACE_ARR_33, FACE_ARR_34, FACE_ARR_35, FACE_ARR_36, FACE_ARR_37, FACE_ARR_38, FACE_ARR_39, FACE_ARR_40, FACE_ARR_41, FACE_ARR_42, FACE_ARR_43, FACE_ARR_44, FACE_ARR_45, FACE_ARR_46, FACE_ARR_47, FACE_ARR_48, FACE_ARR_49, FACE_ARR_50, FACE_ARR_51, FACE_ARR_52, FACE_ARR_53, FACE_ARR_54, FACE_ARR_55, FACE_ARR_56, FACE_ARR_57, FACE_ARR_58, FACE_ARR_59, FACE_ARR_60, FACE_ARR_61, FACE_ARR_62, FACE_ARR_63, FACE_ARR_64, FACE_ARR_65, FACE_ARR_66, FACE_ARR_67, FACE_ARR_68, FACE_ARR_69, FACE_ARR_70, FACE_ARR_71, FACE_ARR_72, FACE_ARR_73, FACE_ARR_74, FACE_ARR_75, FACE_ARR_76, FACE_ARR_77, FACE_ARR_78, FACE_ARR_79, FACE_ARR_80, FACE_ARR_81, FACE_ARR_82, FACE_ARR_83, FACE_ARR_84, FACE_ARR_85, FACE_ARR_86, FACE_ARR_87, FACE_ARR_88, FACE_ARR_89, FACE_ARR_90, FACE_ARR_91, FACE_ARR_92, FACE_ARR_93, FACE_ARR_94, FACE_ARR_95, FACE_ARR_96, FACE_ARR_97, FACE_ARR_98, FACE_ARR_99, FACE_ARR_100, FACE_ARR_101, FACE_ARR_102, FACE_ARR_103, FACE_ARR_104, FACE_ARR_105, FACE_ARR_106, FACE_ARR_107, FACE_ARR_108, FACE_ARR_109, FACE_ARR_110, FACE_ARR_111, FACE_ARR_112, FACE_ARR_113, FACE_ARR_114, FACE_ARR_115, FACE_ARR_116, FACE_ARR_117, FACE_ARR_118, FACE_ARR_119, FACE_ARR_120, FACE_ARR_121, FACE_ARR_122, FACE_ARR_123, FACE_ARR_124, FACE_ARR_125, FACE_ARR_126, FACE_ARR_127)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(ID,NAME,float(FACE_ARR_0),float(FACE_ARR_1),float(FACE_ARR_2),float(FACE_ARR_3),float(FACE_ARR_4),float(FACE_ARR_5),float(FACE_ARR_6),float(FACE_ARR_7),float(FACE_ARR_8),float(FACE_ARR_9),float(FACE_ARR_10),float(FACE_ARR_11),float(FACE_ARR_12),float(FACE_ARR_13),float(FACE_ARR_14),float(FACE_ARR_15),float(FACE_ARR_16),float(FACE_ARR_17),float(FACE_ARR_18),float(FACE_ARR_19),float(FACE_ARR_20),float(FACE_ARR_21),float(FACE_ARR_22), float(FACE_ARR_23), float(FACE_ARR_24), float(FACE_ARR_25), float(FACE_ARR_26), float(FACE_ARR_27), float(FACE_ARR_28), float(FACE_ARR_29), float(FACE_ARR_30), float(FACE_ARR_31), float(FACE_ARR_32), float(FACE_ARR_33), float(FACE_ARR_34), float(FACE_ARR_35), float(FACE_ARR_36), float(FACE_ARR_37), float(FACE_ARR_38), float(FACE_ARR_39), float(FACE_ARR_40), float(FACE_ARR_41), float(FACE_ARR_42), float(FACE_ARR_43), float(FACE_ARR_44), float(FACE_ARR_45), float(FACE_ARR_46), float(FACE_ARR_47), float(FACE_ARR_48), float(FACE_ARR_49), float(FACE_ARR_50), float(FACE_ARR_51), float(FACE_ARR_52), float(FACE_ARR_53), float(FACE_ARR_54), float(FACE_ARR_55), float(FACE_ARR_56), float(FACE_ARR_57), float(FACE_ARR_58), float(FACE_ARR_59), float(FACE_ARR_60), float(FACE_ARR_61), float(FACE_ARR_62), float(FACE_ARR_63), float(FACE_ARR_64), float(FACE_ARR_65), float(FACE_ARR_66), float(FACE_ARR_67), float(FACE_ARR_68), float(FACE_ARR_69), float(FACE_ARR_70), float(FACE_ARR_71), float(FACE_ARR_72), float(FACE_ARR_73), float(FACE_ARR_74), float(FACE_ARR_75), float(FACE_ARR_76), float(FACE_ARR_77), float(FACE_ARR_78), float(FACE_ARR_79), float(FACE_ARR_80), float(FACE_ARR_81), float(FACE_ARR_82), float(FACE_ARR_83), float(FACE_ARR_84), float(FACE_ARR_85), float(FACE_ARR_86), float(FACE_ARR_87), float(FACE_ARR_88), float(FACE_ARR_89), float(FACE_ARR_90), float(FACE_ARR_91), float(FACE_ARR_92), float(FACE_ARR_93), float(FACE_ARR_94), float(FACE_ARR_95), float(FACE_ARR_96), float(FACE_ARR_97), float(FACE_ARR_98), float(FACE_ARR_99), float(FACE_ARR_100), float(FACE_ARR_101), float(FACE_ARR_102), float(FACE_ARR_103), float(FACE_ARR_104), float(FACE_ARR_105), float(FACE_ARR_106), float(FACE_ARR_107), float(FACE_ARR_108), float(FACE_ARR_109), float(FACE_ARR_110), float(FACE_ARR_111), float(FACE_ARR_112), float(FACE_ARR_113), float(FACE_ARR_114), float(FACE_ARR_115), float(FACE_ARR_116), float(FACE_ARR_117), float(FACE_ARR_118), float(FACE_ARR_119), float(FACE_ARR_120), float(FACE_ARR_121), float(FACE_ARR_122), float(FACE_ARR_123), float(FACE_ARR_124), float(FACE_ARR_125), float(FACE_ARR_126), float(FACE_ARR_127)))
    dbase.commit()
    print ('record inserted')


'''
def read_data():
    data=dbase.execute('''' SELECT ID, ARRAY FROM student_record '''')
    for record in data:
        print('ID : '+str(record[0])+'\n')
        print('ARRAY : '+str(record[1])+'\n\n')
    

read_data()
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

            status = cv2.imwrite(r'C:\Users\muhil\Downloads\project\detected faces\img{}.jpg'.format(i), img)
            status = cv2.imwrite(r'C:\Users\muhil\Downloads\project\detected faces\img{}.jpg'.format(i), crop_img)
    
    res1=face_recognition.face_encodings(img)[0]
    result=tuple(res1)
    res.append(result)

  

    if status:
            print("Image saved sucessful\n")
    else:
            print("Image save failed\n")


    
    insert_record(userid.get(),stdname.get(),float(res[0][0]),float(res[0][1]),float(res[0][2]),float(res[0][3]),float(res[0][4]),float(res[0][5]),float(res[0][6]),float(res[0][7]),float(res[0][8]),float(res[0][9]),float(res[0][10]),float(res[0][11]),float(res[0][12]),float(res[0][13]),float(res[0][14]),float(res[0][15]),float(res[0][16]),float(res[0][17]),float(res[0][18]),float(res[0][19]),float(res[0][20]),float(res[0][21]),float(res[0][22]),float(res[0][23]),float(res[0][24]),float(res[0][25]),float(res[0][26]),float(res[0][27]),float(res[0][28]),float(res[0][29]),float(res[0][30]),float(res[0][31]),float(res[0][32]),float(res[0][33]),float(res[0][34]),float(res[0][35]),float(res[0][36]),float(res[0][37]),float(res[0][38]),float(res[0][39]),float(res[0][40]),float(res[0][41]),float(res[0][42]),float(res[0][43]),float(res[0][44]),float(res[0][45]),float(res[0][46]),float(res[0][47]),float(res[0][48]),float(res[0][49]),float(res[0][50]),float(res[0][51]),float(res[0][52]),float(res[0][53]),float(res[0][54]),float(res[0][55]),float(res[0][56]),float(res[0][57]),float(res[0][58]),float(res[0][59]),float(res[0][60]),float(res[0][61]),float(res[0][62]),float(res[0][63]),float(res[0][64]),float(res[0][65]),float(res[0][66]),float(res[0][67]),float(res[0][68]),float(res[0][69]),float(res[0][70]),float(res[0][71]),float(res[0][72]),float(res[0][73]),float(res[0][74]),float(res[0][75]),float(res[0][76]),float(res[0][77]),float(res[0][78]),float(res[0][79]),float(res[0][80]),float(res[0][81]),float(res[0][82]),float(res[0][83]),float(res[0][84]),float(res[0][85]),float(res[0][86]),float(res[0][87]),float(res[0][88]),float(res[0][89]),float(res[0][90]),float(res[0][91]),float(res[0][92]),float(res[0][93]),float(res[0][94]),float(res[0][95]),float(res[0][96]),float(res[0][97]),float(res[0][98]),float(res[0][99]),float(res[0][100]),float(res[0][101]),float(res[0][102]),float(res[0][103]),float(res[0][104]),float(res[0][105]),float(res[0][106]),float(res[0][107]),float(res[0][108]),float(res[0][109]),float(res[0][110]),float(res[0][111]),float(res[0][112]),float(res[0][113]),float(res[0][114]),float(res[0][115]),float(res[0][116]),float(res[0][117]),float(res[0][118]),float(res[0][119]),float(res[0][120]),float(res[0][121]),float(res[0][122]),float(res[0][123]),float(res[0][124]),float(res[0][125]),float(res[0][126]),float(res[0][127]))
    

    
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
