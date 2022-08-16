import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

start_point=(250,20)
end_point=(400,170)
thickness=5
color=(0,255,0)


new_image = cv2.rectangle(img=image,pt1=start_point,pt2=end_point,thickness=thickness,color=color)
cv2.imshow('my window', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()