# import openCV library
import cv2

# image file path
path = 'color_ball.jpg'
# read image
image_bgr = cv2.imread(path, cv2.IMREAD_COLOR)

# create new window title = Display image
cv2.namedWindow('Display image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Display image', image_bgr)

# split blue channel
blue_channel = image_bgr[:, :, 0];
# create new window title = Blue channel image
cv2.namedWindow('Blue channel image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Blue channel image', blue_channel)

# split green channel
green_channel = image_bgr[:, :, 1];
# create new window title = Green channel image
cv2.namedWindow('Green channel image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Green channel image', green_channel)

# split red channel
red_channel = image_bgr[:, :, 2];
# create new window title = Red channel image
cv2.namedWindow('Red channel image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Red channel image', red_channel)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()

