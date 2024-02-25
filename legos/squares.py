from scamp import *
import random

import cv2
import numpy as np
import imutils
from PIL import Image

 # added green dots at corner of lego board
imgpath = "./legos/legos_green_corner.jpg"     
img = Image.open(imgpath).convert('RGB')


na = np.array(img)
img_copy = na

'''
CROPPING
'''
# find green dots
borderY, borderX = np.where(np.all(na==[125,198,0],axis=2))     

top, bottom = np.min(borderY), np.max(borderY)
left, right = np.min(borderX), np.max(borderX)

# crop image from where green dots are
ROI = img_copy[top:bottom, left:right]      

# convert to opencv img
image = cv2.cvtColor(np.array(Image.fromarray(ROI)), cv2.COLOR_RGB2BGR)     

borderY, borderX = np.where(np.all(image==[0,198,125],axis=2))     

top, bottom = np.min(borderY), np.max(borderY)
left, right = np.min(borderX), np.max(borderX)

x_grid_pts = np.linspace(left,right,5)
y_grid_pts = np.linspace(top,bottom,5)

# breakpoint()

for j in x_grid_pts:
    for k in y_grid_pts:
        cv2.circle(image, (int(j), int(k)), 1, (0, 0, 255), 3) 

cv2.imshow('image',image)
cv2.waitKey(0)

# breakpoint()

# height, width = 500, 500
# image = cv2.resize(image,(height,width), interpolation=cv2.INTER_AREA)

x_grid_pts = sorted(x_grid_pts)
y_grid_pts = sorted(y_grid_pts)

# cv2.rectangle(imgResize,(300,250),(320,270),(255,0,0),2)
# breakpoint()

roi = image[int(x_grid_pts[3]):int(x_grid_pts[4]), ## continue this for all squares
            int(y_grid_pts[3]):int(y_grid_pts[4])]

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
red_mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
red_mask = cv2.bitwise_or(red_mask1, red_mask2)

yellow_mask = cv2.inRange(img_hsv, (20, 100, 100), (40, 255, 255))
yellow_pos = np.argwhere(yellow_mask==0)

blue_mask = cv2.inRange(img_hsv, (75, 66, 139), (167, 255, 255))
blue_pos = np.argwhere(blue_mask==0)

blue_cropped = cv2.bitwise_and(image, image, mask=blue_mask)

cv2.imshow('roi', roi)
cv2.waitKey(0)

cv2.imshow('roi', blue_cropped)
cv2.waitKey(0)

## for each roi, see BGR values

## majority BGR values -> volume

## scamp per color

## loop

