import cv2 
import numpy as np
imge = cv2.imread('More Accurate Images/5.jpeg')
# black_img = cv2.imread("black_img.png")
# result =cv2.imread('1.jpeg')
# h,w,ch = imge.shape
# black_img = cv2.resize(black_img,(h,w))
# black_img = cv2.cvtColor(black_img,cv2.COLOR_BGR2GRAY)
     
grey_imge = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
list =[]
l = []
# c=[]
for i in range(50,255):

    _, binary_imagee = cv2.threshold(grey_imge, i, 255, cv2.THRESH_TRUNC)
    # blur_image  = cv2.bilateralFilter(binary_imagee,9,75,75)
# blur_image  = cv2.bilateralFilter(binary_imagee,9,75,75)
    # blur = cv2.medianBlur(blur_image, 5)
    edged = cv2.Canny(binary_imagee, 100, 200) 
    # edged = cv2.Canny(blur, 100, 200) 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # print(contours)
    if len(contours) ==4 :
        list.append(edged)
        l.append(binary_imagee)
        # c.append(contours)

        # cv2.imshow('successnno',edged)
        # cv2.imshow('success',binary_imagee)
        # cv2.waitKey(0
        # break 
# print(len(list))
# for x in range(len(list)):
#     cv2.imshow(f'{x}',list[x])
# print(len(c)) 
if len(list) % 2  == 0:
    num = int((len(list))/2)
    # print(num)
else :
    num = int((len(list)+1)/2)
    # print(int(num))

for i in range(len(l)):
    cv2.imshow(f'{i}',l[i])
    cv2.waitKey(0)
cv2.destroyAllWindows()