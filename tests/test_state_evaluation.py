import sys
sys.path.append("../")

import state_evaluation

def test():
	#board = [
	#	["WF"], ["WF"], ["WF"], ["WF"],
	#	["WF"], [], [], [],
	#	["WF"], ["WF"], ["WF"], ["WF"],
	#	["WF"], ["WF"], ["WF"], ["WF"]
	#]

	board = [
		[], [], [], ["WF"],
		[], ["BF"], [], [],
		[], [], [], [],
		[], [], [], []
	]

	print(state_evaluation.maxOrthogonalRoadLength(board, "W"))

test()
