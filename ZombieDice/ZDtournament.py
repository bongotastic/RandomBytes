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
        
        # Player vector
        self.players = []
        
        # Number of player per game
        self.n_player = 4
        
        # Ranking system
        self.pool = 0
        self.stakes = 0.2
        
    def RegisterPlayer(self, player_instance):
        # Add a player instance
        self.players.append(player_instance)
        
        # Put a bet down
        self.pool += player_instance.rank * self.stakes
        
        # Take stakes and pool it
        player_instance.rank *= 0.9        
        
    def PrintOutcome(self):
        # Output string
        out = 'Player\tRank\n'
        
        # Gather ranks
        ranks = {}
        for i in self.players:
            if not i.rank in ranks:
                ranks[i.rank] = [i]
            else:
                ranks[i.rank].append(i)
        
        # Find largest rank
        while (len(ranks)):
            mx_rank = max(ranks)
            for p in ranks[mx_rank]:
                print (p.name, p.rank)
            del ranks[mx_rank]
        
        
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
    tournament = ZDTournament(10000)
    
    # Add players
    from ZDengine import ZDPlayer
    tournament.RegisterPlayer(ZDPlayer())
    
    from zd_upto2 import zd_upto2
    tournament.RegisterPlayer(zd_upto2())
    
    from zd_go1 import zd_go1
    tournament.RegisterPlayer(zd_go1())
    
    from zd_go2 import zd_go2
    tournament.RegisterPlayer(zd_go2())    
    
    tournament.Run()
    tournament.PrintOutcome()