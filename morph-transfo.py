import cv2 as cv
import numpy as np

# Getting the video of the webcam
cap = cv.VideoCapture(0)

#================================== Morphoological transformations ===============================
# --------------- Erosion and dilation -----------------------------

while True:
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([150,150,30])
    upper_red = np.array([180,255,200])

    mask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv.erode(mask, kernel, iterations = 1 )
    dilation = cv.dilate(mask, kernel, iterations = 1 )

    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    

    # it is the difference between input and opening of the image
    # cv.imshow('Tophat', tophat)

    # It is the difference between the closing of the input image and input image 
    # cv.imshow('Blackhat', blackhat)


    cv.imshow("frame", frame)
    cv.imshow("res", res)
    cv.imshow("erosion", erosion )
    cv.imshow("dilation", dilation)

    cv.imshow('opening', opening)
    cv.imshow('dilation', dilation)

    k = cv.waitKey(5) & 0xFF

    if k == 27:
        break

cv.destroyAllWindows()
cv.release()
