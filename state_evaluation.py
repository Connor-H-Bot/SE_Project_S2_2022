import math
import game_logic

# Ideas:
#- the number of your scoring pieces in the row/column with the most of them (i.e. nearness to an optimal road)
#- orthogonal length of the longest connected chain of pieces
#- flat coverage (for tie breakers)
#- number of spaces your pieces can influence
#- the number of your pieces that can influence each other space
#- number of captive and reserves
def score(board, player):
	squareValueMap = [
		100, 150, 150, 100,
		150, 200, 200, 150,
		150, 200, 200, 150,
		100, 150, 150, 100
	]

	pieceValueMap = {
		"F": 200,
		"S": 200
	}

	wScore = 0
	bScore = 0

	for i in range(16):
		piece = game_logic.controllingPiece(board, i)
		if piece == None: continue

		if game_logic.pieceColor(piece) == "W":
			wScore = wScore + squareValueMap[i]*pieceValueMap[game_logic.pieceType(piece)]
		if piece == "BF":
			bScore = bScore + squareValueMap[i]*pieceValueMap[game_logic.pieceType(piece)]

	if player == "W":
		return wScore - bScore
	else:
		return bScore - wScore

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
