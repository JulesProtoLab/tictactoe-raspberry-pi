#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

X = (255, 0, 0)
O = (0, 255, 0)
L = (0, 0, 255)
B = (0, 0, 0)

BORD_START = [
    X, B, L, B, B, L, B, B,
    B, B, L, B, B, L, B, B,
    L, L, L, L, L, L, L, L,
    B, B, L, B, B, L, B, B,
    B, B, L, B, B, L, B, B,
    L, L, L, L, L, L, L, L,
    B, B, L, B, B, L, B, B,
    B, B, L, B, B, L, B, O,
]

MIN_SIZE_PLAYER = 0
MAX_SIZE_PLAYER = 2
MIN_POS_MATRIX = 0
MAX_POS_MATRIX = 6
STEPS_MOVE = 3

X_POS_START = 3
Y_POS_START = 3

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

def pushed_middle(event):
    global x, y
    if event.action != ACTION_RELEASED:
        x = X_POS_START
        y = Y_POS_START

def refresh():
    sense.clear()
    sense.set_pixels(BORD_START)

    for width in range(MIN_SIZE_PLAYER, MAX_SIZE_PLAYER):
        for height in range(MIN_SIZE_PLAYER, MAX_SIZE_PLAYER):
            sense.set_pixel(x + width, y + height, O)

def main(args):
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_middle = pushed_middle
    sense.stick.direction_any = refresh

    sense.low_light = True
    
    refresh()
    pause()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
