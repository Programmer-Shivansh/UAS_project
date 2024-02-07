import os
import cv2 
import numpy as np
folder =os.chdir("Test_images")
folders = os.listdir(folder)
# l = []
def show_output(img):
    image = cv2.imread(img)
    _, thresh = cv2.threshold(image, 100, 255, cv2.THRESH_TRUNC)
    gray_thresh = cv2.cvtColor(thresh,cv2.COLOR_BGR2GRAY)
    l = []
    for i in range(50,255):

        _, thresh_binary = cv2.threshold(gray_thresh, i, 255, cv2.THRESH_BINARY)
        edged = cv2.Canny(thresh_binary, 100, 200)
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) == 3 :
            l.append(thresh_binary)
    print(len(l))
    if len(l) % 2  == 0:
        num = int((len(l))/2)
    else:
        num = int((len(l)-1)/2)
    if num != 0 :
        final_image = l[num]
        if (final_image[0][0])== 255 :
            final_image = cv2.bitwise_not(final_image)
        cv2.imshow(f'{img}',final_image)
        cv2.waitKey(0)
for image in folders :
    if image.endswith('png') or image.endswith('jpeg') :
        show_output(image)

 