import cv2

img=cv2.imread('logo2.png')
img2=cv2.resize(img,(200,200),interpolation=cv2.INTER_LINEAR)
cv2.imwrite('logo.png', img2)

#img2=cv2.resize(img,(200,200),interpolation=cv2.INTER_LINEAR)

 