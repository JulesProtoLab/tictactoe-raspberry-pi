#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

X = (255, 0, 0)
O = (0, 255, 0)
L = (64, 64, 64)
B = (0, 0, 0)
D = (127, 127, 127)

BORD_START = [              #List_Positions
    B, B, L, B, B, L, B, B, #0 - 7
    B, B, L, B, B, L, B, B, #8 - 15
    L, L, L, L, L, L, L, L, #16 - 23
    B, B, L, B, B, L, B, B, #24 - 31
    B, B, L, B, B, L, B, B, #32 - 39
    L, L, L, L, L, L, L, L, #40 - 47
    B, B, L, B, B, L, B, B, #48 - 55
    B, B, L, B, B, L, B, B, #56 - 63
]

MIN_SIZE_PLAYER = 1
MAX_SIZE_PLAYER = 2
DIFF_SIZE_PLAYER = MAX_SIZE_PLAYER - MIN_SIZE_PLAYER

MIN_POS_MATRIX = 0
MAX_POS_MATRIX = 6
STEPS_MOVE = 3
LEDS_PER_ROW = 8

X_POS_START = 3
Y_POS_START = 3

is_player_x = True
bord_current = BORD_START
x = X_POS_START
y = Y_POS_START

sense = SenseHat()

def clamp(value, min_value=MIN_POS_MATRIX, max_value=MAX_POS_MATRIX):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - STEPS_MOVE)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + STEPS_MOVE)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - STEPS_MOVE)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + STEPS_MOVE)
        
def get_color_current_player():
    return X if is_player_x else O

def pushed_middle(event):
    global x, y, bord_current, is_player_x
    if event.action != ACTION_RELEASED:
       
        #Saving the current players move on the bord
        list_pos_topleft = x + DIFF_SIZE_PLAYER + y * LEDS_PER_ROW
        list_pos_bottemright= x + (y + DIFF_SIZE_PLAYER) * LEDS_PER_ROW
        
        bord_current[list_pos_topleft] = get_color_current_player()
        bord_current[list_pos_bottemright] = get_color_current_player()

        is_player_x = False if is_player_x else True
        x = X_POS_START
        y = Y_POS_START

def refresh():
    sense.clear()
    sense.set_pixels(bord_current)
    
    sense.set_pixel(x, y, get_color_current_player())
    sense.set_pixel(x + DIFF_SIZE_PLAYER, y + DIFF_SIZE_PLAYER, get_color_current_player())

def main(args):
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_middle = pushed_middle
    sense.stick.direction_any = refresh

    sense.low_light = False
    
    refresh()
    pause()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
