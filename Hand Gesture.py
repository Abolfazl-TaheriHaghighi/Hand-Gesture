import cv2
import mediapipe as mp # type: ignore

Cap = cv2.VideoCapture(0)

while True:
    success , img = Cap.read()

    cv2.imshow("Image" , img)
    cv2.waitKey(1)
