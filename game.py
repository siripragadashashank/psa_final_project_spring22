import os.path
import logging
from utils import save, load, ui
from argparse import ArgumentParser
from menace import menace_vs_human #, menace_train
from states import next_state, remove_duplicates, set_possible_moves


def init_states():

	states1 = [[1,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

	# init empty lists for all next possible states
	states2, states3, states4, states5 = [], [], [], []
	states6, states7, states8, states9 = [], [], [], []

	if os.path.exists('./model.dat'):
		logging.info('Loading model.dat \n')
		states = load('./model.dat')

	else:
		logging.info("Creating all possible states")
		logging.info("No of first possible move states: {}".format(len(states1)))
		logging.info('#######################################################')

		next_state(states1, states2, 2)
		logging.info("No. of next possible move states: {}".format(len(states2)))
		states2 = remove_duplicates(states2)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states2)))
		logging.info('#######################################################')

		next_state(states2, states3, 1)
		logging.info("No. of next possible move states: {}".format(len(states3)))
		states3 = remove_duplicates(states3)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states3)))
		logging.info('#######################################################')

		next_state(states3, states4, 2)
		logging.info("No. of next possible move states: {}".format(len(states4)))
		states4 = remove_duplicates(states4)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states4)))
		logging.info('#######################################################')
		
		next_state(states4, states5, 1)
		logging.info("No. of next possible move states: {}".format(len(states5)))
		states5 = remove_duplicates(states5)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states5)))
		logging.info('#######################################################')
		
		next_state(states5, states6, 2)
		logging.info("No. of next possible move states: {}".format(len(states6)))
		states6 = remove_duplicates(states6)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states6)))
		logging.info('#######################################################')
		
		next_state(states6, states7, 1)
		logging.info("No. of next possible move states: {}".format(len(states7)))
		states7 = remove_duplicates(states7)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states7)))
		logging.info('#######################################################')
		
		next_state(states7, states8, 2)
		logging.info("No. of next possible move states: {}".format(len(states8)))
		states8 = remove_duplicates(states8)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states8)))
		logging.info('#######################################################')
		
		next_state(states8, states9, 1)
		logging.info("No. of next possible move states: {}".format(len(states9)))
		states9 = remove_duplicates(states9)
		logging.info("Reduced no. of states after eliminating duplicates: {}".format(len(states9)))
		logging.info('#######################################################')
		
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
	
	logging.basicConfig(filename='game.log', level=logging.INFO, filemode='w')

	parser = ArgumentParser()
	parser.add_argument('--mode', help='Play against menace or Train it')
	parser.add_argument('--iterations', type=int, help='Number of iterations for training')

	args = parser.parse_args()
	states = init_states()

	if args.mode == 'play':
		menace_vs_human(states, 1)

	if args.mode == 'train':
		menace_train(states, args.iterations)
		save(states, 'model.dat')
	