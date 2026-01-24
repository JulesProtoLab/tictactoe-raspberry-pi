#!/usr/bin/env python

from time import sleep
from signal import pause

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

from board import Board
from player import Player
from emoticon import MATRIX_X, MATRIX_V

MIN_COORD_GAME = 0
MAX_COORD_GAME = 2
STEPS_MOVE_PLAYER = 1

sense = SenseHat()
sense.low_light = False

board = Board()
player = Player()

SEC_TO_WAIT_PRE = 2
SEC_TO_WAIT_POST = 10
is_showcasing_bug = False
if is_showcasing_bug:
    SEC_TO_WAIT_PRE = 1
    player.next()
else:
    SEC_TO_WAIT_PRE = 2

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

        if not is_showcasing_bug:
            if is_succesfully_claimed:
                player.next()
            else:
                print("Spot already claimed!")

                sleep(SEC_TO_WAIT_PRE)
                sense.set_pixels(MATRIX_V)
                sleep(SEC_TO_WAIT_POST)
        else:
            print("A bug...")
            board.draw()
            sleep(SEC_TO_WAIT_PRE)
            sense.set_pixels(MATRIX_X)
            sleep(SEC_TO_WAIT_POST)
            player.next()
            
def refresh():
    board.draw()
    board.move(player)

def main(args):
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_middle = pushed_middle
    sense.stick.direction_any = refresh

    refresh()
    pause()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
