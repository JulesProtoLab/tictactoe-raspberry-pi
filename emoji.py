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

# Both the eyes and the mouth are drawn on 4 rows of the LED-matrix
# Combine the eyes and the mouth to draw a emoticon which fills the LED-matrix
class _Eyes(Enum):
    FORWARD = [
        X, X, X, X, X, X, X, X,
        X, X, Y, X, X, Y, X, X,
        X, X, Y, X, X, Y, X, X,
        X, X, X, X, X, X, X, X
        ]

class _Mouth(Enum):
    NEUTRAL = [
        X, X, X, X, X, X, X, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, X, X, X, X, X, X, X,
        X, X, X, X, X, X, X, X
        ]
    SMILE = [
        Y, X, X, X, X, X, X, Y,
        X, Y, X, X, X, X, Y, X,
        X, X, Y, Y, Y, Y, X, X,
        X, X, X, X, X, X, X, X
    ]
    FROWN = [
        X, X, Y, Y, Y, Y, X, X,
        X, Y, X, X, X, X, Y, X,
        Y, X, X, X, X, X, X, Y,
        X, X, X, X, X, X, X, X
    ]
    TONGUE = [
        X, Y, Y, Y, Y, Y, Y, Y,
        X, X, X, X, Y, X, X, Y,
        X, X, X, X, X, Y, Y, X,
        X, X, X, X, X, X, X, X
    ]

# Reference for emoticons: 'https://en.wikipedia.org/wiki/List_of_emoticons'
class Emoticon(Enum):
    NEUTRAL = _Eyes.FORWARD.value + _Mouth.NEUTRAL.value # =|
    SMILING = _Eyes.FORWARD.value + _Mouth.SMILE.value # =)
    FROWNING = _Eyes.FORWARD.value + _Mouth.FROWN.value # =(
    JOKING = _Eyes.FORWARD.value + _Mouth.TONGUE.value # =P

#class EmojiAnimator:
    #def __init__(self):
        #self._sense = SenseHat()
        #self._sense.low_light = True

    #def draw(self, name):
        #self._sense.set_pixels()
        
def main(args):
    sense = SenseHat()
    sense.low_light = True
    
    sense.set_pixels(Emoticon.JOKING.value)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
