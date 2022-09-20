import math

# returns the piece that controlls the square represented by "index"
def controllingPiece(board, index):
	stack = board[index]
	if len(stack) == 0: return None
	return stack.copy().pop()

# returns the piece-type of "piece"
def pieceType(piece):
	return piece[1]

# returns the color/player of "piece"
def pieceColor(piece):
	return piece[0]

# returns the row that "index" is located in, in a 4x4 matrix
def row(index):
	return math.floor(index / 4)

# returns the column that "index" is located in, in a 4x4 matrix
def column(index):
		return index % 4

# returns the index of the square that is north of "index" on the board
def northIndex(index):
	return index - 4 if index - 4 >= 0 else None

# returns the index of the square that is south of "index" on the board
def southIndex(index):
	return index + 4 if index + 4 < 16 else None

# returns the index of the square that is west of "index" on the board
def westIndex(index):
	return index - 1 if index - 1 >= 0 and row(index) == row(index - 1) else None

# returns the index of the square that is east of "index" on the board
def eastIndex(index):
	return index + 1 if index + 1 < 16 and row(index) == row(index + 1) else None

# returns the indices of the squares that are
# North, South, East and West of "index" on a 4x4 board
def adjacentIndices(index):
	adjacent = [northIndex(index), southIndex(index), westIndex(index), eastIndex(index)]
	return [i for i in adjacent if i != None]
