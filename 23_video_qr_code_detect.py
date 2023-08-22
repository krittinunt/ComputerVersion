# import openCV library
import cv2
# import numpy library
import numpy as np
# import time library
import time

# video file path
#path = ''
# config camera id
camera_id = 1
# config ip camera
#ip_camera = 'rtsp://192.168.22.80:8080/h264_pcm.sdp'

# create video capture for video file
#vcap = cv2.VideoCapture(path)
# create video capture for webcam
vcap = cv2.VideoCapture(camera_id)
# create video capture for ip camera
#vcap = cv2.VideoCapture(ip_camera)

# check camera
if not vcap.isOpened():
    raise Exception('Could not open video device or video file')

# camera id config video size and FPS
# Logitech c922 : width = 854, height = 480
# Logitech c270 : width = 320, height = 240
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 854)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# FPS : 5, 10, 15, 20, 25, 30.....
vcap.set(cv2.CAP_PROP_FPS, 5)

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

qrcode_detect = cv2.QRCodeDetector()

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

    # display frame
    #cv2.imshow('frame', frame)
    
    if ret:
        retval, decoded_info, points, straight_qrcode = qrcode_detect.detectAndDecodeMulti(frame)

        if retval:
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                
                frame = cv2.polylines(frame, points.astype(int), True, color, 3)
                frame = cv2.putText(frame, s, p[0].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
        # put FPS to frame
        fps_disp = "FPS: " + str(FPS)#[:5]
        frame = cv2.putText(frame, fps_disp, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # display frame
        cv2.imshow('QR code', frame)

    # press key 'q' for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture
vcap.release()
# close all window
cv2.destroyAllWindows()