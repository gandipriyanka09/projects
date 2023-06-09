import numpy as np
import cv2

img = np.ones((800,800,3))
#First column
img[0:100,100:200] = 0,0,0
img[0:100,300:400]= 0,0,0
img[0:100,500:600] = 0,0,0
img[0:100,700:800]=0,0,0
#Second column
img[100:200,0:100] = 0,0,0
img[100:200,400:500] = 0,0,0
img[100:200,600:700] = 0,0,0
img[100:200,200:300] = 0,0,0
#Third column
img[200:300,100:200]=0,0,0
img[200:300,300:400]=0,0,0
img[200:300,500:600]=0,0,0
img[200:300,700:800]=0,0,0
#Fourth column
img[300:400,0:100]=0,0,0
img[300:400,400:500]=0,0,0
img[300:400,600:700]=0,0,0
img[300:400,200:300]=0,0,0
#Fifth column
img[400:500,100:200]=0,0,0
img[400:500,300:400]=0,0,0
img[400:500,500:600]=0,0,0
img[400:500,700:800]=0,0,0
#Sixth column
img[500:600,0:100]=0,0,0
img[500:600,200:300]=0,0,0
img[500:600,400:500]=0,0,0
img[500:600,600:700]=0,0,0
#Seveth column
img[600:700,100:200]=0,0,0
img[600:700,300:400]=0,0,0
img[600:700,500:600]=0,0,0
img[600:700,700:800]=0,0,0
#Eighth column
img[700:800,0:100]=0,0,0
img[700:800,200:300]=0,0,0
img[700:800,400:500]=0,0,0
img[700:800,600:700]=0,0,0

#Scaling:
img1 = cv2.resize(img,None,fx = 0.75,fy = 0.75)
cv2.imshow('8x8 checker board',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
