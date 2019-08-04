'''
 * Python program to use contours to count the objects in an image.
 *
 * usage: python Contours.py <filename> <threshold>
'''
import cv2, sys
import numpy as np

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
image = cv2.imread(filename = filename)

# create binary image
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)
(t, binary) = cv2.threshold(src = blur,
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY)

# Exploring the contours
contours, hierarchy = cv2.findContours(image = binary, 
    mode = cv2.RETR_EXTERNAL,
    method = cv2.CHAIN_APPROX_SIMPLE)

print("Found %d objects." % len(contours))
for (i, c) in enumerate(contours):
    print("\tSize of contour %d: %d" % (i, len(c)))

cv2.drawContours(image = image, 
    contours = contours, 
    contourIdx = -1, 
    color = (0, 0, 255), 
    thickness = 5)

# Exploring the hierarchy
contours, hierarchy = cv2.findContours(image = binary, 
    mode = cv2.RETR_TREE,
    method = cv2.CHAIN_APPROX_SIMPLE)

# create all-black mask image
mask = np.zeros(shape = image.shape, dtype = "uint8")

for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)

    cv2.rectangle(img = mask, 
        pt1 = (x, y), 
        pt2 = (x + w, y + h), 
        color = (255, 255, 255), 
        thickness = -1)


'''
cv2.drawContours(image = image, 
    contours = contours, 
    contourIdx = -1, 
    color = (0, 0, 255), 
    thickness = 5)
'''
# apply mask to the original image
image = cv2.bitwise_and(src1 = image, src2 = mask)

dim = (700,500)

resized = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA) 

cv2.imshow("", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

