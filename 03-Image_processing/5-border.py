import cv2

image=cv2.imread(filename='ms.jpg',flags=1)
image=cv2.copyMakeBorder(image,top=100,bottom=50,left=30,right=0, borderType=cv2.BORDER_ISOLATED)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()