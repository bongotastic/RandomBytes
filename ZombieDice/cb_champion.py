''' 
   Simple AI #1
   cblouin@dal.ca
'''
from ZDengine import ZDPlayer

class ai_champion(ZDPlayer):
    name = 'cb_champion'
    
    # Probabilities
    _p = {'G':{'B':0.5,'S':1./6}, 'Y':{'B':0.33,'S':0.33}, 'R':{'B':1./6,'S':0.5}}
    
    def __init__(self):
        ZDPlayer.__init__(self)
        
        
    def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
        '''
            The method called by the game to query a decision from the AI.
            INPUT:
               player_id (int) - the index in tallies of the AI player.
               tallies (list of list of int) - List of scores from rounds for all players.
               hand - (List of string) - List of dice in hand, coded by color (R,G,Y)
               cup - (list of string) - Similar to hand, but for what is left in the cup
               n_brain - (int) Current number of brains on the table
               n_shotgun - (int) Current number of shotgun on the table.
            OUTPUT:
               True - (bool) Proceed with another round of dice rolling
               False - (bool) Cash in the brains and stop the turn
               
            STRATEGY:
               ...
         '''
        # Always cash in, regardless of game state.
        return False