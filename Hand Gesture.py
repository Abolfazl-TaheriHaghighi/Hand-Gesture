import cv2
import mediapipe as mp # type: ignore

Cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success , img = Cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image" , img)
    cv2.waitKey(1)
