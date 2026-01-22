#!/usr/bin/env python

from enum import Enum
from sense_hat import SenseHat

# Used LED colors
R = (255, 0, 0) # Red
G = (0, 255, 0)	# Green
Y = (255, 255, 0) #Yellow
B = (0, 0, 255) # Blue
C = (0, 255, 255) # Cyan
W = (128, 128, 128) #White
X = (0, 0, 0) # None (LED off)

MATRIX_SMILEY = [
X, X, X, X, X, X, X, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, C, X, X, C, Y, X,
X, X, X, X, X, X, X, X,
Y, X, X, X, X, X, X, Y,
X, Y, X, X, X, X, Y, X,
X, X, Y, Y, Y, Y, X, X,
X, X, X, X, X, X, X, X,
]

MATRIX_FROWN = [
X, X, X, X, X, X, X, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, C, X, X, C, Y, X,
X, X, X, X, X, X, X, X,
X, X, Y, Y, Y, Y, X, X,
X, Y, X, X, X, X, Y, X,
Y, X, X, X, X, X, X, Y,
X, X, X, X, X, X, X, X,
]

MATRIX_TONGUE= [
X, X, X, X, X, X, X, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, C, X, X, C, Y, X,
X, X, X, X, X, X, X, X,
Y, Y, Y, Y, Y, Y, Y, Y,
X, X, X, R, R, R, R, X,
X, X, X, X, R, R, X, X,
X, X, X, X, X, X, X, X,
]

class Emoji:
    def __init__(self):
        self._sense = SenseHat()
        self._sense.low_light = True

    def draw(self, shape):
        self._sense.set_pixels(shape)
        

def main(args):
    emoji = Emoji()
    emoji.draw(MATRIX_TONGUE)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
