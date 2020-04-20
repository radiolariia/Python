print('Let`s play Tic Tac Toe!')

game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

def move(row, col, player):	
	while True:
		if player % 2 == 1:
			game[row - 1][col - 1] = 'X'
		else:
			game[row - 1][col - 1] = 'O'
		player += 1
	return game

playing = True

while playing:
	while True:
		row = int(input('Row: '))
		col = int(input('Col: '))
		if (row in range(0,4)) and (col in range(0,4)):
			break

	print(move(row, col, player))
	player +=1
		




