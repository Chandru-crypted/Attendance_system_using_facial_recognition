from imutils import face_utils
import dlib
import cv2
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor

detector = dlib.get_frontal_face_detector()

# load the input image and convert it to grayscale
image = cv2.imread(r"C:\Users\ELCOT\Documents\GitHub\Attendance_system_using_facial_recognition\CODE\Classroom test\Original\Cls6_1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detect faces in the grayscale image
rects = detector(gray, 0)

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



status = cv2.imwrite(r'C:\Users\ELCOT\Documents\GitHub\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection\Cls6_1.jpg', img)
status = cv2.imwrite(r'C:\Users\ELCOT\Documents\GitHub\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection and croping\Cls6_1.jpg', crop_img)

if status:
	print("Image saved sucessful")
else:
	print("Image save failed")