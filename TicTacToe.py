#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

from board import Board, BOARD_VISUAL_START

MIN_POS_MATRIX = 0
MAX_POS_MATRIX = 6
STEPS_MOVE = 3

X_POS_START = 3
Y_POS_START = 3

x = X_POS_START
y = Y_POS_START
is_player_x = True

board = Board()

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
    
        board.save_move_player(is_player_x, x, y)
        
        is_player_x = False if is_player_x else True
        x = X_POS_START
        y = Y_POS_START

def refresh():
    board.draw()
    board.move_player(is_player_x, x, y)

def main(args):
    sense = SenseHat()
    
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
