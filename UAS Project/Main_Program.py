import os
import cv2

folder = os.chdir("Test_images")
folders = os.listdir(folder)


def main_output(img, len_contour=1):
    image = cv2.imread(img)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_list = []
    for i in range(50, 255):
        _, binary_image = cv2.threshold(grey_image, i, 255, cv2.THRESH_BINARY)
        blur_image = cv2.bilateralFilter(binary_image, 9, 75, 75)
        blur = cv2.medianBlur(blur_image, 5)
        edged = cv2.Canny(blur, 100, 200)
        contours, hierarchy = cv2.findContours(
            edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        if len(contours) == len_contour:
            image_list.append(binary_image)
    if len_contour == 1:
        if len(image_list) < 15:
            main_output(img, len_contour=4)
        else:
            if len(image_list) % 2 == 0:
                num = int((len(image_list)) / 2)
            else:
                num = int((len(image_list) - 1) / 2)
            final_image = image_list[num]
            if (final_image[0][0]) == 255:
                final_image = cv2.bitwise_not(final_image)
            cv2.imshow(f"result_{img}", final_image)
            cv2.waitKey(0)
    else:
        if len(image_list) % 2 == 0:
            num_more = int((len(image_list)) / 2)
        else:
            num_more = int((len(image_list) - 1) / 2)
        if num_more != 0:
            final_image = image_list[num_more]
            if (final_image[0][0]) == 255:
                final_image = cv2.bitwise_not(final_image)
            cv2.imshow(f"result_{img}", final_image)
            cv2.waitKey(0)


for image in folders:
    if image.endswith("png") or image.endswith("jpeg"):
        main_output(image)
        
cv2.destroyAllWindows()
