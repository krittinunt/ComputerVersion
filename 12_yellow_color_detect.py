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

# rang of yellow color in HSV
# H -> 18 -> 39
# S -> 100 -> 255
# V -> 100 -> 255
yellow_lower_hsv = np.array([18, 100, 180])
yellow_higher_hsv = np.array([39, 255, 255])
# mask for yellow color
yellow_mask = cv2.inRange(image_hsv, yellow_lower_hsv, yellow_higher_hsv)
yellow_detected_image = cv2.bitwise_and(image_bgr, image_bgr, mask=yellow_mask)

# create new window title = Yellow detected image
cv2.namedWindow('Yellow detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Yellow detected image', yellow_detected_image)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()