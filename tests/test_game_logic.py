import sys
sys.path.append("../")

import game_logic

def test_road_exists():
	testBoard = [
		["WF"],["WF"],["WF"],["WF"],
		["WF"],["WF"],["WF"],["WF"],
		["WF"],["WF"],["WF"],["WF"],
		["WF"],["WF"],["WF"],["WF"]
	]

	testBoard2 = [
		["WF"],["BF"],["BS"],["WS"],
		["BF"],["WF"],["WF"],["WF"],
		["BS"],["WF"],["WF"],["WF"],
		["WS"],["WF"],["WF"],["WF"]
	]

	testBoard3 = [
		[],["WF", "WS"],[],[],
		[],["WF"]      ,[],[],
		[],["WF"]      ,[],[],
		[],["WF"]      ,[],[]
	]

	testBoard4 = [
		[],["WF"],[],[],
		[],["WF"],[],[],
		[],["WF"],[],[],
		[],["WF"],[],[]
	]

	print("test_road_exists")
	print(game_logic.roadExists(testBoard, "W") == True)
	print(game_logic.roadExists(testBoard2, "W") == False)
	print(game_logic.roadExists(testBoard2, "B") == False)
	print(game_logic.roadExists(testBoard3, "W") == False)
	print(game_logic.roadExists(testBoard3, "B") == False)
	print(game_logic.roadExists(testBoard4, "W") == True)
	print(game_logic.roadExists(testBoard4, "B") == False)


def test_winner():
	# - white has a road
	# - black has a road
	# - both players have a road, white placed the last piece
	# - both players have a road, black placed the last piece
	# - the board is full, white has more flat pieces
	# - the board is full, black has more flat pieces
	# - the board is full, both players have an equal amount of flat pieces
	return None

test_road_exists()
test_winner()
