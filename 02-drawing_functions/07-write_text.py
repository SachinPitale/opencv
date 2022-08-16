import cv2

image=cv2.imread(filename='ms.jpg', flags=1)

text="MS Dhoni"
origin=(100,100)
font=cv2.QT_FONT_NORMAL
font_scale=1
color=(0,255,0)
thinkness=5
line_type=cv2.LINE_AA

cv2.putText(img=image,org=origin,text=text,fontScale=font_scale,fontFace=font,color=color,thickness=thinkness,lineType=line_type)
cv2.imshow('my window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()