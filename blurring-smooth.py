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

    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv.filter2D(res, -1, kernel)
    blur = cv.GaussianBlur(res, (15,15), 0)
    median = cv.medianBlur(res, 15)
    bilateral = cv.bilateralFilter(res, 15, 75, 75)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow('Smoothed', smoothed)
    cv.imshow('blur', blur)
    cv.imshow('median', median)
    cv.imshow('Bilateral', bilateral)


    k = cv.waitKey(5) & 0xFF

    if k == 27:
        break

cv.destroyAllWindows()
cv.release()
