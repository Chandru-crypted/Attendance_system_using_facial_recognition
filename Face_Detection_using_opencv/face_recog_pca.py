# refer this github repo and this notebook
# https://github.com/xanmolx/FaceDetectorUsingPCA/blob/master/PCA_Face_Recognition_IIT2016040.ipynb

import numpy as np
import cv2
#from matplotlib import pyplot as plt

image_width = 150
image_length = 150
total_pixels = image_width*image_length

images = 8
variants = 1
total_images = images*variants

face_vector = []

for i in range(1, total_images+1):
    face_image = cv2.cvtColor(cv2.imread(str(i) + ".jpg"), cv2.COLOR_RGB2GRAY)
#     plt.imshow(face_image, cmap = 'gray', interpolation = 'bicubic')
#     plt.show()
    face_image = face_image.reshape(total_pixels,)
    face_vector.append(face_image)
    
face_vector = np.asarray(face_vector)
face_vector = face_vector.transpose()

print(face_vector.shape)
print(face_vector)



#STEP2: Normalize the face vectors by calculating the average face vector and subtracting it from each vector
avg_face_vector = face_vector.mean(axis=1)
avg_face_vector = avg_face_vector.reshape(face_vector.shape[0], 1)
normalized_face_vector = face_vector - avg_face_vector
print(normalized_face_vector)


#STEP3: Calculate the Covariance Matrix or the Sigma
covariance_matrix = np.cov(np.transpose(normalized_face_vector))
# covariance_matrix = np.transpose(normalized_face_vector).dot(normalized_face_vector)
print(covariance_matrix)

#STEP4: Calculate Eigen Vectors
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

#STEP5: Select the K best Eigen Faces, K < M
print(eigen_vectors.shape)
k = 20
k_eigen_vectors = eigen_vectors[0:k, :]
print(k_eigen_vectors.shape)


#STEP6: Convert lower dimensionality K Eigen Vectors to Original Dimensionality
eigen_faces = k_eigen_vectors.dot(np.transpose(normalized_face_vector))
print(eigen_faces.shape)


# STEP7: Represent Each eigen face as combination of the K Eigen Vectors
# weights = eigen_faces.dot(normalized_face_vector)
weights = np.transpose(normalized_face_vector).dot(np.transpose(eigen_faces))
print(weights)



#STEP8: Testing Phase
test_add = "1" + ".jpg" #try changing this "1" into "9" or "8" and see the index
test_img = cv2.imread(test_add)
test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2GRAY)


test_img = test_img.reshape(total_pixels, 1)
test_normalized_face_vector = test_img - avg_face_vector
test_weight = np.transpose(test_normalized_face_vector).dot(np.transpose(eigen_faces))


index =  np.argmin(np.linalg.norm(test_weight - weights, axis=1))  
print(index)

test_add = "4" + ".jpg"
test_img = cv2.imread(test_add)
test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2GRAY)


test_img = test_img.reshape(total_pixels, 1)
test_normalized_face_vector = test_img - avg_face_vector
test_weight = np.transpose(test_normalized_face_vector).dot(np.transpose(eigen_faces))


index =  np.argmin(np.linalg.norm(test_weight - weights, axis=1))  
print(index)
