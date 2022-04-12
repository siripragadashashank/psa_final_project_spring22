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


def remove_duplicates(states):
    '''
    Remove duplicate states after checking
    possible flips and rotations
    '''
    n = len(states)
    dups = []

    for i in range(n - 1):

        cur = list(states[i])
        for j in range(i+1, n):
            nxt = states[j]
            match, nrotates, nflips = isequal(nxt, cur)
            if match: dups.append(j)
            else: continue

    dups = list(set(dups))
    uniq = []

    for p in range(n):

        if(bool(dups.count(p))): continue
        else: uniq.append(states[p])

    return uniq


def set_possible_moves(states):
    '''
    Given a state set all possible moves

    Returns 
        possible_moves (hashmap): possible moves for 
        each state in states  
    '''
    n = len(states)
    possible_moves = {}

    for i in range(n):
        actions = []
        for j in range(len(states[i])):
            if states[i][j] == 0:
                actions.append(j)
                actions.append(j)

        possible_moves[tuple(states[i])] = actions
    
    return possible_moves

def get_required_action(cur_action, nrotates, nflips):
    '''
    Given an action, number of rotation and flips

    Retruns: Transformed action 
    '''
    if nflips == 1:

        if cur_action == 0:   cur_action = 2
        elif cur_action == 3: cur_action = 5
        elif cur_action == 6: cur_action = 8
        elif cur_action == 2: cur_action = 0
        elif cur_action == 5: cur_action = 3
        elif cur_action == 8: cur_action = 6

    while nrotates > 0:

        nrotates = nrotates - 1
        
        if cur_action == 1:   cur_action = 5
        elif cur_action == 5: cur_action = 7
        elif cur_action == 7: cur_action = 3
        elif cur_action == 3: cur_action = 1
        elif cur_action == 0: cur_action = 2
        elif cur_action == 2: cur_action = 8
        elif cur_action == 8: cur_action = 6
        elif cur_action == 6: cur_action = 0

    return cur_action


def get_original_action(cur_action, nrotates, nflips):
    '''
    Given an action, number of rotation and flips

    Returns: Original action 
    '''
    nrotates = 4 - nrotates
    
    while nrotates > 0:
        
        nrotates = nrotates - 1
        
        if cur_action == 1:   cur_action = 5
        elif cur_action == 5: cur_action = 7
        elif cur_action == 7: cur_action = 3
        elif cur_action == 3: cur_action = 1
        elif cur_action == 0: cur_action = 2
        elif cur_action == 2: cur_action = 8
        elif cur_action == 8: cur_action = 6
        elif cur_action == 6: cur_action = 0
    
    if nflips == 1:
        if cur_action == 0:   cur_action = 2
        elif cur_action == 3: cur_action = 5
        elif cur_action == 6: cur_action = 8
        elif cur_action == 2: cur_action = 0
        elif cur_action == 5: cur_action = 3
        elif cur_action == 8: cur_action = 6

    return cur_action