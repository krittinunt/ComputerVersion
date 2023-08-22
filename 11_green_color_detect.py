# import openCV library
import cv2
# import numpy library
import numpy as np

# image file path
path = 'color_ball.jpg'
# read image
image_bgr = cv2.imread(path, cv2.IMREAD_UNCHANGED)

# create new window title = RGB image
cv2.namedWindow('RGB image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('RGB image', image_bgr)

# convert to HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# rang of green color in HSV
# H -> 38 -> 93
# S -> 50 -> 255
# V -> 50 -> 255
green_lower_hsv = np.array([38, 50, 50]) #([38, 117, 84])
green_higher_hsv = np.array([93, 255, 255])
# mask for green color
green_mask = cv2.inRange(image_hsv, green_lower_hsv, green_higher_hsv)
green_detected_image = cv2.bitwise_and(image_bgr, image_bgr, mask=green_mask)

# create new window title = Green detected image
cv2.namedWindow('Green detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Green detected image', green_detected_image)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()