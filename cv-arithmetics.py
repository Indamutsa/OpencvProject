import cv2 as cv
import numpy as np

img1 = cv.imread('3D-Matplotlib.png')
img2 = cv.imread('mainlogo.png')
                                                             # ++++++++++++++ Superposing images above one another
# ============== Resizing the image ============
print(img2.shape)
scale_percent = 100 # Percent of original size

width = int(img2.shape[1] * scale_percent / 100 )
height = int(img2.shape[0] * scale_percent / 100 )
dim = ( width, height )

# Resize image
resized = cv.resize(img2, dim, interpolation = cv.INTER_AREA)


img2 = resized

print('Resized dimensions : ', img2.shape)
# ==============================================

#img2 = cv.imread('mainsvmimage.png')

# Adding two images together
#add = img1 + img2

#Another method
#add = cv.add(img1, img2)

# Using weight
#weighted = cv.addWeighted(img1, 0.6, img2, 0.4, 0)

# We are going to make a transparent image

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 220, 255, cv.THRESH_BINARY_INV)

# Make it invisible
mask_inv = cv.bitwise_not(mask)

# The background is black, we changed it back to white
cv.imshow("imahdh", mask)


img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('res', img1)
cv.imshow('mask_inv', mask_inv)
cv.imshow('img_bg', img1_bg)
cv.imshow('img2_fg', img2_fg)
cv.imshow('dst', dst)

#cv.imshow('weighted', weighted)
cv.waitKey(0)
cv.destroyAllWindows()

