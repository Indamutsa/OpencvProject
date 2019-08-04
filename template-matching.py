import numpy as np
import cv2 as cv

img_bgr = cv.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

template = cv.imread('opencv-template-for-matching.jpg', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshhold = 0.90
loc = np.where(res >= threshhold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv.imshow('detected', img_bgr)

cv.waitKey(0)
cv.destroyAllWindows()
