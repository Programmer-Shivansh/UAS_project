import os
import cv2

folder = os.chdir("More Accurate Images")
images = os.listdir(folder)
for image in images:
    if image.endswith("jpeg"):

        img = cv2.imread(image)
        _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)
        thresh_gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
        _, final_image = cv2.threshold(thresh_gray, 85, 255, cv2.THRESH_BINARY)
        if (final_image[0][0]) == 255:
            final_image = cv2.bitwise_not(final_image)

        cv2.imshow(f"more_result_{image}", final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
