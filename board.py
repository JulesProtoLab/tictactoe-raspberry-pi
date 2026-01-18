#!/usr/bin/env python

from sense_hat import SenseHat

# Used LED colors
X = (255, 0, 0) # Player X
O = (0, 255, 0)	# Player O
L = (64, 64, 64) # Outline board
B = (0, 0, 0) # None (LED off)

BOARD_VISUAL_START = [      #List_Positions
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

LEDS_PER_ROW = 8

IS_PLAYER_X = True

class Board:

    def __init__(self):
	self._board_visual = BOARD_VISUAL_START
	self._is_player_x = IS_PLAYER_X
	
	self.sense = SenseHat()
	
    def switch_player(self):
	self._is_player_x = not self._is_player_x 
	
    def get_color_player(self):
	return X if self._is_player_x else O
    
    def move_player(self, x, y):
	color_player = self.get_color_player()
	
	self.sense.set_pixel(x, y, color_player)
	self.sense.set_pixel(x + DIFF_SIZE_PLAYER, y + DIFF_SIZE_PLAYER, color_player)
    
    def save_move_player(self, x, y):
	color_player = self.get_color_player()
	
	list_pos_topleft = x + DIFF_SIZE_PLAYER + y * LEDS_PER_ROW
	self._board_visual [list_pos_topleft] = color_player
	
	list_pos_bottemright= x + (y + DIFF_SIZE_PLAYER) * LEDS_PER_ROW
	self._board_visual [list_pos_bottemright] = color_player
    
    def draw(self):
	self.sense.clear()
	self.sense.set_pixels(self._board_visual)
		
		
	
