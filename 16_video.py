# import openCV library
import cv2
# import numpy library
import numpy as np

# video file path
path = 'ball_colorful.mp4'
# create video capture
vcap = cv2.VideoCapture(path)

# check camera
if not vcap.isOpened():
    raise Exception('Could not open video device or video file')

while True:
    # capture frame
    ret, frame = vcap.read()
    
    # exit can't read frame
    if not ret:
        break
    
    # display frame
    cv2.imshow('Frame', frame)
    
    # press key 'q' for quit
    if cv2.waitKey(1) == ord('q'):
        break
    
# release video capture
vcap.release()
# close all window
cv2.destroyAllWindows()