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
# display image
cv2.imshow('RGB image', image_bgr)

# convert color RGB -> HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# rang of blue color in HSV
# H -> 90 -> 120
# S -> 117 -> 255
# V -> 84 -> 255
blue_lower_hsv = np.array([90, 117, 84])
blue_higher_hsv = np.array([120, 255, 255])
# mask for blue color
blue_mask = cv2.inRange(image_hsv, blue_lower_hsv, blue_higher_hsv)
blue_detected_image = cv2.bitwise_and(image_bgr, image_bgr, mask=blue_mask)

# create new window title = Blue detected image
cv2.namedWindow('Blue detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Blue detected image', blue_detected_image)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()