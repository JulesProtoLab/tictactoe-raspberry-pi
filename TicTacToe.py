#!/usr/bin/env python

from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

from board import Board, BOARD_VISUAL_START

MIN_POS = 0
MAX_POS = 2
STEPS_MOVE = 1

X_POS_START = 1
Y_POS_START = 1

#Location player on gameboard
x = X_POS_START
y = Y_POS_START

board = Board()

def clamp(value, min_value=MIN_POS, max_value=MAX_POS):
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
    
        board.save_move_player(x, y)
        board.switch_player()

        x = X_POS_START
        y = Y_POS_START

def refresh():
    board.draw()
    board.move_player(x, y)

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
