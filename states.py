def vflip(state):
    '''
    Get Mirror image (flipped) of a state

    Returns: Flipped state
    '''

    flipped = list(state)

    flipped[2], flipped[5], flipped[8] = state[0], state[3], state[6]
    flipped[0], flipped[3], flipped[6] = state[2], state[5], state[8]

    return flipped

def rotate90(state):
    '''
    Rotate a given state by 90 degrees right

    Returns: Rotated state
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
    return next
    # print(next, '\n', 'len of state', len(next))

def remove_duplicates(states):
    '''
    Remove duplicate states after checking
    possible flips and rotations

    Returns : states after removing duplicates
    '''
    n = len(states)
    dups = []

    for i in range(n - 1):

        cur = list(states[i])
        for j in range(i+1, n):
            nxt = states[j]
            match, nrotates, nflips = check_equal(nxt, cur)
            if match: dups.append(j)
            else: continue

    dups = list(set(dups))
    uniq = []

    for p in range(n):

        if(bool(dups.count(p))): continue
        else: uniq.append(states[p])

    return uniq


def set_possible_moves(states, alpha=2):
    '''
    Given a state set all possible moves

    Returns : possible_moves (hashmap): possible moves for 
              each state in states  
    '''
    n = len(states)
    possible_moves = {}

    for i in range(n):
        actions = []
        for j in range(len(states[i])):
            if states[i][j] == 0:
                for alp in range(alpha):
                    actions.append(j)
                    #actions.append(j)

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


def is_win(board_state):
    '''
    Given a board state check whether MENACE or human has won

    Returns: 1 for MENACE win, 2 for human win, 0 for no win
    '''

    ## Cases when MENACE has won -> return 1
    
    if board_state[0] == 1 and board_state[1] == 1 and board_state[2] == 1: return 1
    if board_state[0] == 1 and board_state[3] == 1 and board_state[6] == 1: return 1
    if board_state[0] == 1 and board_state[4] == 1 and board_state[8] == 1: return 1
    if board_state[1] == 1 and board_state[4] == 1 and board_state[7] == 1: return 1
    if board_state[2] == 1 and board_state[5] == 1 and board_state[8] == 1: return 1
    if board_state[2] == 1 and board_state[4] == 1 and board_state[6] == 1: return 1
    if board_state[3] == 1 and board_state[4] == 1 and board_state[5] == 1: return 1
    if board_state[6] == 1 and board_state[7] == 1 and board_state[8] == 1: return 1

    ## Cases when human has won -> return 2

    if board_state[0] == 2 and board_state[1] == 2 and board_state[2] == 2: return 2
    if board_state[0] == 2 and board_state[3] == 2 and board_state[6] == 2: return 2
    if board_state[0] == 2 and board_state[4] == 2 and board_state[8] == 2: return 2
    if board_state[1] == 2 and board_state[4] == 2 and board_state[7] == 2: return 2
    if board_state[2] == 2 and board_state[5] == 2 and board_state[8] == 2: return 2
    if board_state[2] == 2 and board_state[4] == 2 and board_state[6] == 2: return 2
    if board_state[3] == 2 and board_state[4] == 2 and board_state[5] == 2: return 2
    if board_state[6] == 2 and board_state[7] == 2 and board_state[8] == 2: return 2
    
    return 0

def match_two_states(s1, s2):
    '''
    Given two states check whether they are 
    equal by iterating through them

    Returns : bool
    '''
    is_match = True
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            is_match = False
            break
    return is_match

def check_equal(state_1, state_2):
    '''
    Given two states check whether they are equal 
    after all possible flips and rotations
    
    Returns : bool - indicating whether two states or equal
              nrotations - number of rotations to achieve equality
              nflips - number of flips to achieve equality
    '''

    nflips, nrotations = 0, 0
    s1, s2 = state_1, list(state_2)
    
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    ## one rotation
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    ## two rotations
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    ## three rotations
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips

    ## Flip
    s2 = vflip(list(state_2))
    nflips += 1
    nrotations = 0    
    if match_two_states(s1, s2) : return True, nrotations, nflips

    ## one rotation
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    ## two rotations
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    ## three rotations
    nrotations += 1
    s2 = rotate90(s2)
    if match_two_states(s1, s2) : return True, nrotations, nflips
    
    return False, nrotations, nflips


