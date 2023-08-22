# import openCV library
import cv2
# import numpy library
import numpy as np

# create a black image
image_bgr = np.zeros((512, 512, 3), np.uint8)

# drawing blue line
color = (255, 0, 0)
thickness = 5
cv2.line(image_bgr, (0, 0), (511, 511), color, thickness)

# drawing green rectangle
color = (0, 255, 0)
thickness = 3
cv2.rectangle(image_bgr, (384, 0), (510, 128), color, thickness)

# drawing red circle
color = (0, 0, 255)
thickness = -1
cv2.circle(image_bgr, (447, 63), 63, color, thickness)

# create new window title = Image
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Image', image_bgr)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()