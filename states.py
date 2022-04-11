def vflip(state):
    '''
    Mirror image of a state
    '''

    flipped = list(state)

    flipped[2], flipped[5], flipped[8] = state[0], state[3], state[6]
    flipped[0], flipped[3], flipped[6] = state[2], state[5], state[8]

    return flipped

def rotate90(state):
    '''
    Rotate a state by 90 degrees
    '''
    rotated = list(state)
    
    rotated[0], rotated[2], rotated[8], rotated[6] = state[6], state[0], state[2], state[8]
    rotated[1], rotated[5], rotated[7], rotated[3] = state[3], state[1], state[5], state[7]

    return rotated

def next_state(cur, next, player):
    '''
    Obtain next state given current state and player
    '''
    # print(cur, '\n', 'len of state', len(cur))
    for i in range(len(cur)):
        for j in range(9):
            next_s = []
            if cur[i][j] == 0:
                next_s = list(cur[i]) 
                next_s[j] = player
                next.append(next_s)
    # print(next, '\n', 'len of state', len(next))