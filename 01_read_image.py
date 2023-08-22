# import openCV library
import cv2

# image file path
path = 'color_ball.jpg'
# read image
image_bgr = cv2.imread(path, cv2.IMREAD_UNCHANGED)


# create new window title = Display image
cv2.namedWindow('Display image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Display image', image_bgr)
# wait any key
cv2.waitKey(0)

# close all window
cv2.destroyAllWindows()