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
	flatCounts = game_logic.countFlatPieces(board)
	return flatCounts[player] - flatCounts["W" if player == "B" else "B"]
