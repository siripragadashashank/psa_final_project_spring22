def print_tictactoe_board(state):
	print('\n-----------')
	for i in range(len(state)):
		print(state[i] + ' | ', end = '')
		if (i+1)%3==0:
			print('\n-----------')