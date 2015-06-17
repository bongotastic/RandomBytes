'''
   Tournament class
   cblouin@dal.ca
'''

from ZDengine import ZDGame
from random import shuffle

class ZDTournament:
    def __init__(self, n_round):
        # Maximum number of round
        self.n_round = n_round
        
        self.players = []
        
        self.pool = 0
        self.stakes = 0.1
        
    def RegisterPlayer(self, player_instance):
        # Add a player instance
        self.players.append(player_instance)
        
        # Put a bet down
        self.pool += player_instance.rank * self.stakes
        
        # Take stakes and pool it
        player_instance.rank *= 0.9        
        
    def Run(self):
        # Run n_round times
        for i in range(self.n_round):
            # Create a game
            game = ZDGame()
            
            # Add players
            for p in self.players:
                game.AddPlayer(p)
                
            # Run Game
            game.PlayGame()
            
            # Register winner
            winner = game.GetWinner()
            winner.RecordWin()
            
            # shuffle player orders
            shuffle(self.players)
            
        # Update ranks
        for player in self.players:
            # Prop win
            p_win = player.n_win / float(self.n_round)
            
            # rank update
            player.rank += p_win * self.pool
            

if __name__ == "__main__":
    # Create a tournament
    tournament = ZDTournament(1000)
    
    # Add players
    from ZDengine import ZDPlayer
    tournament.RegisterPlayer(ZDPlayer())
    tournament.RegisterPlayer(ZDPlayer())
    
    from zd_upto2 import zd_upto2
    tournament.RegisterPlayer(zd_upto2())
    
    from zd_go1 import zd_go1
    tournament.RegisterPlayer(zd_go1())
    
    tournament.Run()
    print tournament