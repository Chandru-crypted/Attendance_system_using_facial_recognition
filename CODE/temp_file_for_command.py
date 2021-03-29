# i have used the file for creating the create table command which has 128 columns
f = open(r"C:\Users\ELCOT\Documents\Chandru\Git_Bash\Attendance_system_using_facial_recognition\CODE\db\table_creation2.txt", "a")
for i in range(128):
	f.write("Face_arr_{:}, ".format(i))
f.close()