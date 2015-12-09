''' Zero Sum Two-players
'''
# import 
from random import random

# The Payoff Matrix
PayoffMatrix = [[5,-2,1],[6,4,-2],[0,7,-1]]

# Player 1 Strategy
p1_row = [0.5, 0.4, 0.1]
p1_col = [0.15, 0.25, 0.60]


# Player 2 Strategy
p2_row = [0.8, 0.1, 0.1]
p2_col = [0.0, 0.2, 0.8]

# Starting money
p1_money = 1000
p2_money = 1000


# Random selection
def RandomSelection( Vector ):
    rnd = random()
    
    i = 0
    
    while i < len(Vector) and rnd > Vector[i] :
        rnd -= Vector[i]
        i += 1
        
    return min(i, len(Vector)-1)

# One round payoff computation
def Payoff(Pmat, R, C):
    '''
       Pmat is the payoff matrix
       R is the row selection vector
       C is the column selection vector 
    '''
    row_selection = RandomSelection(R)
    col_selection = RandomSelection(C)
    
    return Pmat[row_selection][col_selection]
    
def PlayNRounds(N, Pmat, p1R, p1C, p2R, p2C, p1_money, p2_money):
    for i in range(N):
        # p1 goes first
        px = Payoff(Pmat, p1R, p2C)
        
        p1_money += px
        p2_money -= px
        
        # p2 goes first
        px = Payoff(Pmat, p2R, p1C)
            
        p2_money += px
        p1_money -= px 
        
    print ( 'Player 1: %d, Player 2: %d'%(p1_money, p2_money))
    return 1000 - p1_money
    

## Testing the code
p1_loss = []
for game in range(1000):
    
    loss = PlayNRounds(1000, PayoffMatrix, p1_row, p1_col, p2_row, p2_col, p1_money, p2_money)
    
    p1_loss.append(loss)
    
print sum(p1_loss) / float(len(p1_loss))
