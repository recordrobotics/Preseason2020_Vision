import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #cv.blur(frame, frame)
    lower_color = np.array([90, 100,50])
    upper_color = np.array([120,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_color, upper_color)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()