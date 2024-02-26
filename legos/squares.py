from scamp import *
import random

import cv2
import numpy as np
import imutils
from PIL import Image

from scamp import *
import random

# from music import build_chord

# breakpoint()

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


notes = [60,55,52,36]
octaves = [4,3,3,2]
drum_sounds = [42,45,41,36]

red = [[0 for i in range(cols)] for j in range(rows)]
yellow = [[0 for i in range(cols)] for j in range(rows)]
blue = [[0 for i in range(cols)] for j in range(rows)]

s = Session()
print("New session created")

piano = s.new_part("piano")
guitar = s.new_part("guitar")
drums = s.new_part("drums")
print("new instruments created")
    



for x in range(4):
    for y in range(4):
        rois[x][y] = (image[(x_grid_pts[x]):(x_grid_pts[x+1]),
                           (y_grid_pts[y]):(y_grid_pts[y+1])])
        masks[x][y][:] = color_detection(rois[x][y])
        
        if y == 0:
            note, octave = 60, 4
            drum_sound = 42
        elif y == 1:
            note, octave = 55, 3
            drum_sound = 45
        elif y == 2:
            note, octave = 52, 3
            drum_sound = 41
        else:
            note, octave = 36, 2
            drum_sound = 36
    
        
        if (masks[x][y][0] != 0).sum() > 1000:  # check if there is red
            exec(f"def red_{x}{y}(): drums.play_note({drum_sound}, 0.8, 1)")
        else: exec(f"def red_{x}{y}(): wait({1})")
            # Drums(drum_sound)  # duration set to 1 as an example
            # print("played drum at note: ", note)

        if (masks[x][y][1] != 0).sum() > 1000:  # check if there is yellow
            exec(f"def yellow_{x}{y}(): guitar.play_note({note}, 0.8, 1)")
        else: exec(f"def yellow_{x}{y}(): wait({1})")
            # print("played guitar at note:", note)

        if (masks[x][y][2] != 0).sum() > 1000:  # check if there is blue
            exec(f'def blue_{x}{y}(): piano.play_note({note}, 0.8, 1)')
        else: exec(f"def blue_{x}{y}(): wait({1})")
            # Piano(note)  # duration set to 1 as an example
            # print("played piano at note: ", note)



while True:
    s.fork(red_00)
    s.fork(yellow_00)
    s.fork(blue_00)
    s.fork(red_01)
    s.fork(yellow_01)
    s.fork(blue_01)
    s.fork(red_02)
    s.fork(yellow_02)
    s.fork(blue_02)
    s.fork(red_03)
    s.fork(yellow_03)
    s.fork(blue_03)
    s.wait_for_children_to_finish()
    s.fork(red_10)
    s.fork(yellow_10)
    s.fork(blue_10)
    s.fork(red_11)
    s.fork(yellow_11)
    s.fork(blue_11)
    s.fork(red_12)
    s.fork(yellow_12)
    s.fork(blue_12)
    s.fork(red_13)
    s.fork(yellow_13)
    s.fork(blue_13)
    s.wait_for_children_to_finish()
    s.fork(red_20)
    s.fork(yellow_20)
    s.fork(blue_20)
    s.fork(red_21)
    s.fork(yellow_21)
    s.fork(blue_21)
    s.fork(red_22)
    s.fork(yellow_22)
    s.fork(blue_22)
    s.fork(red_23)
    s.fork(yellow_23)
    s.fork(blue_23)
    s.wait_for_children_to_finish()
    s.fork(red_30)
    s.fork(yellow_30)
    s.fork(blue_30)
    s.fork(red_31)
    s.fork(yellow_31)
    s.fork(blue_31)
    s.fork(red_32)
    s.fork(yellow_32)
    s.fork(blue_32)
    s.fork(red_33)
    s.fork(yellow_33)
    s.fork(blue_33)
    s.wait_for_children_to_finish()

    breakpoint()
