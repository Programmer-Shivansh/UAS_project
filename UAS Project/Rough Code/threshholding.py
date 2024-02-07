import cv2 
# imgc = cv2.imread('Test_C.png')
imgc = cv2.imread('C.png')
imge = cv2.imread('C.png')

grey_imgc = cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
grey_imge = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)

_, binary_imagec = cv2.threshold(grey_imgc, 80, 255, cv2.THRESH_BINARY_INV)
_, binary_imagee = cv2.threshold(grey_imge, 100, 255, cv2.THRESH_BINARY)

actuall_img = binary_imagec

cv2.imshow('c',binary_imagec)
cv2.imshow('e',binary_imagee)
cv2.waitKey(0)
cv2.destroyAllWindows()