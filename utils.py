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

