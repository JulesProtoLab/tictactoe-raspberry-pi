#!/usr/bin/env python

from sense_hat import SenseHat

from player import Player

# Used LED colors
X = (255, 0, 0) # Player X
O = (0, 255, 0)	# Player O
L = (64, 64, 64) # Outline board
B = (0, 0, 0) # None (LED off)

MATRIX_START = [      #List_Positions
    B, B, L, B, B, L, B, B, #0 - 7
    B, B, L, B, B, L, B, B, #8 - 15
    L, L, L, L, L, L, L, L, #16 - 23
    B, B, L, B, B, L, B, B, #24 - 31
    B, B, L, B, B, L, B, B, #32 - 39
    L, L, L, L, L, L, L, L, #40 - 47
    B, B, L, B, B, L, B, B, #48 - 55
    B, B, L, B, B, L, B, B, #56 - 63
]

TOTAL_GAMEBOARD_POS = 9
GAMEBOARD_START = [Player.UNDEFINED] * TOTAL_GAMEBOARD_POS
LENGTH_GAMEBOARD = int(TOTAL_GAMEBOARD_POS ** 0.5)

MIN_SIZE_PLAYER = 1
MAX_SIZE_PLAYER = 2
DIFF_SIZE_PLAYER = MAX_SIZE_PLAYER - MIN_SIZE_PLAYER
OFFSET_GAME_TO_MATRIX = 3
LEDS_PER_ROW = 8

IS_PLAYER_X = True

class Board:

    def __init__(self):
	self._matrix = MATRIX_START
	self._gameboard = GAMEBOARD_START
	self._is_player_x = IS_PLAYER_X
	self._color_player = self.determine_color_player()
	
	self.sense = SenseHat()
	
    def switch_player(self):
	self._is_player_x = not self._is_player_x 
	self._color_player = self.determine_color_player()
	
    def determine_color_player(self):
	return X if self._is_player_x else O

    def get_current_player(self):
	return Player.X if self._is_player_x else Player.O
    
    #Moving the player is only a visual effect on the matrix
    def move_player(self, x_game, y_game):
	x_matrix = x_game * OFFSET_GAME_TO_MATRIX
	y_matrix = y_game * OFFSET_GAME_TO_MATRIX
    
	self.sense.set_pixel(x_matrix, y_matrix, self._color_player)
	self.sense.set_pixel(x_matrix + DIFF_SIZE_PLAYER, y_matrix + DIFF_SIZE_PLAYER, self._color_player)
    
    def claim_spot_player(self, x_game, y_game):
	self._gameboard[x_game + y_game * LENGTH_GAMEBOARD] = self.get_current_player()
	
	x_matrix = x_game * OFFSET_GAME_TO_MATRIX
	y_matrix = y_game * OFFSET_GAME_TO_MATRIX
	
	list_pos_topleft = x_matrix + DIFF_SIZE_PLAYER + y_matrix * LEDS_PER_ROW
	self._matrix [list_pos_topleft] = self._color_player
	
	list_pos_bottemright= x_matrix + (y_matrix + DIFF_SIZE_PLAYER) * LEDS_PER_ROW
	self._matrix [list_pos_bottemright] = self._color_player
    
    def draw(self):
	self.sense.clear()
	self.sense.set_pixels(self._matrix)
		
		
		
	
