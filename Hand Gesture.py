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

        hand = results.multi_hand_landmarks [0]
        mp.solutions.drawing_utils.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
        
        lmlist = []


        for id , lm in enumerate(hand.landmark):
            a , b , c = img.shape
            zx, zy = int(lm.x * b), int(lm.y * a)
            lmlist.append([id, zx , zy])


        if len(lmlist) > 0:
            x1 , y1 = lmlist[4][1], lmlist[4][2]
            x2 , y2 = lmlist[8][1], lmlist[8][2]
            cx , cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 6, (185, 4 , 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 6, (185, 4 , 0), cv2.FILLED)
            cv2.circle(img, (cx, cy), 6, (185, 4 , 0), cv2.FILLED)
            cv2.line(img , (x1, y1), (x2 , y2), (255 , 255 , 0), 2)



    cv2.imshow("Image" , img)
    cv2.waitKey(1)
