import cv2 as cv
import numpy as np

#program that finds edges of an image and the a rectangle that encases it

impath = "testPics\\polygons.png"

img = cv.imread(impath, 1)
imgrey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_, binimg = cv.threshold(imgrey,0,128,0) #returns a tuple, first variable there to avoid error

_, contours, _ = cv.findContours(binimg,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # returns tuple of 3

img = cv.drawContours(img, contours, -1, (0,255,0),1)

#fit rects around imgage
for i in contours:
    x,y,w,h = cv.boundingRect(i)
    img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

cv.imshow("china", img)
cv.waitKey()

