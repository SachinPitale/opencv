import cv2

image1=cv2.imread(filename='binnary1.png')
image2=cv2.imread(filename='binnary2.png')
image2=cv2.resize(src=image2,dsize=(144,144))
#final_image= cv2.bitwise_and(image1,image2)
#final_image= cv2.bitwise_or(image1,image2)
final_image= cv2.bitwise_not(image1,image2)
cv2.imshow('image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()