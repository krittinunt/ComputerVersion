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

# rang of red color in HSV
# red band 1 of 2
# H -> 0 -> 5
# S -> 80 -> 170
# V -> 80 -> 170
#
# red band 2 of 2
# H -> 170 -> 180
# S -> 175 -> 255
# V -> 20 -> 255

red_lower_hsv_1 = np.array([0, 80, 80])
red_higher_hsv_1 = np.array([5, 170, 170])

red_lower_hsv_2 = np.array([170, 175, 20])
red_higher_hsv_2 = np.array([180, 255, 255])

# mask for red color
red_mask_1 = cv2.inRange(image_hsv, red_lower_hsv_1, red_higher_hsv_1)
red_mask_2 = cv2.inRange(image_hsv, red_lower_hsv_2, red_higher_hsv_2)

red_detected_image = cv2.bitwise_and(image_bgr, image_bgr, mask=red_mask_1+red_mask_2)

# create new window title = Red detected image
cv2.namedWindow('Red detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Red detected image', red_detected_image)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()