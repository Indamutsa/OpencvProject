import cv2 as cv
import numpy as np

# Getting the video of the webcam
cap = cv.VideoCapture(0)


while True:
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([150,150,30])
    upper_red = np.array([180,255,200])

    mask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask=mask)

    k = cv.waitKey(5) & 0xFF

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow('res', res)

    if k == 27:
        break

cv.destroyAllWindows()
cv.release()
