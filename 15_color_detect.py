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

# rang of green color in HSV
# H -> 38 -> 93
# S -> 50 -> 255
# V -> 50 -> 255
green_lower_hsv = np.array([38, 50, 50])
green_higher_hsv = np.array([93, 255, 255])

# rang of yellow color in HSV
# H -> 18 -> 39
# S -> 100 -> 255
# V -> 180 -> 255
yellow_lower_hsv = np.array([18, 100, 180])
yellow_higher_hsv = np.array([39, 255, 255])

# rang of orange color in HSV
# H -> 8 -> 12
# S -> 170 -> 255
# V -> 170 -> 255
orange_lower_hsv = np.array([8, 170, 170])
orange_higher_hsv = np.array([12, 255, 255])

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


# mask for blue color
blue_mask = cv2.inRange(image_hsv, blue_lower_hsv, blue_higher_hsv)

# mask for green color
green_mask = cv2.inRange(image_hsv, green_lower_hsv, green_higher_hsv)

# mask for yellow color
yellow_mask = cv2.inRange(image_hsv, yellow_lower_hsv, yellow_higher_hsv)

# mask for orange color
orange_mask = cv2.inRange(image_hsv, orange_lower_hsv, orange_higher_hsv)

# mask for red color
red_mask_1 = cv2.inRange(image_hsv, red_lower_hsv_1, red_higher_hsv_1)
red_mask_2 = cv2.inRange(image_hsv, red_lower_hsv_2, red_higher_hsv_2)
red_mask = red_mask_1 + red_mask_2


# fine contours in blue mask
blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# fine contours in green mask
green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# fine contours in yellow mask
yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# fine contours in orange mask
orange_contours, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# fine contours in red mask
red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# loop blue_contours draw rectangle
for cnt in blue_contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image_bgr, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
# loop green_contours draw rectangle
for cnt in green_contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image_bgr, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
# loop yellow_contours draw rectangle
for cnt in yellow_contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(image_bgr, 'Yellow', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        
# loop orange_contours draw rectangle
for cnt in orange_contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 165, 255), 2)
        cv2.putText(image_bgr, 'Orange', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2)
        
# loop red_contours draw rectangle
for cnt in red_contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image_bgr, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

# create new window title = Color detected image
cv2.namedWindow('Color detected image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Color detected image', image_bgr)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()