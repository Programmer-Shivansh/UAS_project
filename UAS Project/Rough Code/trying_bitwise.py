
import cv2

black_img = cv2.imread("black_img.png")
white_img = cv2.imread("white_img.png")

black_img = cv2.resize(black_img,(300,300))
white_img = cv2.resize(white_img,(300,300))
# black_img = cv2.cvtColor(black_img,cv2.COLOR_BGR2GRAY)
# white_img = cv2.cvtColor(white_img,cv2.COLOR_BGR2GRAY)

bit_and = cv2.bitwise_and(white_img,black_img)
bit_or = cv2.bitwise_or(white_img,black_img)
cv2.imshow('and',bit_and)
cv2.imshow('or',bit_or)

cv2.waitKey(0)

cv2.destroyAllWindows()
