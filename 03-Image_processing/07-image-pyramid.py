import cv2

image = cv2.imread(filename="ms.jpg")

for i in range(5):
    #image = cv2.pyrDown(image) # reduce the dimension of image

    image=cv2.pyrUp(image)
    cv2.imshow('my image window', image)



    cv2.waitKey(0)

cv2.destroyAllWindows()