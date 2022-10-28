Board format
```
4	[12]	[13]	[14]	[15]
3	[8]	[9]	[10]	[11]
2	[4]	[5]	[6]	[7]
1	[0]	[1]	[2]	[3]
	a	b	c	d		
a1 is square 0 and d4 is square 15
```

Movestring formats: 
	1. Placing a piece: piece_type(F or S) position on the board(columnrow)
			Example - To place a flat piece on square 0: the move string is Fa1
					  To place a standing piece on square 11: the move string is Sd4

	2. Making a stacking/unstacking move: Number_of_pieces_to_pick_up Position_to_pick_from Direction(+,-,<,>)Number_of_pieces_to_place
			Example - To stack a piece from a1 to b1: the move string is 1a1>1
					  To unstack 3 pieces from c4 to 2 pieces on c3 and one piece on c2: the move string is 3c4-21	

Game.py file has a function execute_move which should be used to make a move.

Game platform and Game AI is integrated. Run the main_game_window.py to play the game.
