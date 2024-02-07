import os
import cv2 
import numpy as np
folder =os.chdir("Test_images")
folders = os.listdir(folder)
# l = []
for image in folders :
    if image.endswith('png') or image.endswith('jpeg') :
        img = cv2.imread(image)
        _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)
        thresh = cv2.cvtColor(thresh,cv2.COLOR_BGR2GRAY)
        _, thresh_binary = cv2.threshold(thresh, 85, 255, cv2.THRESH_BINARY)

        # edged = cv2.Canny(thresh, 100, 200)
        # contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.imshow(f"{image}", thresh_binary)
        cv2.waitKey(0)
cv2.destroyAllWindows()
