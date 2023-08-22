# import openCV library
import cv2

# image file path
path = 'color_ball.jpg'
# read image
image_bgr = cv2.imread(path, cv2.IMREAD_UNCHANGED)

# create new window title = Original image
cv2.namedWindow('Original image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Original image', image_bgr)

# image info
dimensions = image_bgr.shape
height = image_bgr.shape[0]
width = image_bgr.shape[1]
channels = image_bgr.shape[2]

# print info
print('Original image dimension    : ', dimensions)
print('Original image height       : ', height)
print('Original image width        : ', width)
print('Original number of channels : ', channels)

# calculate resized image
scale_percent = 50
height = int(image_bgr.shape[0] * (scale_percent / 100))
width = int(image_bgr.shape[1] * (scale_percent / 100))
dim = (width, height)

# resized image from image
resized = cv2.resize(image_bgr, dim, interpolation = cv2.INTER_AREA)
# create new window title = Resized image
cv2.namedWindow('Resized image', cv2.WINDOW_AUTOSIZE)
# display image
cv2.imshow('Resized image', resized)

# image info
dimensions = resized.shape
height = resized.shape[0]
width = resized.shape[1]
channels = resized.shape[2]

# print info
print('Resized image dimension    : ', dimensions)
print('Resized image height       : ', height)
print('Resized image width        : ', width)
print('Resized number of channels : ', channels)

# wait any key
cv2.waitKey(0)
# close all window
cv2.destroyAllWindows()