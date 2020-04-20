def draw_a_gameboard(size, tic_tac = None):
	if tic_tac is None:
		tic_tac = [['   ' for j in range(size)] for i in range(size)]

	def intersperse(column, item):
	    column_result = [item] * (len(column) * 2 - 1)
	    column_result[0::2] = column
	    return column_result

	line =[' ---' for b in range(size)]
	column = ['|' for a in range(size)]

	print(''.join(line))

	c = 0

	for k in range(size):
			print(''.join(intersperse(column, game[k][c])) + '   |')
			print(''.join(line))
			if c == size:
				c = 0
			else:
				c +=1
def get_a_move():
	while True:
		row = int(input('Row: ')) - 1
		col = int(input('Col: ')) - 1
		if (row in range(size)) and (col in range(size)):
			return (row, col)
		print('Unacceptable number of row / column')

def move(player):
	while True:
		row, col = get_a_move()

		if game[row][col] == '   ':
			if player % 2 == 1:
				game[row][col] = 'X'
			else:
				game[row][col] = 'O'
			player += 1
			break
		else:
			print('The field you chose is filled! \nChoose another one please!')

	return game

print('Let`s play Tic Tac Toe!')
size = int(input('Size of the table: '))

game = [['   ' for j in range(size)] for i in range(size)]

draw_a_gameboard(size)

player = 1
while True:
	game = move(player)
	print(game)
	draw_a_gameboard(size, game)
	player +=1





