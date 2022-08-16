import cv2

image = cv2.imread(filename="ms.jpg")
#image[0:100,0:100]=255
image[0:100,0:100]=[128,0,0]
print(image[0:100,0:100])

cv2.imshow('my image window', image)  # display image

cv2.waitKey(10000) # To keep window till 10 second

# cv2.waitKey(0)  # display the image until you close the window

cv2.destroyAllWindows()  # terminate all windows