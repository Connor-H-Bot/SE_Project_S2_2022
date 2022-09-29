import math
import game_logic
import state_evaluation

# Returns the "best" move and it's score
# The implementation is based on the Minimax algorithm with alpha-beta pruning
#
# Possible improvements
# 1. Iterative deepening search
#    - Search-depths are tested from 1 to X, until some end condition on X occurs
#    - Helps always select the shortest path that leads to a win
#    - Makes it easier to interrupt searching when time limit is
#      reached, or no more resources are available
#    - Also makes improvement 2. possible
#
# 2. Caching states and scores, so that they can be looked up
#    - Store scores for the states in a hash table
#    - Need to be able to calculate a hash from a given game state
#    - When a previously seen game state is encountered, the score for this
#      state can be looked up instead of calculating it again
#
# 3. Order moves based on how good they are believed to be
#    - Come up with rules that determine if a move likely is good
#    - Before being searched through, the moves should be ordered after these rules.
#    - Aplha-beta pruning, will then have better chances of affecting efficieny
#
def findMove(board, player, depth):
	bestMove = {}
	startDepth = depth

	def alphaBeta(board, player, depth, alpha, beta):
		if depth == 0:
			return state_evaluation.score(board, "W" if player == "B" else "B")

		winner = game_logic.winner(board,  "W" if player == "B" else "B")
		if winner != None:
			if winner == "draw":
				return 0
			elif winner == player:
				return math.inf
			else:
				return -math.inf

		for move in game_logic.moves(board, player):
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
