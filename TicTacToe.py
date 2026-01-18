from time import sleep
from sense_hat import SenseHat

X = (255, 0, 0)
O = (0, 255, 0)
L = (0, 0, 255)
B = (0, 0, 0)

BORD_START = [
    X, B, L, B, B, L, B, B,
    B, B, L, B, B, L, B, B,
    L, L, L, L, L, L, L, L,
    B, B, L, B, X, L, B, B,
    B, B, L, X, B, L, B, B,
    L, L, L, L, L, L, L, L,
    B, B, L, B, B, L, B, B,
    B, B, L, B, B, L, B, O,
]
        
def main(args):
    sense = SenseHat()
    
    sense.low_light = True
    sense.set_pixels(BORD_START)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
