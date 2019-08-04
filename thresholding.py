import cv2 as cv
import numpy as np

img = cv.imread('bookpage.jpg')

# This means the pixel above below twelve will be black
retval, threshold = cv.threshold(img, 12, 255, cv.THRESH_BINARY)

grayscaled = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
retval2, threshold2 = cv.threshold(grayscaled, 12, 255, cv.THRESH_BINARY)
gaus = cv.adaptiveThreshold(grayscaled, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
retval1, otsu = cv.threshold(grayscaled, 12, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


cv.imshow('original', img)
cv.imshow('threshold', threshold)
cv.imshow('thresholdi1', threshold2)
cv.imshow('Gaussian', gaus)
cv.imshow('Gaussian', otsu)
cv.waitKey(0)
cv.destroyAllWindows()
