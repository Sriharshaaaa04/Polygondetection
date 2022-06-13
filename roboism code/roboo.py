import cv2
import numpy as np 
from contors import coun   
from rotationfun import rotate        
org=cv2.imread("IMG_20220604_134409.jpg")
org=cv2.resize(org,(620,438))
coun(org)
cv2.imshow("img",org)
cv2.waitKey(0)

#first image
im1=cv2.imread("LMAO1.jpg")

rotated1=rotate(im1,-15.9642184)
coun(rotated1)
rotateed1=rotated1[97:519,91:513]
resize1=cv2.resize(rotateed1,(146,146))
img1=cv2.imread("blk.webp")
img1=cv2.resize(img1,(800,800))
img1[150:588,100:720]=org
img1=rotate(img1,13.4652081)
coun(img1)
img1[220:366,122:268]=resize1
img1=rotate(img1,-13.4652081)

#for the second image
img2=cv2.imread("XD2.jpg")
resize2=cv2.resize(img2,(600,600))
rotated2=rotate(resize2,12.8477049)
coun(rotated2) 
coun(img1)
crop2=rotated2[63:540,64:541]
resize2=cv2.resize(crop2,(126,126))
img1[176:302,512:638]=resize2

#for the third image
img3=cv2.imread("Ha3.jpg")
resize3=cv2.resize(img3,(600,600))
coun(resize3)
crop3=resize3[76:526,78:525]
crop3=cv2.resize(crop3,(108,108))
img1=rotate(img1,22.7028421)
coun(img1)
img1[245:353,547:655]=crop3
img1=rotate(img1,-22.7028421)

#for the fourth image
img4=cv2.imread("HaHa4.jpg")
img4=rotate(img4,-14.9567059)
crop4=img4[76:517,75:515]
coun(crop4)
resize4=cv2.resize(crop4,(189,189))
img1=rotate(img1,-28.4651622)
coun(img1) 
img1[300:489,244:433]=resize4
img1=rotate(img1,+28.4651622)


img1=img1[150:588,100:720]
cv2.imshow("FInal",img1)
cv2.waitKey(0)