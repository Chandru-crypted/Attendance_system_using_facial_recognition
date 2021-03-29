import face_recognition
import cv2

known_image = face_recognition.load_image_file(r"C:\Users\ELCOT\Documents\GitHub\Attendance_system_using_facial_recognition\CODE\Classroom test\After face detection and croping\Cls1.png")
unknown_image = face_recognition.load_image_file(r"C:\Users\ELCOT\Downloads\Aathi.png")
print(unknown_image)

half = cv2.resize(unknown_image, (0, 0), fx = 0.1, fy = 0.1) 

known_encoding = face_recognition.face_encodings(known_image)[0]
print(known_encoding)
unknown_encoding = face_recognition.face_encodings(half)[0]

print(known_encoding)
print(unknown_encoding)

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

print(results)