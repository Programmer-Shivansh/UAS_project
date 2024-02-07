import cv2

img = cv2.imread('Test_E.png')

black = cv2.imread('black_img.png')

img = cv2.resize(img,(300,300))
black = cv2.resize(black,(300,300))

grey_black = cv2.cvtColor(black,cv2.COLOR_BGR2GRAY)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bitwise_xor = cv2.bitwise_xor(gray_img,grey_black)

cv2.imshow('img',bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()