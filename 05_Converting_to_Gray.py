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

# image info
dimensions = image_bgr.shape
# print info
print('Image dimension    : ', dimensions)

# convert color RGB -> Gray
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# create new window title = Gray image
cv2.namedWindow('Gray image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Gray image', image_gray)

# image info
dimensions = image_gray.shape
# print info
print('Gray image dimension    : ', dimensions)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()