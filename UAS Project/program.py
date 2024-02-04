import numpy as np 
import cv2

test =cv2.imread('Test.png',0)
e = cv2.imread('E.png',0)
height, width = (e).shape
methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
for method in methods :
    image = test.copy()
    result = cv2.matchTemplate(image,e,method)
    min_value, max_value , min_loc,max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + width,location[1]+height)
    cv2.rectangle(image,location,bottom_right,(0,0,0),3)
    cv2.imshow("Match",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
