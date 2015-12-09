''' 
   Simple AI #1
   cblouin@dal.ca
'''
from ZDengine import ZDPlayer

class zd_go3(ZDPlayer):
    name = 'zd Good enough 3'
    
    def __init__(self):
        ZDPlayer.__init__(self)
        
    def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
        # Reroll if there is no brain in the hand
        if n_brain < 3:
            return True
        return False