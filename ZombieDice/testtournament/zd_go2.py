''' 
   Simple AI #1
   cblouin@dal.ca
'''
from ZDengine import ZDPlayer

class zd_go2(ZDPlayer):
    name = 'zd_go2'
    
    def __init__(self):
        ZDPlayer.__init__(self)
        
    def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
        # Reroll if there is no brain in the hand
        # Last ditch attempt
        # Compute tallies
        scores = []
        for i in tallies:
            scores.append(sum(i))
            
        if scores[player_id] + n_brain >= 13:
            return False
        
        if n_brain < 4:
            return True
        return False