# import openCV library
import cv2

# image file path
path = 'color_ball.jpg'
# read image
image_bgr = cv2.imread(path, cv2.IMREAD_UNCHANGED)

# create new window title = RGB image
cv2.namedWindow('RGB image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('RGB image', image_bgr)

# image dimensions info
dimensions = image_bgr.shape
# print dimensions info
print('Image dimension    : ', dimensions)

# convert color RGB -> HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# create new window title = HSV image
cv2.namedWindow('HSV image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('HSV image', image_hsv)

# image dimensions info
dimensions = image_hsv.shape
# print dimensions info
print('Image dimension    : ', dimensions)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()