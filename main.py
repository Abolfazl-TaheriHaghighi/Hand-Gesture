import cv2
import mediapipe as mp # type: ignore
import math
import numpy as np

Cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
draw = mp.solutions.drawing_utils



from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(-65.25, None)


vol_range = volume.GetVolumeRange()
minVol = vol_range[0]
maxVol = vol_range[1]

while True:
    success , img = Cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks [0]
        draw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

        
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

            Distance = int(math.hypot(x2 - x1 , y2 - y1))
            handsrange = [25 , 300]

            vol = np.interp(Distance, [25, 200], [minVol, maxVol])
            vol_bar = np.interp(Distance, [25, 200], [400, 150])
            vol_per = np.interp(Distance, [25, 200], [0, 100])
            volume.SetMasterVolumeLevel(vol , None)

            cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 2)
            cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(vol_per)} %', (40, 430), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 0), 3)

            #print(Distance)



    cv2.imshow("Image" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Cap.release()
cv2.destroyAllWindows()



# Abolfazl Taheri Haghighi
# Bachelor's student of statistics at Fasa University
# Volume Control with Hand Gestures
# Version: v1.1.0