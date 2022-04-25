import time
import os.path
import logging
from utils import setup_logger
from utils import save, load, ui
from argparse import ArgumentParser
from menace_selfplay import menace_train
from menace_humanplay import menace_vs_human 
from states import next_state, remove_duplicates, set_possible_moves


def init_states(mode):

	states1 = [[1,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

	# init empty lists for all next possible states
	states2, states3, states4, states5 = [], [], [], []
	states6, states7, states8, states9 = [], [], [], []

	if os.path.exists('./model.dat') and mode=='play':
		game_log.info('Loading model.dat \n')
		states = load('./model.dat')

	else:
		print("Creating all possible states for MENACE, refer game.log")
		game_log.info("No of first possible move states: {}".format(len(states1)))
		game_log.info('#######################################################')

		states2 = next_state(states1, states2, 2)
		game_log.info("No. of next possible move states: {}".format(len(states2)))
		states2 = remove_duplicates(states2)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states2)))
		game_log.info('#######################################################')

		states3 = next_state(states2, states3, 1)
		game_log.info("No. of next possible move states: {}".format(len(states3)))
		states3 = remove_duplicates(states3)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states3)))
		game_log.info('#######################################################')

		states4 = next_state(states3, states4, 2)
		game_log.info("No. of next possible move states: {}".format(len(states4)))
		states4 = remove_duplicates(states4)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states4)))
		game_log.info('#######################################################')
		
		states5 = next_state(states4, states5, 1)
		game_log.info("No. of next possible move states: {}".format(len(states5)))
		states5 = remove_duplicates(states5)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states5)))
		game_log.info('#######################################################')
		
		states6 = next_state(states5, states6, 2)
		game_log.info("No. of next possible move states: {}".format(len(states6)))
		states6 = remove_duplicates(states6)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states6)))
		game_log.info('#######################################################')
		
		states7 = next_state(states6, states7, 1)
		game_log.info("No. of next possible move states: {}".format(len(states7)))
		states7 = remove_duplicates(states7)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states7)))
		game_log.info('#######################################################')
		
		states8 = next_state(states7, states8, 2)
		game_log.info("No. of next possible move states: {}".format(len(states8)))
		states8 = remove_duplicates(states8)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states8)))
		game_log.info('#######################################################')
		
		states9 = next_state(states8, states9, 1)
		game_log.info("No. of next possible move states: {}".format(len(states9)))
		states9 = remove_duplicates(states9)
		game_log.info("Reduced no. of states after eliminating duplicates: {}".format(len(states9)))
		game_log.info('#######################################################')
		
		states =	states1 + states2 + states3 + states4 + \
					states5 + states6 + states7 + states8 + \
					states8

		## adding next possible moves for each of the states 
		states = set_possible_moves(states, 4)

		## adding first possible moves for MENACE - 0, 1, 4
		states[tuple([0,0,0,0,0,0,0,0,0])] = [0,0,0,0,1,1,1,1,4,4,4,4]
		# print("No of state: ", len(states))

		save(states, 'init_states.dat')
		print("States created")
		

	return states


if __name__ == '__main__':
	
	game_log = setup_logger('game', 'game.log')

	parser = ArgumentParser()
	parser.add_argument('--mode', help='Play against menace or Train it')
	parser.add_argument('--iterations', type=int, help='Number of iterations for training', default=1000)
	parser.add_argument('--probability', help='Probability for best strategy', default=0.7)

	args = parser.parse_args()
	states = init_states(args.mode)

	if args.mode == 'play':
		menace_vs_human(states, 1)

	if args.mode == 'train':
		start = time.time()
		print("Training MENACE for {} iterations, refer training.log for details".format(args.iterations))
		menace_train(states, args.iterations, float(args.probability))
		end = time.time()
		print("Training took {}".format(end-start))
		print("MENACE is trained and ready to play.")
		save(states, 'model.dat')
	