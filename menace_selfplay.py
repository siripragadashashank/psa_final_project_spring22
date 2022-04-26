import sys
import logging, datetime
from utils import setup_logger
from utils import ui, save, strategy
from states import is_win, next_state, remove_duplicates
from states import check_equal, get_original_action, get_required_action

training_log = setup_logger('training', 'training.log')

def learn(game_state, win, states):
    
    rew = int((10 - len(game_state))/2)
    
    for i in range(len(game_state)-1):
        
        action_actual = (game_state[i][1])[0]
        
        for s in states:
            
            is_match, rot, flip = check_equal(list(s), game_state[i][0])
            
            if is_match:
                
                action_internal = get_required_action(action_actual, rot, flip)
                
                if win == 1:
                    
                    if((i+1) % 2 != 0):
                        
                        loop = rew  + int((9 - (len(game_state) - i - 2))/2)
                        
                        for n in range(loop):                            
                            
                            states[s].append(action_internal)

                    else:
                        
                        loop = rew  + int((9 - (len(game_state) - i - 2))/2)
                        
                        for n in range(loop):
                            
                            if(states[s].count(action_internal) > 1):
                                
                                states[s].remove(action_internal)
                
                if(win == 2):
                    
                    if((i+1) % 2 != 0):  
                        
                        loop = rew  + int((9 - (len(game_state) - i - 2))/2)
                        
                        for n in range(loop):
                            
                            if(states[s].count(action_internal) > 1):
                                
                                states[s].remove(action_internal)
                    
                    else:
                        
                        loop = rew  + int((9 - (len(game_state) - i - 2))/2)
                        
                        for n in range(loop):
                            
                            states[s].append(action_internal)


def menace_train(states, iterations, probability):    
    
    for i in range(iterations): 

        # if i < iterations * probability:
        #     # random game with optimal human agent
        #     menace_agent_epsilon = 1 
        #     human_agent_epsilon = 0
        
        # else:
        #     # random game with random human agent
        #     menace_agent_epsilon = 1
        #     human_agent_epsilon = 1

        if i < iterations * (1/4):
            menace_agent_epsilon = 1 
            human_agent_epsilon = 1
        
        elif i < iterations * (1/2):
            menace_agent_epsilon = 1
            human_agent_epsilon = 0

        elif i < iterations * (3/4):
            menace_agent_epsilon = 0
            human_agent_epsilon = 1

        elif i < iterations * 1:
            menace_agent_epsilon = 1 - probability
            human_agent_epsilon = 1 - probability

        # menace_agent_epsilon = 1
        # human_agent_epsilon = 1 - probability

        training_log.info("Training Game {} Time: {}".format(i, datetime.datetime.now()))

        game_state = [[[0,0,0,0,0,0,0,0,0],[]]]
        
        win = 0
        
        training_log.info("menace_agent_epsilon: {} human_agent_epsilon: {} ".format(menace_agent_epsilon, human_agent_epsilon))
        
        while True:

            found = False
            for s in states:
                match, rot, flip = check_equal(list(s),game_state[-1][0])    
                
                if match:

                    (move1_internal, menace_agent_epsilon) = strategy(states[s], menace_agent_epsilon)

                    move1_actual = get_original_action(move1_internal, rot, flip)

                    game_state[-1][1].append(move1_actual)
                    new_state = list(game_state[-1][0])
                    new_state[move1_actual] = 1

                    game_state.append([new_state, []])
                    found = True
                    break
            
            
            found = False
            win = is_win(game_state[-1][0])      
            
            if win != 0:
                training_log.info("Won: MENACE_{}".format(win)) 
                learn(game_state, win, states)
                break

            if sum(game_state[-1][0]) == 13:
                training_log.info("Draw")
                break

            for s in states:
                match, rot, flip = check_equal(list(s),game_state[-1][0])
                
                if match:

                    (move2_internal, human_agent_epsilon) = strategy(states[s], human_agent_epsilon)

                    move2_actual = get_original_action(move2_internal, rot, flip)
                    
                    game_state[-1][1].append(move2_actual)
                    
                    new_state = list(game_state[-1][0])

                    new_state[move2_actual] = 2
                    game_state.append([new_state, []])

                    found = True
                    break

            win = is_win(game_state[-1][0])

            if win != 0:
                training_log.info("Won: MENACE_{}".format(win)) 
                learn(game_state, win, states)
                break