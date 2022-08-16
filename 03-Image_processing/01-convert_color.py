import cv2

image = cv2.imread(filename='ms.jpg',flags=1)
image = cv2.cvtColor(src=image,code=cv2.COLOR_BGR2RGB)
cv2.imshow('window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()