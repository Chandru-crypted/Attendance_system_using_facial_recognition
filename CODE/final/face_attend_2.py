from sqlite3 import connect
from imutils import face_utils
import dlib
import cv2
from face_recognition import load_image_file, face_encodings, compare_faces
from tkinter import *
import os
import cv2
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter
import numpy as np
from scipy import spatial
def read_data_from_db():
	db_loc = r'C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\final\db\STUDENTSDATA.db'
	#print ('studentsdata Database opened')
	conn = connect(db_loc)
	curser = conn.cursor()
	command = '''SELECT * FROM students_record '''
	data = curser.execute(command)
	res_list = []
	temp_lis = []
	temp_encoding = []
	for record in data:
		temp_lis = list(record[0:2])
		temp_encoding = record[2:]
		temp_lis.append(np.asarray(temp_encoding))
		res_list.append(tuple(temp_lis))
	conn.close()
	res = tuple(res_list)
	return (res)

def find_faces_in_img(img_loc):
	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	# load the input image and convert it to grayscale
	image = cv2.imread(img_loc)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#frame = imutils.resize(frame, width=450)
	# detect faces in the grayscale image
	rects = detector(gray, 0)
	encoding_in_class_lis = []
	# loop over the face detections
	for (i, rect) in enumerate(rects):
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
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
		# # Blue color in BGR 
		# color = (255, 0, 0) 
		# # Line thickness of 2 px 
		# thickness = 2
		crop_img = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
		cv2.imwrite(r'C:\Users\ELCOT\Documents\Cls{}.jpg'.format(i), crop_img)
		encoding = face_encodings(crop_img)[0]
		encoding_in_class_lis.append(encoding)
	encoding_in_class = tuple(encoding_in_class_lis)
	return (encoding_in_class)

def compare_2_faces(known_encoding, unknown_encoding):
	# known encoding will be register images that is already in the db
	# unknown encoding will be the image taken 
	# result = 1 - spatial.distance.cosine(known_encoding, unknown_encoding)
	# print(result)
	# return (result)
	res = compare_faces([known_encoding], unknown_encoding, tolerance=0.5)[0]
	#print(res)
	return (res)

def compare_in_db(encoding_in_class, encoding_in_db):
	for i in encoding_in_class:
		for j in encoding_in_db:
			if (compare_2_faces(j[2], i)):
				print(j[0])
				print(j[1])
				break

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
	img_loc = filename
	encoding_in_class = find_faces_in_img(img_loc)
	encoding_in_db = read_data_from_db()
	compare_in_db(encoding_in_class, encoding_in_db)

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
	Label(screen,text = "Choose Image:").place(x=50,y=100)
	Button(screen,text = "Browse",width="15", command = browse).place(x=150,y=150)
	Button(screen,text = "submit",width="15", command = send_data).place(x=150,y=200)
	screen.mainloop()

if __name__ == "__main__":
	main_screen()