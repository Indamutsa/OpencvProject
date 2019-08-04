import cv2 as cv
import numpy as np

img = cv.imread('opencv-corner-detection-sample.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x,y), 3, 255, -1)

cv.imshow('Corner', img)

cv.waitKey(0)
cv.destroyAllWindows()

