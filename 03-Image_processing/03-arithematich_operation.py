import cv2

image1=cv2.imread(filename='ms.jpg',flags=1)
image2=cv2.imread(filename='msd.jpg',flags=1)
image2=cv2.resize(src=image2,dsize=(612,379))
#final_image=cv2.add(src1=image1,src2=image2)
#final_image=cv2.divide(src1=image1,src2=image2,scale=380)
final_image=cv2.multiply(src1=image1,src2=image2)
cv2.imshow('image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()