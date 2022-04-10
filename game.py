import os.path
from argparse import ArgumentParser
from menace import menace_vs_human, menace_train
from utils import save, load, ui
from states import isequal, inverse_transform_action
from states import check_win, next_level, delete_duplicates, set_random_moves


def init_states():

	states1 = [[1,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

	# init empty lists for all next possible states
	states2, states3, states4, states5 = [], [], [], []
	states6, states7, states8, states9 = [], [], [], []

	if os.path.exists('./model.dat'):
		print('Loading model.dat \n')
		states = load('./model.dat')

	else:
		print("Creating all possible states")
		
		print("No of first possible move states: ", len(states1))
		print('#######################################################\n')

		next_level(states1,states2,2)
		print("No. of next possible states: ", len(states2))
		states2 = delete_duplicates(states2)
		print("Reduced no. of states after eliminating duplicates: ", len(states2))
		print('#######################################################\n')

		next_level(states2,states3,1)
		print("No. of next possible states: ", len(states3))
		states3 = delete_duplicates(states3)
		print("Reduced no. of states after eliminating duplicates: ", len(states3))
		print('#######################################################\n')

		next_level(states3,states4,2)
		print("No. of next possible states: ", len(states4))
		states4 = delete_duplicates(states4)
		print("Reduced no. of states after eliminating duplicates: ", len(states4))
		print('#######################################################\n')
		
		next_level(states4,states5,1)
		print("No. of next possible states: ", len(states5))
		states5 = delete_duplicates(states5)
		print("Reduced no. of states after eliminating duplicates: ", len(states5))
		print('#######################################################\n')
		
		next_level(states5,states6,2)
		print("No. of next possible states: ", len(states6))
		states6 = delete_duplicates(states6)
		print("Reduced no. of states after eliminating duplicates: ", len(states6))
		print('#######################################################\n')
		
		next_level(states6,states7,1)
		print("No. of next possible states: ", len(states7))
		states7 = delete_duplicates(states7)
		print("Reduced no. of states after eliminating duplicates: ", len(states7))
		print('#######################################################\n')
		
		next_level(states7,states8,2)
		print("No. of next possible states: ", len(states8))
		states8 = delete_duplicates(states8)
		print("Reduced no. of states after eliminating duplicates: ", len(states8))
		print('#######################################################\n')
		
		next_level(states8,states9,1)
		print("No. of next possible states: ", len(states9))
		states9 = delete_duplicates(states9)
		print("Reduced no. of states after eliminating duplicates: ", len(states9))
		print('#######################################################\n')
		
		states =	states1 + states2 + states3 + states4 + \
					states5 + states6 + states7 + states8 + \
					states8

		## adding next possible moves for each of the states 
		states = set_random_moves(states)

		## adding first possible moves for MENACE - 0, 1, 4
		states = states + [[[0,0,0,0,0,0,0,0,0],[0,0,1,1,4,4]]]
		# print("No of state: ", len(states))

		save(states, 'init_states.dat')
		

	return states


if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('--mode', help='Play against menace or Train it')
	parser.add_argument('--iterations', type=int, help='Number of iterations for training')

	args = parser.parse_args()
	states = init_states()

	if args.mode == 'play':
		menace_vs_human(states)

	if args.mode == 'train':
		menace_train(states, args.iterations)
		save(states, 'model.dat')
	