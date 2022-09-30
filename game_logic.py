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
	otherPlayer = "W" if activePlayer == "B" else "B"
	pieceCounts = countPieces(board)
	if pieceCounts[activePlayer] + pieceCounts[otherPlayer] < 5: return None

	if roadExists(board, activePlayer): return activePlayer
	if roadExists(board, otherPlayer): return otherPlayer

	if (pieceCounts[activePlayer] == 15 or
		pieceCounts[otherPlayer] == 15 or
		boardIsFull(board)):
		flatCounts = countFlatPieces(board)

		if flatCounts[activePlayer] > flatCounts[otherPlayer]:
			return activePlayer
		elif flatCounts[activePlayer] < flatCounts[otherPlayer]:
			return otherPlayer
		else:
			return "draw"

	return None


# returns all possible stack moves from the square represented by "index"
#
# A stack move is represented by a list that contains sub-moves.
# Example:
# 		move: [{"from": 0, "to": 1, "carry": 3}, {"from": 1, "to": 2, "carry": 1}]
#
# 		This means that, first the player moves 3 pieces from position 0 to position 1.
#		Once that is done, the player then moves 1 piece from position 1 to position 2.
def stackMoves(board, index):

	# returns all possible stack moves from "currentIndex" in the direction given by "direction"
	def stackMovesDirection(board, currentIndex, direction, carry):
		if carry == 0: return [[]]

		nextIndex = None
		if direction == "N": nextIndex = northIndex(currentIndex)
		elif direction == "S": nextIndex = southIndex(currentIndex)
		elif direction == "E": nextIndex = eastIndex(currentIndex)
		elif direction == "W": nextIndex = westIndex(currentIndex)
		if nextIndex == None: return False

		nextPiece = controllingPiece(board, nextIndex)
		if nextPiece and pieceType(nextPiece) == "S": return False

		moves = []
		for i in range(carry):
			current = stackMovesDirection(board, nextIndex, direction, carry - i - 1)
			if current == False: continue

			for move in current:
				subMove = {"from": currentIndex, "to": nextIndex, "carry": carry}
				moves.append([y for x in [[subMove], move] for y in x])

		return moves

	piecesInStack = len(board[index])
	carryLimit = piecesInStack if piecesInStack < 4 else 4
	moves = []
	for direction in ["N", "S", "E", "W"]:
		for carry in range(1, carryLimit + 1):
			directionMoves = stackMovesDirection(board, index, direction, carry)
			if directionMoves == False: continue
			moves = [y for x in [moves, directionMoves] for y in x if len(y)]

	return moves

# Returns all possible moves for "player" given the game state represented by "board"
#
# New pieces can be placed standing or flat on empty squares.
#
# Stacks of pieces can be moved in straight lines orthogonally
# from the starting point of the move - a player can't change move direction during the move.
# At least one piece from the moving stack must be left on each square that the move includes.
def moves(board, player):
	moves = []
	for index in range(16):
		piece = controllingPiece(board, index)
		if piece == None:
			moves.append({"to": index, "piece": player+"F"})
			moves.append({"to": index, "piece": player+"S"})
			continue

		if pieceColor(piece) != player: continue

		sMoves = stackMoves(board, index)
		moves = [y for x in [moves, sMoves] for y in x]

	return moves

def getXLast(square, x):
	return square[-x:]

def removeXLast(square, x):
	return square[:len(square)-x]

# makes a move that represents moving a stack
def makeStackMove(board, move, reverse=False):
	for subMove in ( reversed(move) if reverse else move ):
		source = subMove["from"] if not reverse else subMove["to"]
		target = subMove["to"] if not reverse else subMove["from"]
		carry = subMove["carry"]

		square = board[source]
		piecesToMove = getXLast(square, carry)
		board[source] = removeXLast(square, carry)

		board[target] = [y for x in [board[target], piecesToMove] for y in x]

	return board

# makes a move that represents placing a new piece
def placePiece(board, move, reverse=False):
	position = move["to"]
	piece = move["piece"]
	if not reverse:
		board[position].append(piece)
	else:
		board[position] = removeXLast(board[position], 1)

	return board

# Applies the move represented by "move" to the game state represented by "board"
# "move" can be either a stack move, or placement of a new piece
def makeMove(board, move):
	if type(move) == list:
		board = makeStackMove(board, move)
	else:
		board = placePiece(board, move)

	return board

# reverts "board" to the state it had before "move" was applied
# "move" can be either a stack move, or placement of a new piece
def unmakeMove(board, move):
	if type(move) == list:
		board = makeStackMove(board, move, True)
	else:
		board = placePiece(board, move, True)

	return board
