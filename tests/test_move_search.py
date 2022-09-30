import sys
sys.path.append("../")

import time
import move_search

def test():
	board = [
		[], [], [], [],
		[], [], [], [],
		[], [], [], [],
		[], [], [], [],
	]

	start = time.time()
	print(move_search.findMove(board, "W", 5))
	end = time.time()
	print(end - start)

test()
