import math
import time
import game_logic
import state_evaluation

counter = 0

# Returns the "best" move and it's score
# The implementation is based on the Minimax algorithm with alpha-beta pruning
#
# Possible improvements
# 1. Iterative deepening search
#    - Search-depths are tested from 1 to X, until some end condition on X occurs
#    - Helps always select the shortest path that leads to a win
#    - Makes it easier to interrupt searching when time limit is
#      reached, or no more resources are available
def findMove(board, player, depth):
	bestMove = {"move": None, "score": -math.inf}
	startDepth = depth

	def alphaBeta(board, player, depth, alpha, beta):
		if depth == 0:
			return state_evaluation.score(board, player)

		winner = game_logic.winner(board,  "W" if player == "B" else "B")
		if winner != None:
			if winner == "draw":
				return 0
			elif winner == player:
				return 1000000
			else:
				return -1000000

		for move in state_evaluation.orderedMoves(board, player):
			board = game_logic.makeMove(board, move)
			score = -alphaBeta(board, "W" if player == "B" else "B", depth - 1, -beta, -alpha)
			board = game_logic.unmakeMove(board, move)

			if score > alpha:
				if depth == startDepth:
					bestMove["move"] = move
					bestMove["score"] = score
				alpha = score
			if alpha >= beta:
				break

		return alpha


	alphaBeta(board, player, depth, -math.inf, math.inf)
	return bestMove
