from enum import Enum

# Start location of the player on the gameboard
X_COORD_START = 1
Y_COORD_START = 1

class PlayerName(Enum):
	UNDEFINED = 0
	X = 1
	O = 2

class Player():
	def __init__(self):
		self._name = PlayerName.X
		self._reset_coordinates()

	def _reset_coordinates(self):
		self._x = X_COORD_START
		self._y = Y_COORD_START
		
	def next(self):
		self._name = PlayerName.X if self._name != PlayerName.X else PlayerName.O
		self._reset_coordinates()

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y

	def set_coordinates(self, x, y):
		self._x = x
		self._y = y

	def get_name(self):
		return self._name

	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def get_coordinates(self):
		return self._x, self._y
		
