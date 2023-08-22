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

# convert color RGB -> HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# rang of orange color in HSV
# H -> 8 -> 12
# S -> 170 -> 255
# V -> 170 -> 255
orange_lower_hsv = np.array([8, 170, 170]) #([5, 120, 120])
orange_higher_hsv = np.array([12, 255, 255])
# mask for orange color
orange_mask = cv2.inRange(image_hsv, orange_lower_hsv, orange_higher_hsv)
orange_detected_image = cv2.bitwise_and(image_bgr, image_bgr, mask=orange_mask)

# create new window title = Orange detected image
cv2.namedWindow('Orange detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Orange detected image', orange_detected_image)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()