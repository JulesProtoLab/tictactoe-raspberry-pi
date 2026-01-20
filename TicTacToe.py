#!/usr/bin/env python

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

from board import Board
from player import Player

MIN_COORD_GAME = 0
MAX_COORD_GAME = 2
STEPS_MOVE_PLAYER = 1

board = Board()
player = Player()

def clamp(value, min_value=MIN_COORD_GAME, max_value=MAX_COORD_GAME):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        y = clamp(player.get_y() - STEPS_MOVE_PLAYER)
        player.set_y(y)
            
def pushed_down(event):
    if event.action != ACTION_RELEASED:
        y = clamp(player.get_y() + STEPS_MOVE_PLAYER)
        player.set_y(y)

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        x = clamp(player.get_x() - STEPS_MOVE_PLAYER)
        player.set_x(x)

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        x = clamp(player.get_x() + STEPS_MOVE_PLAYER)
        player.set_x(x)

def pushed_middle(event):
    if event.action != ACTION_RELEASED:
        is_succesfully_claimed = board.claim_spot(player)

        if is_succesfully_claimed:
            player.next()
        else:
            print("Nee =P")

def refresh():
    board.draw()
    board.move(player)

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
