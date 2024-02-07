import os
import cv2 
import numpy as np

image = cv2.imread('Test_images/5.jpeg')
_, thresh = cv2.threshold(image, 100, 255, cv2.THRESH_TRUNC)
thresh = cv2.cvtColor(thresh,cv2.COLOR_BGR2GRAY)
_, thresh_binary = cv2.threshold(thresh, 85, 255, cv2.THRESH_BINARY)
edged = cv2.Canny(thresh, 100, 200)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow("k", thresh_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()