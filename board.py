#!/usr/bin/env python

from sense_hat import SenseHat

from player import PlayerName, Player

# Used LED colors
X = (255, 0, 0) # Player X
O = (0, 255, 0)	# Player O
L = (64, 64, 64) # Outline board
B = (0, 0, 0) # None (LED off)

LEDS_PER_ROW = 8
MATRIX_COLORS_START = [      #List_Positions
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
OFFSET_GAME_TO_MATRIX = 3

TOTAL_GAMEBOARD_POS = 9
GAMEBOARD_CLAIMS_START = [PlayerName.UNDEFINED] * TOTAL_GAMEBOARD_POS
LENGTH_GAMEBOARD = int(TOTAL_GAMEBOARD_POS ** 0.5)

sense = SenseHat()

class Board:
    def __init__(self):
	self._matrix_colors = MATRIX_COLORS_START
	self._gameboard_claims = GAMEBOARD_CLAIMS_START
	
    def determine_color_player(self, playername):
	return X if playername == PlayerName.X else O

    #Moving the player is only a visual effect on the matrix
    def move(self, player):
	x_game, y_game = player.get_coordinates()

	x_matrix = x_game * OFFSET_GAME_TO_MATRIX
	y_matrix = y_game * OFFSET_GAME_TO_MATRIX
	color = self.determine_color_player(player.get_name())
	
	sense.set_pixel(x_matrix, y_matrix, color)
	sense.set_pixel(x_matrix + DIFF_SIZE_PLAYER, y_matrix + DIFF_SIZE_PLAYER, color)
    
    def claim_spot(self, player):
	x_game, y_game = player.get_coordinates()
	name = player.get_name()

	self._gameboard_claims[x_game + y_game * LENGTH_GAMEBOARD] = name
	
	x_matrix = x_game * OFFSET_GAME_TO_MATRIX
	y_matrix = y_game * OFFSET_GAME_TO_MATRIX
	color = self.determine_color_player(name)
	
	list_pos_topleft = x_matrix + DIFF_SIZE_PLAYER + y_matrix * LEDS_PER_ROW
	list_pos_bottemright= x_matrix + (y_matrix + DIFF_SIZE_PLAYER) * LEDS_PER_ROW
	
	self._matrix_colors [list_pos_topleft] = color
	self._matrix_colors [list_pos_bottemright] = color
    
    def draw(self):
	sense.clear()
	sense.set_pixels(self._matrix_colors)
		
		
		
	
