#!/usr/bin/env python

import cv2
import numpy as np
import os
import math

#Lecture image en couleur
img=cv2.imread('./dc19843.jpg')
print('---Couleur---')
print(img.shape)
rows,cols,colors = img.shape

alpha = 0.5
beta = 1

result = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

cv2.imwrite('bc_image.jpg', result)
"""chemin_img_crop='./image_treated.jpg'
#Parcours de l'image par tres grandes parties
for i in range(0,math.floor(rows/2)+1,math.floor(rows/2)):
	for j in range(0,math.floor(cols/2)+1,math.floor(cols/2)):
		img_crop_1=img[i:i+math.floor(rows/2),j:j+math.floor(cols/2)]
		chemin_img_crop_1='p1'+'_'+str(i)+'_'+str(j)+'.jpg'	
		cv2.imwrite(chemin_img_crop_1,cv2.resize(img_crop_1,(299,299)))
		
for i in range(0,(2*math.floor(rows/3))+1,math.floor(rows/3)):
	for j in range(0,(2*math.floor(cols/3))+1,math.floor(cols/3)):
		img_crop_2=img[i:i+math.floor(rows/3),j:j+math.floor(cols/3)]
		chemin_img_crop_2='p2'+'_'+str(i)+'_'+str(j)+'.jpg'	
		cv2.imwrite(chemin_img_crop_2,cv2.resize(img_crop_2,(299,299)))"""