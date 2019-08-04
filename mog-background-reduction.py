import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
# cap = cv.VideoCapture('people-walking.mp4')
fgbg = cv.createBackgroundSubtractorMOG2()
# fgbg = cv.face.createLBPHFaceRecognizer()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
     
    cv.imshow('original', frame)
    cv.imshow('fg', fgmask)

    k = cv.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
