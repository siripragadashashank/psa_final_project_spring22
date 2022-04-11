import os.path
from utils import save, load, ui
from argparse import ArgumentParser
from menace import menace_vs_human, menace_train
from states import isequal, inverse_transform_action
from states import check_win, next_state, remove_duplicates, set_possible_moves


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

		next_state(states1,states2,2)
		print("No. of next possible states: ", len(states2))
		states2 = remove_duplicates(states2)
		print("Reduced no. of states after eliminating duplicates: ", len(states2))
		print('#######################################################\n')

		next_state(states2,states3,1)
		print("No. of next possible states: ", len(states3))
		states3 = remove_duplicates(states3)
		print("Reduced no. of states after eliminating duplicates: ", len(states3))
		print('#######################################################\n')

		next_state(states3,states4,2)
		print("No. of next possible states: ", len(states4))
		states4 = remove_duplicates(states4)
		print("Reduced no. of states after eliminating duplicates: ", len(states4))
		print('#######################################################\n')
		
		next_state(states4,states5,1)
		print("No. of next possible states: ", len(states5))
		states5 = remove_duplicates(states5)
		print("Reduced no. of states after eliminating duplicates: ", len(states5))
		print('#######################################################\n')
		
		next_state(states5,states6,2)
		print("No. of next possible states: ", len(states6))
		states6 = remove_duplicates(states6)
		print("Reduced no. of states after eliminating duplicates: ", len(states6))
		print('#######################################################\n')
		
		next_state(states6,states7,1)
		print("No. of next possible states: ", len(states7))
		states7 = remove_duplicates(states7)
		print("Reduced no. of states after eliminating duplicates: ", len(states7))
		print('#######################################################\n')
		
		next_state(states7,states8,2)
		print("No. of next possible states: ", len(states8))
		states8 = remove_duplicates(states8)
		print("Reduced no. of states after eliminating duplicates: ", len(states8))
		print('#######################################################\n')
		
		next_state(states8,states9,1)
		print("No. of next possible states: ", len(states9))
		states9 = remove_duplicates(states9)
		print("Reduced no. of states after eliminating duplicates: ", len(states9))
		print('#######################################################\n')
		
		states =	states1 + states2 + states3 + states4 + \
					states5 + states6 + states7 + states8 + \
					states8

		## adding next possible moves for each of the states 
		states = set_possible_moves(states)

		## adding first possible moves for MENACE - 0, 1, 4

		states[tuple([0,0,0,0,0,0,0,0,0])] = [0,0,1,1,4,4]
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
	