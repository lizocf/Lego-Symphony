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

'''
DETECTING CIRCLES
'''

# convert to opencv img
image = cv2.cvtColor(np.array(Image.fromarray(ROI)), cv2.COLOR_RGB2BGR)     

height, width = 500, 500
image = cv2.resize(image,(height,width), interpolation=cv2.INTER_AREA)

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 35, 
               param2 = 17.5, minRadius = 1, maxRadius = 20) 
  
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
    circle_positions = []

    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 

        circle_positions.append((a,b))      # append circle coords
  
        # Draw the circumference of the circle. 
        cv2.circle(image, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3) 
        

        # print(a,b)

'''
SORTING CIRCLE COORDS FROM TOP LEFT -> BOTTOM RIGHT
'''
# breakpoint()
# print(sort_index(circle_positions))

cv2.rectangle(imgResize,(300,250),(320,270),(255,0,0),2)
roi = imgResize[255:267, 305: 317]

cv2.imshow('image', image)
cv2.waitKey(0)