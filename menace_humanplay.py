import sys
import random
import logging
from utils import ui
from states import check_equal, get_original_action, get_required_action
from states import is_win, next_state, remove_duplicates


def menace_vs_human(states, ngames):
    '''
    Begin MENACE vs Human Play
    
    ngames (int): number of games human want to play against MENACE
                  Can be increase as seen fit 
    '''

    for i in range(ngames):
        game_state = [[[0,0,0,0,0,0,0,0,0],[]]]
        print("\nBegin game {}\n".format(i))
        
        while True:
            print("MENACE's Turn\n")
            for s in states:

                match, nrotations, nflips =  check_equal(list(s), game_state[-1][0])
                
                if match:
                    most_prob_move, count = 0, 0
                    
                    # next moves
                    moves = list(set(states[s])) 
                    
                    for move in moves:
                        pscore = states[s].count(move)/len(states[s]) * 100
                        
                        # print("Probability for move: {} {} %".format(move, pscore))
                        
                        #picking move with highest probability, i.e. highest count
                        if(states[s].count(move) > count):
                            most_prob_move = move
                            count = states[s].count(move)
                    # print(most_prob_move)
                    
                    # most_prob_move = random.choice(states[s])
                    
                    # print(most_prob_move, nrotations, nflips)

                    menace_move = get_original_action(most_prob_move, 
                                                        nrotations, 
                                                        nflips)
                    
                    # print(menace_move)

                    game_state[-1][1].append(menace_move)                    
                    game_state[-1][0][menace_move] = 1 
                    game_state.append([game_state[-1][0], []])
                    
                    break
            
            ui(game_state[-1][0])    
            
            if sum(game_state[-1][0]) == 13:
                print("Draw!")
                break

            if is_win(game_state[-1][0])!= 0:
                print("Menace won!") 
                break
            
            while True:
                print("You choose")
                player_move = int(eval(input("Select index: ")))   
                if game_state[-1][0][player_move] != 0 : continue
                game_state[-1][0][player_move] = 2
                break

            game_state.append([game_state[-1][0], []])
            
            if sum(game_state[-1][0]) == 13:
                print('Draw!')
                break
            
            if is_win(game_state[-1][0])!= 0:
                print("You won!") 
                break



