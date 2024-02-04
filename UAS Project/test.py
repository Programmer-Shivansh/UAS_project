import cv2

e = cv2.imread("E.png", 0)
_, ne = cv2.threshold(e, 50, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("img2",e)
cv2.imshow("img1", ne)
cv2.waitKey(0)
cv2.destroyAllWindows()
