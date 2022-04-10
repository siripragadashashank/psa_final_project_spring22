def save(states, filename):
    with open(filename, 'w') as f:
        
        for state in states:
            out = [str(x) for x in state[0]]
            out = ','.join(out)
            f.write(out+'\n')
            
            out = [str(x) for x in state[1]]
            out = ','.join(out)
            f.write(out+'\n')


def load(filename):
    states = []
    
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        lines = [x.split(',') for x in lines]
        output  = []
        
        for line in lines:
            temp = [int(x) for x in line]
            output.append(temp)
        states = []
        
        for i in range(0, len(output), 2):
            states.append([output[i], output[i+1]])

    return states

def ui(state):
    
    pos = list(state)
    
    for i in range(len(pos)):
        if pos[i] == 1: pos[i] = "X"
        if pos[i] == 2: pos[i] = "O"
        if pos[i] == 0: pos[i] = " "

    row1, row2, row3 = pos[0:3], pos[3:6], pos[6:9]

    print("  ", row1[0], "  |  ", row1[1], "  |  ", row1[2])
    print('----------------------')
    print("  ", row2[0], "  |  ", row2[1], "  |  ", row2[2])
    print('----------------------')
    print("  ", row3[0], "  |  ", row3[1], "  |  ", row3[2])

    print("\n\nIndices\n\n")

    print("  ", "0", "  |  ", "1", "  |  ", "2")
    print('----------------------')
    print("  ", "3", "  |  ", "4", "  |  ", "5")
    print('----------------------')
    print("  ", "6", "  |  ", "7", "  |  ", "8")