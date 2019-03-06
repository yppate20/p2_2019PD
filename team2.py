team_name = 'Asian Guys' # Only 10 chars displayed.
strategy_name = 'majority rules'
strategy_description = 'In their history for their last 5 games, if they chose betray the majority of the time, then we will choose betray each time. If collude is the majority, we will also collude'

def move(my_history, their_history, my_score, their_score):
    '''reads their last 5 moves, then we play the move that they played a majority of the time (3+ times)'''
    last5 = their_history[-5:]
    betray = last5.count('b')
    collude = last5.count('c')
    if betray == 3:
        print 'b'
    elif betray == 4:
        print 'b'
    elif betray == 5:
        print 'b'
    elif collude == 3:
        print 'c'
    elif collude == 4:
        print 'c'
    elif collude == 5:
        print 'c'
    else:
        return 'b'  
