import cv2 
import numpy as np
imge = cv2.imread('Test_images/7.jpeg')
# result =cv2.imread('result_c.png')


grey_imge = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
# list =[]
l = []
for i in range(50,255):

    _, binary_imagee = cv2.threshold(grey_imge, i, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(binary_imagee, 100, 200) 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    if len(contours) ==1 :
        # list.append(edged)
        l.append(binary_imagee)
print(len(l))
if len(l) % 2  == 0:
    num = (int((len(l))/2) - 1)
else :
    num = (int((len(l)+1)/2) -1 )


image = l[num]
if (image[0][0])== 255 :
    final_image = cv2.bitwise_not(image)
else :
    final_image = image
for x in range(len(l)):
    cv2.imshow(f"{x}",l[x])
# cv2.imshow("success",final_image)
# cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()