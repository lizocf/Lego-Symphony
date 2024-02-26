from scamp import *
import random

import cv2
import numpy as np
import imutils
from PIL import Image

from scamp import *
import random

# from music import build_chord

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

x_grid_pts = np.ceil(x_grid_pts).astype(int)
y_grid_pts = np.ceil(y_grid_pts).astype(int)

# example to focus on the bottom right corner
roi = image[(x_grid_pts[3]):(x_grid_pts[4]),
            (y_grid_pts[3]):(y_grid_pts[4])]

cv2.imshow('roi', roi)
cv2.waitKey(0)

## for each roi, see BGR values

# color detection

def color_detection(img, position=False):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    red_mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
    red_mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    
    yellow_mask = cv2.inRange(img_hsv, (20, 100, 100), (40, 255, 255))
    
    blue_mask = cv2.inRange(img_hsv, (75, 66, 139), (167, 255, 255))
    
    if position:
        red_pos = np.argwhere(red_mask!=0)
        yellow_pos = np.argwhere(yellow_mask!=0)
        blue_pos = np.argwhere(blue_mask!=0)
        return red_pos, yellow_pos, blue_pos 

    else: return red_mask, yellow_mask, blue_mask

red_mask, yellow_mask, blue_mask = color_detection(image)

blue_cropped = cv2.bitwise_and(image, image, mask=blue_mask)
cv2.imshow('blue areas', blue_cropped)
cv2.waitKey(0)

  
rows, cols, m = (4, 4, 3)
rois = [[0 for i in range(cols)] for j in range(rows)] # rois[x,y,z], where x,y are squares from top-left
masks = [[[0 for z in range(m)]for i in range(cols)] for j in range(rows)] # masks[x,y,z] where z is R,Y,B


for x in range(4):
    for y in range(4):
        rois[x][y] = (image[(x_grid_pts[x]):(x_grid_pts[x+1]),
                           (y_grid_pts[y]):(y_grid_pts[y+1])])
        masks[x][y][:] = color_detection(rois[x][y])
        
        ## INSERT YURI'S CODE HERE ##
        if (mask[x][y][0] != 0).sum() > 1000:  # check if there is red
            # make chord
        if (mask[x][y][1] != 0).sum() > 1000:  # check if there is yellow
            # make chord
        if (mask[x][y][2] != 0).sum() > 1000:  # check if there is blue
            # make chord




# count = 0

breakpoint()

# for j in range(len(x_grid_pts)-1):
#     for k in range(len(y_grid_pts)-1):
#         bools = np.logical_and((blue_pos < [x_grid_pts[j+1], y_grid_pts[j+1]]), (blue_pos >= [x_grid_pts[j], y_grid_pts[j]]))

#         x_bools = [bool[0] for bool in bools]
#         y_bools = [bool[1] for bool in bools]
        
    
#     if [a and b for a, b in zip(x_bools, y_bools)]:
#         if bool:
#             print('yas')
#             count +=1
            

        # breakpoint()
        # if bools

    
        # breakpoint()
        # # if np.logical_and(all(x_grid_pts[j] < (list(zip(*blue_pos))[0]) < x_grid_pts[j+1]), (y_grid_pts[k] < (list(zip(*blue_pos))[1]) < y_grid_pts[k])):
        # #     breakpoint()
        # breakpoint()


# def build_chord(interval_options, num_notes, pitch_center, round_transposition=False):
#     chord = [0]
#     while len(chord) < num_notes:
#         chord.append(chord[-1] + interval_options[0])
#         chord.append(chord[-1] + interval_options[1])
#         chord.append(chord[-1] + interval_options[2])

#     transposition = pitch_center - sum(chord) / len(chord)
#     return [p + transposition for p in chord]


# s = Session()

# guitar = s.new_part("guitar")
# recorder = s.new_part("recorder")
# piano = s.new_part("piano")



''' TO_DO:
1. Make each roi of squares
1. majority BGR values -> volume
2. scamp per color
3. loop
'''
