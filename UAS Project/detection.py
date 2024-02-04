import cv2 
import numpy as np 
  
def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated
# Read the main image 
img_rgb = cv2.imread('Test_C.png') 
  
# Convert it to grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
  
# Read the template 
template = cv2.imread('C.png', 0) 

# list= []
# Store width and height of template in w and h 
w, h = template.shape[::-1] 
max = 0 
for i in range(360):
    template = rotate(template,i)
# Perform match operations. 
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED) 
    threshold = 0.15
    loc = np.where(res >= threshold) 

    # if np.where(res >= 0.1) is True :
    #     print(i)
    # list.append(res)
    i += 1
  
# print(len(list))
# print((list)[30])
# Specify a threshold 
# list.sort()
# threshold = 0.58
  
# Store the coordinates of matched area in a numpy array 
# loc = np.where(res >= threshold) 
# loc = np.where(list[-1]) 
print(len(loc))
# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    # print("1")
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2) 
  
# Show the final image with the matched area. 
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()