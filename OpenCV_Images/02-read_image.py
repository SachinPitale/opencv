import cv2

# To read image in color format which doesn't include alpha channel  =1. cv2.IMREAD_COLORD
# To read image in grayscale = 0 cv2.IMREAD_GRAYSCALE
# To read image as it is including alpha channel =-1  cv2.IMREAD_UNCHANGED

image = cv2.imread(filename='ms.jpg',flags=0)

cv2.imshow("pic", image)
print(image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
