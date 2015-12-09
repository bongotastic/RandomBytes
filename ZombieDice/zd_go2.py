''' 
   Simple AI #1
   cblouin@dal.ca
'''
from ZDengine import ZDPlayer

class zd_go2(ZDPlayer):
    name = 'zd Good enough 4 with bailing out'
    
    def __init__(self):
        ZDPlayer.__init__(self)
        
    def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
        # Compute tallies
        scores = []
        for i in tallies:
            scores.append(sum(i))
            
        # Stop if a victory is possible
        if scores[player_id] + n_brain >= 13:
            return False
        
        # Stop unless you have 4+ brains
        if n_brain < 4:
            return True
        return False