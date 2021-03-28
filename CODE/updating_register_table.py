from sqlite3 import connect
import face_recognition
#import cv2
from pypika import Query, Table
import time


def execute_insert_or_update(db_loc, command):
	conn = connect(db_loc)
	curser = conn.cursor()
	curser.execute(command)
	conn.commit()
	conn.close()


def Insert_Reg_ID(db_loc, table_name, Reg_ID):
	table = Table(table_name)
	q = Query.into(table).columns('Reg_ID').insert(Reg_ID)
	sql_command = q.get_sql()
	execute_insert_or_update(db_loc, sql_command)


def Getting_ID_after_Reg_ID(db_loc, table_name, Reg_ID):
	table = Table(table_name)
	q = Query.from_(table).select(table.ID).where(table.Reg_ID == Reg_ID)
	sql_command = q.get_sql()
	conn = connect(db_loc)
	curser = conn.cursor()
	curser.execute(sql_command)
	ID = tuple(curser)[0]
	conn.close()
	return (ID)
	

def Updating_Face_arr(db_loc, table_name, ID,Face_arr_name, Face_arr_value):
	table = Table(table_name)
	q = Query.update(table).set(Face_arr_name, Face_arr_value).where(table.ID == ID)
	sql_command = q.get_sql()
	execute_insert_or_update(db_loc, sql_command)


def updating_register_table_with_face_array(db_loc,table_name,Reg_ID, face_arr):
	
	# inserting the registration number in the table
	Insert_Reg_ID(db_loc, table_name, Reg_ID)

	# getting the id of the registraion number entered 
	ID = Getting_ID_after_Reg_ID(db_loc, table_name, Reg_ID)

	for i in range(0, 128):
		load_start_time = time.time()
		Face_arr_name = "Face_arr_%s" % (i)
		load_end_time = time.time()
		print("making the face arr string ---{:}----".format(load_start_time - load_end_time))
		load_start_time = time.time()
		Updating_Face_arr(db_loc, table_name, ID, Face_arr_name, face_arr[i])
		load_end_time = time.time()
		print("updating face arr ---{:}----".format(load_start_time - load_end_time))


def updating_register_table_with_face_image(db_loc, table_name, Reg_ID, face_img_loc):
	start_time = time.time()
	load_start_time = time.time()
	image = face_recognition.load_image_file(face_img_loc)
	load_end_time = time.time()
	print("loading the image ---{:}----".format(load_start_time - load_end_time))
	load_start_time = time.time()
	encoding = face_recognition.face_encodings(image)[0]
	load_end_time = time.time()
	print("face_recognition process ---{:}----".format(load_start_time - load_end_time))
	load_start_time = time.time()
	updating_register_table_with_face_array(db_loc, table_name, Reg_ID, encoding)
	load_end_time = time.time()
	print("updation in database ---{:}----".format(load_start_time - load_end_time))
	end_time = time.time()
	print("total ---{:}----".format(end_time - start_time))


if __name__ == "__main__":
	db_loc = r'C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\db\test.db'
	table_name = "register"
	updating_register_table_with_face_image(db_loc, table_name, "RA1711004040036", r"C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection and croping\Cls1.png")

