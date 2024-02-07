import cv2 
 
img = cv2.imread("Test_images/7.jpeg")
_, binary_imagee = cv2.threshold(img,200, 255, cv2.THRESH_BINARY)

# print(img)
print(binary_imagee)

cv2.imshow('img',binary_imagee)
cv2.waitKey(0)
cv2.destroyAllWindows()