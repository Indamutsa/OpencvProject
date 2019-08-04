import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    laplacian = cv.Laplacian(frame, cv.CV_64F)

    sobelx = cv.Sobel(frame, cv.CV_64F, 1,0, ksize=5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0,1, ksize=5)
    edges = cv.Canny(frame, 100, 200)

    cv.imshow('original', frame)
    cv.imshow('laplacian', laplacian)
    cv.imshow('sobelx', sobelx)
    cv.imshow('sobely', sobely) 
    cv.imshow('Edge', edges)


    k = cv.waitKey(5) & 0xFF

    if k == 27:
        break

cv.destroyAllWindows()
cap.release()
