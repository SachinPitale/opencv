import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

center=(335,85)
radius = 65
color = (255,0,0)
thickness = 5

new_image=cv2.circle(img=image,radius=radius,color=color,thickness=thickness,center=center)
new_image=cv2.circle(img=new_image,radius=radius,color=color,thickness=thickness,center=(335,300))
cv2.imshow('my window', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()