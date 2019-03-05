####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'SravAN' # Only 10 chars displayed.
strategy_name = 'Analyzer - B Heavy'
strategy_description = 'Analyzes Opponents moves and responds accordingly but prefers to betray if chance happens'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    if their_history [-3:] == 'ccc':
      return 'b'
    elif their_history [-2:]  == 'cc':
      return 'c'
    else:
        return 'b'
                
