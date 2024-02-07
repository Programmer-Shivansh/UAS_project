import cv2 
import numpy as np
imge = cv2.imread('image_5/5.jpeg')
blur_image  = cv2.bilateralFilter(imge,9,75,75)

# blur = cv2.medianBlur(blur_image, 5)

grey_imge = cv2.cvtColor(blur_image,cv2.COLOR_BGR2GRAY)
# grey_imge = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
list =[]
l = []
l2 = []
for i in range(0,255):

    _, binary_imagee = cv2.threshold(grey_imge, i, 255, cv2.THRESH_BINARY)
    # blur = cv2.medianBlur(binary_imagee, 5)
    edged = cv2.Canny(binary_imagee, 100, 200) 
    # edged = cv2.Canny(blur_image, 100, 200) 
    # edged = cv2.Canny(blur, 100, 200) 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    if len(contours) ==1 :
        list.append(edged)
        l.append(binary_imagee)
        l2.append(hierarchy)
# print(len(l2))
if len(list) % 2  == 0:
    num = int((len(list))/2)
else :
    num = int((len(list)-1)/2)
for i in range(len(l)):
    print(l2[i])

cv2.waitKey(0)
cv2.destroyAllWindows()