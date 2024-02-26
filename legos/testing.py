import cv2
from scamp import *
import numpy as np

# just testing
s = Session()
piano = s.new_part("piano")

piano.play_note(70, 0.8, 2)

def play_lego_music(color_map):
    # Create a SCAMP session
    s = Session()
    print("New session created")

    # Create ensembles for each instrument
    piano = s.new_part("piano")
    guitar = s.new_part("guitar")
    drums = s.new_part("drums")
    print("new instruments created")
    
    # Iterate through the color map
    for position, color in color_map.items():
        row, _ = position  # Column value is not used for determining the note or drum

        # for drums
        # 42 = closed hi hat
        # 45 = low tom
        # 41 = floor tom
        # 36 = bass drum

        # chords
        # C4 = 60
        # G3 = 55
        # E3 = 52
        # C2 = 36
        
        # Determine the note or drum based on the row
        if row < 4:
            note, octave = 60, 4
            drum_sound = 42
        elif row < 8:
            note, octave = 55, 3
            drum_sound = 45
        elif row < 12:
            note, octave = 52, 3
            drum_sound = 41
        else:
            note, octave = 36, 2
            drum_sound = 36
        
        # play the instrument untz untz
        if color == "yellow":  # Guitar
            guitar.play_note(note, 0.8, 1)  # duration set to 1 as an example
            print("played guitar at note:", note)
        elif color == "blue":  # Piano
            piano.play_note(note, 0.8, 1)  # duration set to 1 as an example
            print("played piano at note: ", note)

        elif color == "red":  # Drums
            drums.play_note(drum_sound, 0.8, 1)  # duration set to 1 as an example
            print("played drum at note: ", note)




# color_map = {}
# colors = ['yellow', 'blue', 'red']  # repeating pattern of colors

# # generate sample color map
# for row in range(16):  # for each row in a 16x16 grid
#     for col in range(16):  # for each column in the row
#         color_index = (row + col) % len(colors)  # calculate which color to use
#         color_map[(row, col)] = colors[color_index]  # assign the color to the current position





play_lego_music(color_map)
