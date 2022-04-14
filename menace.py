import sys
import random, logging
from utils import save, load, ui
from states import get_required_action, get_original_action 
from states import is_win, check_equal, next_state, remove_duplicates

def menace_vs_human(states, ngames):
    '''
    Begin MENACE vs Human Play
    
    ngames (int): number of games human want to play against MENACE
                  Can be increase as seen fit 
    '''

    for i in range(ngames):
        win = 0
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
                        prob_score = states[s].count(move)/len(states[s]) * 100
                        print("Probability score for the move: {} {} %".format(move, prob_score))
                        
                        #picking the move with highest probability, i.e. highest count
                        if(states[s].count(move) > count):
                            most_prob_move = move
                            count = states[s].count(move)
  
                    menace_move = get_original_action(most_prob_move, nrotations, nflips)
                    
                    game_state[-1][1].append(menace_move)                    
                    new_state = list(game_state[-1][0])
                    new_state[menace_move] = 1
                    game_state.append([new_state, []])
                    
                    internal_state = list(s)
                    internal_state[most_prob_move] = 1
                    
                    break
            
            ui(game_state[-1][0])    
            
            if is_win(game_state[-1][0])!= 0:
                print("Menace won!") 
                break
            
            if sum(game_state[-1][0]) == 13:
                print("Draw!")
                break

            new_state = list(game_state[-1][0])
            
            while True:
                print("You choose")
                player_move = int(eval(input("Index: ")))   
                if new_state[player_move]!=0 : continue
                new_state[player_move] = 2
                break

            game_state.append([new_state, []])

            if is_win(game_state[-1][0])!= 0:
                print("You won!") 
                break

            ui(game_state[-1][0])
            if sum(game_state[-1][0]) == 13:
                print('Draw!')
                break
