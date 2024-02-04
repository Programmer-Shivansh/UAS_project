
import cv2

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated

img = cv2.imread('E.png')

new_img = rotate(img,90)

cv2.imshow('rotated',new_img)

cv2.waitKey(0)

cv2.destroyAllWindows()