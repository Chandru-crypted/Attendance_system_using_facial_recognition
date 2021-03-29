from sqlite3 import connect
from face_recognition import load_image_file, face_encodings
from pypika import Query, Table
import time

"""
Used these websites for creating the fast thing
actually making a single insert statement is so fast approax it is taking 0.1 to 0.2 seconds

join method = https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string
%s method = https://wiki.python.org/moin/PythonSpeed/PerformanceTips
"""

def execute_insert_or_update(db_loc, command):
	conn = connect(db_loc)
	curser = conn.cursor()
	curser.execute(command)
	conn.commit()
	conn.close()


def Insert_Reg_ID(db_loc, table_name, Reg_ID, face_arr):
	col_names = ", Face_arr_0, Face_arr_1, Face_arr_2, Face_arr_3, Face_arr_4, Face_arr_5, Face_arr_6, Face_arr_7, Face_arr_8, Face_arr_9, Face_arr_10, Face_arr_11, Face_arr_12, Face_arr_13, Face_arr_14, Face_arr_15, Face_arr_16, Face_arr_17, Face_arr_18, Face_arr_19, Face_arr_20, Face_arr_21, Face_arr_22, Face_arr_23, Face_arr_24, Face_arr_25, Face_arr_26, Face_arr_27, Face_arr_28, Face_arr_29, Face_arr_30, Face_arr_31, Face_arr_32, Face_arr_33, Face_arr_34, Face_arr_35, Face_arr_36, Face_arr_37, Face_arr_38, Face_arr_39, Face_arr_40, Face_arr_41, Face_arr_42, Face_arr_43, Face_arr_44, Face_arr_45, Face_arr_46, Face_arr_47, Face_arr_48, Face_arr_49, Face_arr_50, Face_arr_51, Face_arr_52, Face_arr_53, Face_arr_54, Face_arr_55, Face_arr_56, Face_arr_57, Face_arr_58, Face_arr_59, Face_arr_60, Face_arr_61, Face_arr_62, Face_arr_63, Face_arr_64, Face_arr_65, Face_arr_66, Face_arr_67, Face_arr_68, Face_arr_69, Face_arr_70, Face_arr_71, Face_arr_72, Face_arr_73, Face_arr_74, Face_arr_75, Face_arr_76, Face_arr_77, Face_arr_78, Face_arr_79, Face_arr_80, Face_arr_81, Face_arr_82, Face_arr_83, Face_arr_84, Face_arr_85, Face_arr_86, Face_arr_87, Face_arr_88, Face_arr_89, Face_arr_90, Face_arr_91, Face_arr_92, Face_arr_93, Face_arr_94, Face_arr_95, Face_arr_96, Face_arr_97, Face_arr_98, Face_arr_99, Face_arr_100, Face_arr_101, Face_arr_102, Face_arr_103, Face_arr_104, Face_arr_105, Face_arr_106, Face_arr_107, Face_arr_108, Face_arr_109, Face_arr_110, Face_arr_111, Face_arr_112, Face_arr_113, Face_arr_114, Face_arr_115, Face_arr_116, Face_arr_117, Face_arr_118, Face_arr_119, Face_arr_120, Face_arr_121, Face_arr_122, Face_arr_123, Face_arr_124, Face_arr_125, Face_arr_126, Face_arr_127"
	col_values_str = ", ".join(face_arr)
	sql_command = "INSERT INTO %s (Reg_ID %s) VALUES (%s, %s);" % (table_name, col_names, "\' %s \'" % (Reg_ID), col_values_str)
	execute_insert_or_update(db_loc, sql_command)


def updating_register_table_with_face_image(db_loc, table_name, Reg_ID, face_img_loc):
	start_time = time.time()
	load_start_time = time.time()
	image = load_image_file(face_img_loc)
	load_end_time = time.time()
	print("loading the image ---{:}----".format(load_start_time - load_end_time))
	load_start_time = time.time()
	encoding = tuple(map(str, face_encodings(image)[0])) # making as tuple for perfomance
	load_end_time = time.time()
	print("face_recognition process ---{:}----".format(load_start_time - load_end_time))
	load_start_time = time.time()
	Insert_Reg_ID(db_loc, table_name, Reg_ID, encoding)
	load_end_time = time.time()
	print("updation in database ---{:}----".format(load_start_time - load_end_time))
	end_time = time.time()
	print("total ---{:}----".format(end_time - start_time))


if __name__ == "__main__":
	db_loc = r'C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\db\test.db'
	table_name = "register"
	updating_register_table_with_face_image(db_loc, table_name, "RA1711004040048", r"C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection and croping\Cls1.png")

