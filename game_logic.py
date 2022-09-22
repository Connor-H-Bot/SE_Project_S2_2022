# The 4x4 board is represented by a list with 16 positions.
# Each position holds a list that contains the pieces
# that have been placed on that particular position.
# An empty board representation looks like:
# [
#   [], [], [], [],
#   [], [], [], [],
#   [], [], [], [],
#   [], [], [], []
# ]
#
# There are 4 possible pieces
# "WF" - White flat
# "WS" - White standing
# "BF" - Black flat
# "BS" - Black standing
#
# A board representation with 3 pieces could look like:
# [
#   ["WF", "BF"], ["WF"], [], [],
#   []          , []    , [], [],
#   []          , []    , [], [],
#   []          , []    , [], []
# ]
#
# The last piece in each list is the piece that controlls that particular square.
# The square represented by ["WF", "BF"] in the above example is therefore controlled by
# the piece "BF".
#

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

# returns true if "board" contains a valid road created by "player"
def roadExists(board, player):

	# reursively determines if "player" has a valid road from "currentIndex" to "targetIndex"
	def roadExistsRecursive(currentIndex, targetIndex, visited = []):
		if currentIndex in visited: return False

		currentPiece = controllingPiece(board, currentIndex)
		if currentPiece == None: return False
		if pieceColor(currentPiece) != player: return False
		if len(visited):
			lastPiece = controllingPiece(board, visited.copy().pop())
			if currentPiece != lastPiece: return False

		if currentIndex == targetIndex:
			return True

		for adjacentIndex in adjacentIndices(currentIndex):
			road = roadExistsRecursive(adjacentIndex, targetIndex, [y for x in [visited, [currentIndex]] for y in x])
			if road: return True

		return False


	return (# corner to corner
			roadExistsRecursive(0, 15) or
			roadExistsRecursive(3, 12) or

			# North to South
			roadExistsRecursive(0, 12) or
			roadExistsRecursive(0, 13) or
			roadExistsRecursive(0, 14) or
			roadExistsRecursive(1, 12) or
			roadExistsRecursive(1, 13) or
			roadExistsRecursive(1, 14) or
			roadExistsRecursive(1, 15) or
			roadExistsRecursive(2, 12) or
			roadExistsRecursive(2, 13) or
			roadExistsRecursive(2, 14) or
			roadExistsRecursive(2, 15) or
			roadExistsRecursive(3, 13) or
			roadExistsRecursive(3, 14) or
			roadExistsRecursive(3, 15) or

			# West to East
			roadExistsRecursive(0, 3) or
			roadExistsRecursive(0, 7) or
			roadExistsRecursive(0, 11) or
			roadExistsRecursive(4, 3) or
			roadExistsRecursive(4, 7) or
			roadExistsRecursive(4, 11) or
			roadExistsRecursive(4, 15) or
			roadExistsRecursive(8, 3) or
			roadExistsRecursive(8, 7) or
			roadExistsRecursive(8, 11) or
			roadExistsRecursive(8, 15) or
			roadExistsRecursive(12, 7) or
			roadExistsRecursive(12, 11) or
			roadExistsRecursive(12, 15))

# Counts the number of flat pieces that each player has on the board,
# that count towards winning the game (only flat pieces that are controlling a square).
def countFlatPieces(board):
	wf = 0
	bf = 0
	for index in range(16):
		piece = controllingPiece(board, index)
		if piece == "WF":
			wf = wf + 1
		if piece == "BF":
			bf = bf + 1

	return {
		"W": wf,
		"B": bf
	}

# Counts the number of pieces that each playes has placed on the board
def countPieces(board):
	w = 0
	b = 0
	for i in range(16):
		for j in range(len(board[i])):
			if pieceColor(board[i][j]) == "W":
				w = w + 1
			else:
				b = b + 1

	return {
		"W": w,
		"B": b
	}

# returns true if "board" doesn't contain any empty squares, else false
def boardIsFull(board):
	for i in range(16):
		if controllingPiece(board, i) == None:
			return False
	return True

# Returns the player that has won the game, either "W" or "B".
# "activePlayer" is the player that made the move that resulted in
# the current state of "board".
#
# The first player to create a road wins the game.
#
# If a player makes a move that creates a road for both players,
# the player that made the move wins.
#
# If the board is full, or neither player has any pieces left to place, the game ends.
# In order to determine who wins in this case, the flat pieces on the board are counted,
# and the player with most flat pieces wins the game. Pieces that are underneath a stack of pieces do
# not count towards this score. If both players have an equal amount of flat pieces that count towards
# the score, the game ends in a draw.
def winner(board, activePlayer):
	if roadExists(board, activePlayer): return activePlayer

	otherPlayer = "W" if activePlayer == "B" else "B"
	if (countPieces(board)[activePlayer] == 15 or
		boardIsFull(board)):
		flatCounts = countFlatPieces(board)

		if flatCounts[activePlayer] > flatCounts[otherPlayer]:
			return activePlayer
		elif flatCounts[activePlayer] < flatCounts[otherPlayer]:
			return otherPlayer
		else:
			return "draw"

	return None
