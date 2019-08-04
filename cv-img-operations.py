import numpy as np
import cv2 as cv

img = cv.imread('watch.jpg', cv.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]


#print(px)

# Region of image
#roi = img[100:150, 100:150]
#print(roi)

img[100:150, 100:150] = [255, 255, 255]

watch_face = img[37:111, 107:194]

# The numbers below, is the difference of the numbers above
img[0:74, 0:87] = watch_face


cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
