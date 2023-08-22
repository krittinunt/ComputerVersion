import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

webcam = cv2.VideoCapture(1)
image = webcam.read()
while True:
    success, image = webcam.read()    
    image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, landmark, mp_hands.HAND_CONNECTIONS)
            #mp_draw.draw_landmarks(image, landmark)

    cv2.imshow("Image",image)
    cv2.waitKey(1)