import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

center = (100,100) # width * height
axes = (50,50)
angle = 0
start_angle=0
end_angle=180
thickness=5
color=(0,255,0)
new_image=cv2.ellipse(img=image,angle=angle,center=center,axes=axes,startAngle=start_angle,color=color,thickness=thickness,endAngle=end_angle)

cv2.imshow('my window', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()