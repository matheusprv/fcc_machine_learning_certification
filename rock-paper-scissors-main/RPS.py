# Quincy repeats RRPPS pattern
# Abbey tries to guess the next play based on the pattern from the last two plays
# Kris defeats my last play
# Mrugesh counter our play with most repetition in the last 10 rounds

winning_moves = {'R': 'P', 'P': 'S', 'S':'R'}
N = 4
RESET_HISTORY = 50

# Transition table made by taking the element at the i_th position and groupind the i_th + N elements
# If it already exists in the table, increases +1 in the occurencies of the pattern, otherwise it is 0
def mk_transition_table(opponent_history):
    transition_table = {}
    for i in range(len(opponent_history) - (N-1)):
        current = "".join(opponent_history[i:i+N])
        if current in transition_table: transition_table[current] += 1
        else: transition_table[current] = 1
    
    return transition_table

def player(prev_play, opponent_history=[]):
    if prev_play != '':
        opponent_history.append(prev_play)
    total_plays = len(opponent_history)
    
    # Checking if the minimum number of plays was reached
    if total_plays < N: return 'R'

    # Creating the transition table
    transition_table = mk_transition_table(opponent_history)

    # Taking the last N-1 previous opponent plays and creating the next possible ones
    previous_N_minus_one = "".join(opponent_history[-(N-1):])
    next_opponent_possibilities = [previous_N_minus_one + move for move in ['R', 'P', 'S']]
    
    # Calculates the probability of the next_opponent_possibilities according to what has already happended
    probabilities = {play: transition_table.get(play, 0) / total_plays for play in next_opponent_possibilities}

    # Verifica qual a jogada mais provável de ser feita com base nas que já foram feitas
    highest_probability = max(probabilities, key=lambda k: probabilities[k])[-1]

    return winning_moves[highest_probability]


