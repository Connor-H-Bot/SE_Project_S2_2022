from operator import le
from random import random
import sys, time, socket, pdb
from telnetlib import GA
from unittest import case

from pyrsistent import v
import game
import copy

import move_search
import game_logic


depth = 5

def number2square(number):
	if number % 4 == 0:
		if number == 0:
			return 'a4'
		elif number == 4:
			return 'a3'
		elif number == 8:
			return 'a2'
		elif number == 12:
			return 'a1'
	elif number % 4 == 1:
		if number == 1:
			return 'b4'
		elif number == 5:
			return 'b3'
		elif number == 9:
			return 'b2'
		elif number == 13:
			return 'b1'
	elif number % 4 == 2:
		if number == 2:
			return 'c4'
		elif number == 6:
			return 'c3'
		elif number == 10:
			return 'c2'
		elif number == 14:
			return 'c1'	
	elif number % 4 == 3:
		if number == 3:
			return 'd4'
		elif number == 7:
			return 'd3'
		elif number == 11:
			return 'd2'
		elif number == 15:
			return 'd1'
	else:
		return 0		

def convertAImove(move):
	'''TODO
	convertAImove({'move': [{'from': 0, 'to': 4, 'carry': 3}], 'score': -40})
	convertAImove({'move': [{'from': 9, 'to': 5, 'carry': 4}, {'from': 5, 'to': 1, 'carry': 2}], 'score': -40})
	convertAImove({'move': [{'from': 5, 'to': 6, 'carry': 3}, {'from': 6, 'to': 7, 'carry': 2}], 'score': -40})
	convertAImove({'move': [{'from': 15, 'to': 14, 'carry': 2}, {'from': 14, 'to': 13, 'carry': 1}], 'score': -40})


	1. convert the placing move - F/S{square(a1)}
	2. convert the stacking move - {number of pieces}{square}{pieces per square}
	{'from': 0, 'to': 4, 'carry': 3}, {'from': 4, 'to': 8, 'carry': 2}
	'''
	if not isinstance(move['move'], list):
		game_move = move['move']['piece'][1] + number2square(move['move']['to'])
	else:
		game_move = str(move['move'][0]['carry']) + number2square(move['move'][0]['from'])
		direction_value = move['move'][0]['from'] - move['move'][0]['to']
		if abs(direction_value) % 4 == 0 and direction_value < 0:
			game_move = game_move + '-'
		elif abs(direction_value) % 4 == 0 and direction_value > 0:
			game_move = game_move + '+'
		elif abs(direction_value) % 4 == 1 and direction_value < 0:
			game_move = game_move + '>'
		elif abs(direction_value) % 4 == 1 and direction_value > 0:
			game_move = game_move + '<'
		else:
			return 0
		
		if len(move['move']) == 1:
			game_move = game_move + str(move['move'][-1]['carry'])
		else:
			for i in range(0,len(move['move'])-1):
				game_move = game_move + str(abs(move['move'][i+1]['carry'] - move['move'][i]['carry']))
			game_move = game_move + str(move['move'][-1]['carry'])
	return game_move



def update_board(board):
	"""TODO"""
	# UPDATE the board before sending it to the AI
	updated_board = [] * 16
	updated_board[0:4] = board[12:16]
	updated_board[4:8] = board[8:12]
	updated_board[8:12] = board[4:8]
	updated_board[12:16] = board[0:4]
	
	for index, square in enumerate(updated_board):
		if len(square) < 1:
			continue
		elif len(square) == 1:	
			output_string = "W" if square[0][0] == 0 else "B" 
			output_string = output_string + square[0][1]
			updated_board[index] = [output_string]
		else:
			output_list = []
			for ind, pos in enumerate(square):	
				output_string = "W" if pos[0] == 0 else "B"
				output_string = output_string + pos[1]	
				output_list.insert(ind, output_string)
			updated_board[index] = output_list
	return updated_board

def square_to_num_reverse(square_string):
		''' Return -1 if square_string is invalid
		'''
		if len(square_string) != 2:
			return -1
		if not square_string[0].isalpha() or not square_string[0].islower() or not square_string[1].isdigit():
			return -1
		row = ord(square_string[0]) - 96
		col = int(square_string[1])
		if row < 1 or row > 4 or col < 1 or col > 4:
			return -1
		return 4 * (4 - col) + (row - 1)

def check_game_status(status):
	if status == 0:
		print("Make a valid move")
		return 0
	elif status == 1:
		return 1
	else:
		if status == 2:	
			print("Game Over. Player 1 wins")
		elif status == 3:
			print("Game over. Player 2 wins")
		else:
			print("Game over. Match drawn")
		exit()

'''Implement W or B'''
def game_setup(game_board):
	
	game_board.render_board.render(game_board)
	game_board.render()
	if random() > 0.1:
		player_move = input('Make a move: ')
		status, curr_player = game_board.execute_move(player_move)
		while not status:
			player_move = input('Make a move: ')
			status, curr_player = game_board.execute_move(player_move)
		game_board.render()
		AI_board = copy.deepcopy(game_board.board)
		AI_move = move_search.findMove(update_board(AI_board), 'W', depth)
		status, curr_player = game_board.execute_move(convertAImove(AI_move))
		game_board.render()	
	else:
		player_move = move_search.findMove(copy.deepcopy(game_board.board), 'B', depth)
		status, curr_player = game_board.execute_move(convertAImove(player_move))
		game_board.render()

	while True:
		player_move = input('Make a move: ')
		status, curr_player = game_board.execute_move(player_move)
		if check_game_status(status):
			print(game_board.render())
			if game_board.moves != 1:
				if curr_player:
					next_player = 'W'
				else:
					next_player = 'B'
			else:
				next_player = 'W'
			AI_board = copy.deepcopy(game_board.board)
			AI_move = move_search.findMove(update_board(AI_board), next_player, depth)
			status, curr_player = game_board.execute_move(convertAImove(AI_move))
			print('AI move: ', convertAImove(AI_move))
			if check_game_status(status):
				print(game_board.render())
				continue
			
	
"""Convert the AI_move and execute move on GUI game board"""

"""Check status after the AI move"""
def start_game():
	game_board = game.Game(4, 'GUI')
	game_board.init_display()
	game_setup(game_board)
	game_board.display.mainloop()

