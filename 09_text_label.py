# import openCV library
import cv2
# import numpy library
import numpy as np

# create a black image
image_bgr = np.zeros((512, 512, 3), np.uint8)

# set font
font = cv2.FONT_HERSHEY_SIMPLEX
# set font scale
fontscale = 3
# set color
color = (0, 255, 0)
# set thickness
thickness = 10
# put 'OpenCV' text
image_bgr = cv2.putText(image_bgr, 'OpenCV', (70, 120), font, fontscale, color, thickness, cv2.LINE_AA)


# set font scale
fontscale = 1
# set color
color = (0, 0, 255)
# set thickness
thickness = 3
# put 'SRTC' text
image_bgr = cv2.putText(image_bgr, 'SRTC', (320, 160), font, fontscale, color, thickness, cv2.LINE_AA)


# set font scale
fontscale = 0.5
# set color
color = (0, 255, 255)
# set thickness
thickness = 1
# put 'By Krittinunt' text
image_bgr = cv2.putText(image_bgr, 'By Krittinunt', (215, 160), font, fontscale, color, thickness, cv2.LINE_AA)

# create new window title = Image
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Image', image_bgr)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()