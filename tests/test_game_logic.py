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
	board1 = [
		["WS"], ["WS"], []    , [],
		[]    , ["WS"], []    , [],
		[]    , ["WS"], ["WS"], ["WS"],
		[]    , []    , []    , []
	]

	# - black has a road
	board2 = [
		[], []    , []    , ["BF"],
		[], []    , ["BF"], ["BF"],
		[], ["BF"], ["BF"], [],
		[], ["BF"], []    , []
	]

	# - both players have a road, white placed the last piece
	board3 = [
		[]    , []    , []    , [],
		[]    , []    , []    , [],
		["WF"], ["WF"], ["WF"], ["WF"],
		["BS"], ["BS"], ["BS"], ["BS"]
	]

	# - both players have a road, black placed the last piece
	board4 = [
		[], ["WS"], ["BF"], [],
		[], ["WS"], ["BF"], [],
		[], ["WS"], ["BF"], [],
		[], ["WS"], ["BF"], []
	]

	# - the board is full, white has more flat pieces
	board5 = [
		["BF"], ["WF"], ["WF"], ["WF"],
		["WF"], ["BS"], ["BF"], ["BS"],
		["WF"], ["WF"], ["WF"], ["WS"],
		["BF"], ["BF"], ["BS"], ["BS"]
	]

	# - the board is full, black has more flat pieces
	board6 = [
		["BF"], ["WF"]      , ["BF"], ["WF"],
		["WF"], ["WF", "BF"], ["WF"], ["BF"],
		["WF"], ["BF"], ["WF", "BF"], ["BF"],
		["WF"], ["BF"], ["WF"]      , ["BF"]
	]

	# - the board is full, both players have an equal amount of flat pieces
	board7 = [
		["BF"], ["WF"]      , ["BF"], ["WF"],
		["WF"], ["WF", "BF"], ["WF"], ["BF"],
		["WF"], ["BF"]      , ["WF"], ["BF"],
		["WF"], ["BF"]      , ["WF"], ["BF"]
	]

	# - piece limit reached
	board8 = [
		["BF", "WF"], ["WF", "BF"], ["WF", "BF", "WF"], [],
		["WF", "BF"], ["WF"]      , ["WF", "BF", "WF"], ["WF", "BF"],
		["WF"]      , ["WF", "BF"], ["WF"]            , ["BF"],
		["WF"]      , ["WF"]      , []                , ["WF"]
	]

	# - piece limit reached
	board9 = [
		["BF", "WF"], ["WF", "BF"], ["WF", "BF", "WF"], [],
		["WF", "BF"], ["WF"]      , ["WF", "BF", "WF"], ["WF", "BF"],
		["WF", "BF"], ["WF", "BF"], ["WF"]            , ["BF"],
		["WF", "BF"], ["WF", "BF"], []                , ["WF"]
	]

	print("test_winner")
	print(game_logic.winner(board1, "W") == "W")
	print(game_logic.winner(board2, "B") == "B")
	print(game_logic.winner(board3, "W") == "W")
	print(game_logic.winner(board4, "B") == "B")
	print(game_logic.winner(board5, "W") == "W")
	print(game_logic.winner(board6, "B") == "B")
	print(game_logic.winner(board7, "W") == "draw")
	print(game_logic.winner(board8, "W") == "W")
	print(game_logic.winner(board9, "W") == "B")

test_road_exists()
test_winner()
