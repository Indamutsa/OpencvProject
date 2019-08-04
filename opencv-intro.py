import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('watch.jpg', cv.IMREAD_GRAYSCALE) # IMREAD_GRAYSCALE(0), IMREAD_COLOR(1), IMREAD_UNCHANGED(-1)

# We can use cv to show the image
'''
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
#we can use plt as well
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [80, 100], 'c', linewidth=5)
plt.show()
'''

cv.imwrite('watchgray.png', img)
