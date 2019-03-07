####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team6' # Only 10 chars displayed.
strategy_name = 'Geurilla'
strategy_description = 'We are colluding with a certain team and betraying everyone else'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    
    "strategy 1"
    if their_history[0:3] == 'ccb':
        return 'c'
    elif len(my_history) == 0:
        return 'c'
    elif my_history == 'c':
        return 'c'
    else:
        return 'b'
    
    '''
    "strategy 2"
    if their_history[len(their_history)-5:len(their_history)] == "bcbcb" or "cbcbc" or "ccccc" or "bbbbb":
        return "b"
    else:
        return 'c'
    '''
 
    '''
    "strategy 3"
    if len(my_history) < 51:
        return "b"
    else:
        return "c"
    '''
