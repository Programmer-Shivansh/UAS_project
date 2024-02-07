import cv2 
import numpy as np
imge = cv2.imread('Test_C.png')
# black_img = cv2.imread("black_img.png")
result =cv2.imread('result_c.png')
# h,w,ch = imge.shape
# black_img = cv2.resize(black_img,(h,w))
# black_img = cv2.cvtColor(black_img,cv2.COLOR_BGR2GRAY)

grey_imge = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
list =[]
l = []
# c=[]
for i in range(50,255):

    _, binary_imagee = cv2.threshold(grey_imge, i, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(binary_imagee, 100, 200) 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # print(contours)
    if len(contours) ==1 :
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


image = l[num]
# print(image[0][0])
if (image[0][0])== 255 :
    final_image = cv2.bitwise_not(image)
else :
    final_image = image
cv2.imshow("success",final_image)
cv2.imshow("result",result)
# image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
# print(image)
# print(l[num])

# cont = cv2.drawContours(imge ,(c[num]),-1,(0,0,0),1,cv2.LINE_AA)

# com = cv2.addWeighted(cont,1,black_img,1,0)

# cv2.imshow("img",cont)
# bitwise_not = cv2.bitwise_not(image)

# bitwise_and = cv2.bitwise_and(bitwise_not,grey_imge)
# bitwise_or = cv2.bitwise_or(list[num],grey_imge)
# bitwise_xor = cv2.bitwise_xor(list[num],grey_imge)
# cv2.imshow('img',bitwise_xor)
# cv2.imshow('img',bitwise_or)
# cv2.imshow('img',bitwise_not)
# cv2.imshow('main',grey_imge)

# cv2.imshow("image",imge)
# cv2.imshow('img',bitwise_and)
# combined =cv2.addWeighted(image,1,imge,1,0)
# cv2.imshow('1',bitwise_not)
# cv2.imshow('2',l[num])
# cv2.imshow('comb',combined)
cv2.waitKey(0)
cv2.destroyAllWindows()