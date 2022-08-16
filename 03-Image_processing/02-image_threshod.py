import cv2

image = cv2.imread(filename='ms.jpg',flags=1)

# THRESH_BINARY = > pixel >= threshold =255 : 0
# THRESH_BINARY_INV => pixel >= threshold = 0 :255
# Thresh_TRUNC => Pixel => threshold  value = threshold value


ret, thresh = cv2.threshold(src=image,thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow('window', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()