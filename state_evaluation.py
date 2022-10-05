import math
import game_logic


def connections(board, index, controllingPiece):
	num = 0

	east = game_logic.eastIndex(index)
	west = game_logic.westIndex(index)
	south = game_logic.southIndex(index)
	north = game_logic.northIndex(index)

	eastPiece = None if east == None else game_logic.controllingPiece(board, east)
	westPiece = None if west == None else game_logic.controllingPiece(board, west)
	southPiece = None if south == None else game_logic.controllingPiece(board, south)
	northPiece = None if north == None else game_logic.controllingPiece(board, north)


	if northPiece == southPiece == controllingPiece:
		num = num + 16

	if eastPiece == westPiece == controllingPiece:
		num = num + 16

	if northPiece == eastPiece == controllingPiece:
		num = num + 8

	if northPiece == westPiece == controllingPiece:
		num = num + 8

	if southPiece == eastPiece == controllingPiece:
		num = num + 8

	if southPiece == westPiece == controllingPiece:
		num = num + 8

	return num




# Ideas:
#- the number of your scoring pieces in the row/column with the most of them (i.e. nearness to an optimal road)
#- orthogonal length of the longest connected chain of pieces
#- flat coverage (for tie breakers)
#- number of spaces your pieces can influence
#- the number of your pieces that can influence each other space
#- number of captive and reserves
def score(board, player):
	squareValueMap = [
		2, 3, 3, 2,
		3, 4, 4, 3,
		3, 4, 4, 3,
		2, 3, 3, 2
	]

	pieceValueMap = {
		"F": 2,
		"S": 10
	}

	wScore = 0
	bScore = 0

	for i in range(16):
		piece = game_logic.controllingPiece(board, i)
		if piece == None: continue

		if game_logic.pieceColor(piece) == "W":
			wScore = wScore + squareValueMap[i]*pieceValueMap[game_logic.pieceType(piece)] + connections(board, i, piece)
		if game_logic.pieceColor(piece) == "B":
			bScore = bScore + squareValueMap[i]*pieceValueMap[game_logic.pieceType(piece)] + connections(board, i, piece)

	if player == "W":
		return wScore
	else:
		return bScore

# Function for ordering moves based on how likely it is that they are good
#
# The reasoning behind move ordering is that, if the search algorithm encounteres the
# best moves first, it will be able to prune as many branches as possible off the search tree,
# making it more efficient.
def orderedMoves(board, player):
	def orderFun(move):
		boardRef = board
		boardRef = game_logic.makeMove(boardRef, move)
		scr = score(boardRef, player)
		boardRef = game_logic.unmakeMove(boardRef, move)
		return scr

	moves = game_logic.moves(board, player)
	moves.sort(reverse=True, key=orderFun)
	return moves
