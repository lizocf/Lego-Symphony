from scamp import *
import random

import cv2
import numpy as np
import imutils
from PIL import Image

from scamp import *
import random

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

# make dots for approximate location of grid
for j in x_grid_pts:
    for k in y_grid_pts:
        cv2.circle(image, (int(j), int(k)), 1, (0, 0, 255), 3) 

cv2.imshow('image',image)
cv2.waitKey(0)

# height, width = 500, 500
# image = cv2.resize(image,(height,width), interpolation=cv2.INTER_AREA)

x_grid_pts = sorted(x_grid_pts)
y_grid_pts = sorted(y_grid_pts)

# example to focus on the bottom right corner
roi = image[int(x_grid_pts[3]):int(x_grid_pts[4]),
            int(y_grid_pts[3]):int(y_grid_pts[4])]

cv2.imshow('roi', roi)
cv2.waitKey(0)

## for each roi, see BGR values

# color detection
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
red_mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
red_mask = cv2.bitwise_or(red_mask1, red_mask2)
red_pos = np.argwhere(red_mask==0)

yellow_mask = cv2.inRange(img_hsv, (20, 100, 100), (40, 255, 255))
yellow_pos = np.argwhere(yellow_mask==0)

blue_mask = cv2.inRange(img_hsv, (75, 66, 139), (167, 255, 255))
blue_pos = np.argwhere(blue_mask==0)

# example
blue_cropped = cv2.bitwise_and(image, image, mask=blue_mask)
cv2.imshow('blue areas', blue_cropped)
cv2.waitKey(0)


x_grid_pts = np.ceil(x_grid_pts).astype(int)
y_grid_pts = np.ceil(y_grid_pts).astype(int)

count = 0

for j in range(len(x_grid_pts)-1):
    for k in range(len(y_grid_pts)-1):
        bools = np.logical_and((blue_pos < [x_grid_pts[j+1], y_grid_pts[j+1]]), (blue_pos >= [x_grid_pts[j], y_grid_pts[j]]))

        x_bools = [bool[0] for bool in bools]
        y_bools = [bool[1] for bool in bools]
        
        for bool in [a and b for a, b in zip(x_bools, y_bools)]:
            if bool:
                print('yas')
                count +=1
            

        # breakpoint()
        # if bools

    
        breakpoint()
        # if np.logical_and(all(x_grid_pts[j] < (list(zip(*blue_pos))[0]) < x_grid_pts[j+1]), (y_grid_pts[k] < (list(zip(*blue_pos))[1]) < y_grid_pts[k])):
        #     breakpoint()
        breakpoint()

breakpoint()

''' TO_DO:
1. majority BGR values -> volume
2. scamp per color
3. loop
'''
