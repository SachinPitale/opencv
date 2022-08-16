import cv2
import numpy as np

image = cv2.imread(filename="ms.jpg")
print(image.shape)

height=image.shape[0]
width=image.shape[1]
dsize=(height,width)
m=np.float32([[1,0,10] , [0,1,10]])

shifting=cv2.warpAffine(src=image,dsize=dsize,M=m)

cv2.imshow('my image window', image)
cv2.imshow('shifting', shifting) # display image


cv2.waitKey(0)

cv2.destroyAllWindows()