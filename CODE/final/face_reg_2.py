from tkinter import *
import os
# import cv2
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter
import json
#face_detect packages

# from imutils import face_utils
# import dlib
# import cv2

# import face_recognition

from sqlite3 import connect
from face_recognition import load_image_file, face_encodings
from pypika import Query, Table

def execute_insert_or_update(db_loc, command):
    conn = connect(db_loc)
    curser = conn.cursor()
    curser.execute(command)
    conn.commit()
    conn.close()

def initialising_database(db_loc): 
    command = ''' CREATE TABLE IF NOT EXISTS students_record (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Reg_ID TEXT NOT NULL,
    Face_arr_0 REAL,
    Face_arr_1 REAL,
    Face_arr_2 REAL,
    Face_arr_3 REAL,
    Face_arr_4 REAL,
    Face_arr_5 REAL,
    Face_arr_6 REAL,
    Face_arr_7 REAL,
    Face_arr_8 REAL,
    Face_arr_9 REAL,
    Face_arr_10 REAL,
    Face_arr_11 REAL,
    Face_arr_12 REAL,
    Face_arr_13 REAL,
    Face_arr_14 REAL,
    Face_arr_15 REAL,
    Face_arr_16 REAL,
    Face_arr_17 REAL,
    Face_arr_18 REAL,
    Face_arr_19 REAL,
    Face_arr_20 REAL,
    Face_arr_21 REAL,
    Face_arr_22 REAL,
    Face_arr_23 REAL,
    Face_arr_24 REAL,
    Face_arr_25 REAL,
    Face_arr_26 REAL,
    Face_arr_27 REAL,
    Face_arr_28 REAL,
    Face_arr_29 REAL,
    Face_arr_30 REAL,
    Face_arr_31 REAL,
    Face_arr_32 REAL,
    Face_arr_33 REAL,
    Face_arr_34 REAL,
    Face_arr_35 REAL,
    Face_arr_36 REAL,
    Face_arr_37 REAL,
    Face_arr_38 REAL,
    Face_arr_39 REAL,
    Face_arr_40 REAL,
    Face_arr_41 REAL,
    Face_arr_42 REAL,
    Face_arr_43 REAL,
    Face_arr_44 REAL,
    Face_arr_45 REAL,
    Face_arr_46 REAL,
    Face_arr_47 REAL,
    Face_arr_48 REAL,
    Face_arr_49 REAL,
    Face_arr_50 REAL,
    Face_arr_51 REAL,
    Face_arr_52 REAL,
    Face_arr_53 REAL,
    Face_arr_54 REAL,
    Face_arr_55 REAL,
    Face_arr_56 REAL,
    Face_arr_57 REAL,
    Face_arr_58 REAL,
    Face_arr_59 REAL,
    Face_arr_60 REAL,
    Face_arr_61 REAL,
    Face_arr_62 REAL,
    Face_arr_63 REAL,
    Face_arr_64 REAL,
    Face_arr_65 REAL,
    Face_arr_66 REAL,
    Face_arr_67 REAL,
    Face_arr_68 REAL,
    Face_arr_69 REAL,
    Face_arr_70 REAL,
    Face_arr_71 REAL,
    Face_arr_72 REAL,
    Face_arr_73 REAL,
    Face_arr_74 REAL,
    Face_arr_75 REAL,
    Face_arr_76 REAL,
    Face_arr_77 REAL,
    Face_arr_78 REAL,
    Face_arr_79 REAL,
    Face_arr_80 REAL,
    Face_arr_81 REAL,
    Face_arr_82 REAL,
    Face_arr_83 REAL,
    Face_arr_84 REAL,
    Face_arr_85 REAL,
    Face_arr_86 REAL,
    Face_arr_87 REAL,
    Face_arr_88 REAL,
    Face_arr_89 REAL,
    Face_arr_90 REAL,
    Face_arr_91 REAL,
    Face_arr_92 REAL,
    Face_arr_93 REAL,
    Face_arr_94 REAL,
    Face_arr_95 REAL,
    Face_arr_96 REAL,
    Face_arr_97 REAL,
    Face_arr_98 REAL,
    Face_arr_99 REAL,
    Face_arr_100 REAL,
    Face_arr_101 REAL,
    Face_arr_102 REAL,
    Face_arr_103 REAL,
    Face_arr_104 REAL,
    Face_arr_105 REAL,
    Face_arr_106 REAL,
    Face_arr_107 REAL,
    Face_arr_108 REAL,
    Face_arr_109 REAL,
    Face_arr_110 REAL,
    Face_arr_111 REAL,
    Face_arr_112 REAL,
    Face_arr_113 REAL,
    Face_arr_114 REAL,
    Face_arr_115 REAL,
    Face_arr_116 REAL,
    Face_arr_117 REAL,
    Face_arr_118 REAL,
    Face_arr_119 REAL,
    Face_arr_120 REAL,
    Face_arr_121 REAL,
    Face_arr_122 REAL,
    Face_arr_123 REAL,
    Face_arr_124 REAL,
    Face_arr_125 REAL,
    Face_arr_126 REAL,
    Face_arr_127 REAL
    );'''
    execute_insert_or_update(db_loc, command)

def Insert_Reg_ID(db_loc, table_name, Reg_ID, face_arr):
    # using %s for string concatenation as it improves the speed
    col_names = ", Face_arr_0, Face_arr_1, Face_arr_2, Face_arr_3, Face_arr_4, Face_arr_5, Face_arr_6, Face_arr_7, Face_arr_8, Face_arr_9, Face_arr_10, Face_arr_11, Face_arr_12, Face_arr_13, Face_arr_14, Face_arr_15, Face_arr_16, Face_arr_17, Face_arr_18, Face_arr_19, Face_arr_20, Face_arr_21, Face_arr_22, Face_arr_23, Face_arr_24, Face_arr_25, Face_arr_26, Face_arr_27, Face_arr_28, Face_arr_29, Face_arr_30, Face_arr_31, Face_arr_32, Face_arr_33, Face_arr_34, Face_arr_35, Face_arr_36, Face_arr_37, Face_arr_38, Face_arr_39, Face_arr_40, Face_arr_41, Face_arr_42, Face_arr_43, Face_arr_44, Face_arr_45, Face_arr_46, Face_arr_47, Face_arr_48, Face_arr_49, Face_arr_50, Face_arr_51, Face_arr_52, Face_arr_53, Face_arr_54, Face_arr_55, Face_arr_56, Face_arr_57, Face_arr_58, Face_arr_59, Face_arr_60, Face_arr_61, Face_arr_62, Face_arr_63, Face_arr_64, Face_arr_65, Face_arr_66, Face_arr_67, Face_arr_68, Face_arr_69, Face_arr_70, Face_arr_71, Face_arr_72, Face_arr_73, Face_arr_74, Face_arr_75, Face_arr_76, Face_arr_77, Face_arr_78, Face_arr_79, Face_arr_80, Face_arr_81, Face_arr_82, Face_arr_83, Face_arr_84, Face_arr_85, Face_arr_86, Face_arr_87, Face_arr_88, Face_arr_89, Face_arr_90, Face_arr_91, Face_arr_92, Face_arr_93, Face_arr_94, Face_arr_95, Face_arr_96, Face_arr_97, Face_arr_98, Face_arr_99, Face_arr_100, Face_arr_101, Face_arr_102, Face_arr_103, Face_arr_104, Face_arr_105, Face_arr_106, Face_arr_107, Face_arr_108, Face_arr_109, Face_arr_110, Face_arr_111, Face_arr_112, Face_arr_113, Face_arr_114, Face_arr_115, Face_arr_116, Face_arr_117, Face_arr_118, Face_arr_119, Face_arr_120, Face_arr_121, Face_arr_122, Face_arr_123, Face_arr_124, Face_arr_125, Face_arr_126, Face_arr_127"
    col_values_str = ", ".join(face_arr)
    sql_command = "INSERT INTO %s (Reg_ID %s) VALUES (%s, %s);" % (table_name, col_names, "\' %s \'" % (Reg_ID), col_values_str)
    execute_insert_or_update(db_loc, sql_command)


def updating_register_table_with_face_image(db_loc, table_name, Reg_ID, face_img_loc):
    image = load_image_file(face_img_loc)
    # print(image)
    # print(type(image))
    # using the tuple and map function for perfomance
    # this creates a tuple of face arr values converted into strings
    encoding = tuple(map(str, face_encodings(image)[0]))
    Insert_Reg_ID(db_loc, table_name, Reg_ID, encoding)

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
    face_img_loc = filename
    Reg_ID = userid.get()
    print(Reg_ID,"\n")
    #print(stdname.get(),"\n")
    print(face_img_loc,"\n")
    db_loc = r'C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\final\db\STUDENTSDATA.db'
    table_name = "students_record"
    initialising_database(db_loc)
    updating_register_table_with_face_image(db_loc, table_name, Reg_ID, face_img_loc)

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


if (__name__ == "__main__"):
	main_screen()