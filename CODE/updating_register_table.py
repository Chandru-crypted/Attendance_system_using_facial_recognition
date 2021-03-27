import sqlite3
import face_recognition
import cv2
from pypika import Query, Table

def creating_insert(table_name, Reg_ID, Face_array):
	table = Table(table_name)
	q = Query.into(table).columns('Reg_ID', 'Face_array').insert(Reg_ID, Face_array)
	sql_command = q.get_sql()
	return (sql_command)

def execute_insert(command):
	conn = sqlite3.connect(db_loc)
	curser = conn.execute(command)
	conn.close() 

def get_back_array_from_string(Face_array):
	Face_array_list =  list(map(float, Face_array.split(' ')[: -1]))

	print(Face_array_list)


db_loc = r'C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\db\test.db'
table_name = "register"

known_image = face_recognition.load_image_file(r"C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection and croping\Cls1.png")
known_encoding = face_recognition.face_encodings(known_image)[0]

Face_array = ""
for i in range(len(known_encoding)):
	Face_array += "{:.8f}".format(float(known_encoding[i]))
	Face_array += " " 

command = creating_insert(table_name, "RA1711004040030", Face_array)
print(command)
get_back_array_from_string(Face_array)
# execute_insert(command)
