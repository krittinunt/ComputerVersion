# import openCV library
import cv2

# file path
path = 'qrcode.jpg'
#path = 'qrcode.png'
image_bgr = cv2.imread(path)

# display image
cv2.imshow('Image', image_bgr)

qrcode_detect = cv2.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = qrcode_detect.detectAndDecodeMulti(image_bgr)

if retval:
    print('Decode info : ', decoded_info)
    print('Points : ', points)

    image_bgr = cv2.polylines(image_bgr, points.astype(int), True, (0, 255, 0), 3)
    
    for s, p in zip(decoded_info, points):
        image_bgr = cv2.putText(image_bgr, s, p[0].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # display image
    cv2.imshow('QR code', image_bgr)

    # wait any key
    cv2.waitKey(0)
else:
    print('No QR code.')
# close all window
cv2.destroyAllWindows()