# import openCV library
import cv2
# import numpy library
import numpy as np
# import time library
import time

# video file path
path = 'ball_colorful.mp4'
# config camera id
#camera_id = 1
# create video capture
vcap = cv2.VideoCapture(path)

# check camera
if not vcap.isOpened():
    raise Exception('Could not open video device or video file')

# get and print video info
video_width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
video_height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
video_fps = vcap.get(cv2.CAP_PROP_FPS)
video_frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
print('Width = ' + str(video_width))
print('Height = ' + str(video_height))
print('FPS = ' + str(video_fps))
print('Frame count = ' + str(video_frame_count))

# variable for check FPS
start_time = time.time()
display_time = 2
fc = 0
FPS = 0
frame_rate = 2
prev = 0

while True:
    # capture frame
    ret, frame = vcap.read()
    
    # exit can't read frame
    if not ret:
        break
    
    # calc FPS
    fc += 1
    TIME = time.time() - start_time
    if (TIME) >= display_time:
        FPS = fc / (TIME)
        fc = 0
        start_time = time.time()
        FPS = int(FPS)
    # put FPS to frame
    fps_disp = "FPS: " + str(FPS)#[:5]
    frame = cv2.putText(frame, fps_disp, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # display frame
    cv2.imshow('Frame', frame)
    
    # press key 'q' for quit
    if cv2.waitKey(1) == ord('q'):
        break
    
# release video capture
vcap.release()
# close all window
cv2.destroyAllWindows()