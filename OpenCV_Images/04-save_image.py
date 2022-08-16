import cv2

image = cv2.imread(filename='ms.jpg',flags=0)

print(image.shape)

resize_image=cv2.resize(src=image,dsize=(0,0), fx=0.5, fy=0.5)
print(resize_image.shape)
cv2.imwrite(filename='resize_image.jpg', img=resize_image)  # save the image

cv2.imshow('my window', resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
