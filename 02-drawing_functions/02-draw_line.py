import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

point_1=(290,20)
point_2=(410,20)

#BGR
color=(0,255,0)
thickness = 5

image_new=cv2.line(img=image,pt1=point_1,pt2=point_2,thickness=thickness,color=color)
image_new=cv2.arrowedLine(img=image_new,pt1=(10,250),pt2=(250,350),thickness=thickness,color=color)
cv2.imshow('my window', image_new)
cv2.waitKey(0)
cv2.destroyAllWindows()