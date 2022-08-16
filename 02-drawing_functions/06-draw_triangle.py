import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

point1=(150,200)
point2=(100,250)
point3=(300,360)
cv2.line(img=image,pt1=point1,pt2=point2,color=(0,255,0),thickness=5)
cv2.line(img=image,pt1=point2,pt2=point3,color=(0,255,0),thickness=5)
cv2.line(img=image,pt1=point3,pt2=point1,color=(0,255,0),thickness=5)

cv2.imshow('my window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()