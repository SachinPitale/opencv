import cv2

image = cv2.imread(filename='ms.jpg', flags=1)

print(image.shape)
widht=500
height=250
dimension=(widht,height)
#resize_image = cv2.resize(src=image, dsize=(dimension))

# fx => width
# fy => height
resize_image = cv2.resize(src=image, dsize=(0,0), fx=0.5, fy=0.5)
print(resize_image.shape)
cv2.imshow("image window", resize_image)
cv2.im
cv2.waitKey(0)
cv2.destroyAllWindows()
