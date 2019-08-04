import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# In case we want to ouput the video
fourcc = cv.VideoWriter_fourcc(*'XVID')

# Specification of the format
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # We read in the video, ret will be true if the video is captured
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    out.write(frame)
    
    # We show the image
    cv.imshow('frame',frame)
    cv.imshow('gray', gray)
    
    # When we press q, we will exit 
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

