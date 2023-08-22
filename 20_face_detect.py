# import openCV library
import cv2

# Haar feature-based cascade classifiers
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# file path
path = 'thaiger.png'
#path = 'srtc01.jpg'
image_bgr = cv2.imread(path)

# display image
cv2.imshow('Image', image_bgr)

# convert color RGB -> gray
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
# display image
cv2.imshow('Gray', image_gray)

# detect face
faces = face_classifier.detectMultiScale(image_gray, 1.1, 4) #(image_gray, 1.1, 4)

# draw rectangle
for (x, y, w, h) in faces:
    cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# display image
cv2.imshow('Face detection', image_bgr)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()