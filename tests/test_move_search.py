import sys
sys.path.append("../")

import time
import json
import move_search
import game_logic

def printBoard(board):

	for i in range(4):
		row = ""
		for j in range(4):
			index = (i * 4) + j
			piece = game_logic.controllingPiece(board, index)
			symbol = piece if piece != None else "  "
			row = row + "|"+symbol
		print(row, end="\n")
		print("------------")


board = [
	[], [], [], [],
	[], [], [], [],
	[], [], [], [],
	[], [], [], []
]


while True:
	inp = input("Enter move: ")
	if inp == "Q": break

	move = json.loads(inp)

	board = game_logic.makeMove(board, move)
	printBoard(board)

	winner = game_logic.winner(board, "W")
	if winner:
		if winner == "draw":
			print("DRAW")
		else:
			print(winner + " has won the game")

		break

	start = time.time()
	computerMove = move_search.findMove(board, "B", 5)
	end = time.time()
	print("Computers move: ", computerMove, end - start)

	board = game_logic.makeMove(board, computerMove["move"])
	printBoard(board)

	winner = game_logic.winner(board, "B")
	if winner:
		if winner == "draw":
			print("DRAW")
		else:
			print(winner + " has won the game")

		break
