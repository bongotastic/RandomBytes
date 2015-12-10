'''
   Tournament class
   cblouin@dal.ca
'''

from ZDengine import ZDGame, ZDPlayer
from random import shuffle
from os import listdir
from importlib import import_module


class ZDTournament:
    def __init__(self, n_round):
        # Maximum number of round
        self.n_round = n_round
        
        # Ideal number of players
        self.n_player = 4
        
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

    def LoadFolder(self, foldername):
        # Set tournament name
        self.name = foldername

        # Import all files of the pattern zd_*
        for fname in listdir(foldername):
            if fname.startswith('zd_') and fname.endswith('.py'):
                # Remove extension
                x = import_module(fname[:-3])

                # INstanciate a player
                player = getattr(x, fname[:-3])()

                # Add it to the tournament
                self.RegisterPlayer(player)  
        
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
        
    def Leaderboard(self):
        ''' Create a leaderboard.
        '''
        # Open file
        fout = open('leaderboard.html','w')
        
        # Header bit
        fout.write('<html>\n<body>\n')
        
        # Table body       
        
        # Open table
        fout.write('<table><tr><td>Rank</td><td>Name</td><td>Credit</td><td>Wins</td><td>Time/win(ms)</td></tr>')
        
        # Gather ranks
        ranks = {}
        for i in self.players:
            if not i.rank in ranks:
                ranks[i.rank] = [i]
            else:
                ranks[i.rank].append(i)
    
        # Find largest rank
        ranking = 1
        while (len(ranks)):
            mx_rank = max(ranks)
            for p in ranks[mx_rank]:
                fout.write('<tr><td>%d</td><td>%s</td><td>%f</td><td>%d</td><td>%.3f</td></tr>\n'%(ranking, p.name, p.rank, p.n_win, 1000*p.clock/p.n_win))
            del ranks[mx_rank]   
            ranking += 1
        
        # End table
        fout.write('</table>')
        
        # Close file
        fout.write('</body>\n</html>\n')
        fout.close()
            
    def Run(self):
        ''' Run tournament of n_rounds and n_players
        '''
        # determine number of game to average n_rounds of n_players for all players
        n_rounds = max((self.n_round * len(self.players)) / self.n_player, self.n_round)
        
            
        for i in range(n_rounds):
            # Pick players for next game
            shuffle(self.players)
            players = self.players[:self.n_player]  
            
            # Set pool of credits
            credits = 0.0
            for p in players:
                p.n_game += 1
                x = p.rank * 0.1
                p.rank -= x
                credits += x            
            
            # Create a game
            game = ZDGame()
            
            # Add players
            for p in players:
                game.AddPlayer(p)
                
            # Run Game
            game.PlayGame()
            
            # Register winner
            winner = game.GetWinner()       
            
            # Grant awards
            winner.rank += credits
            winner.n_win += 1
            

if __name__ == "__main__":
    # Create a tournament
    tournament = ZDTournament(10000)
    
    # Add players
    tournament.LoadFolder('.')   
    
    # Add baseline
    tournament.RegisterPlayer(ZDPlayer())
    
    tournament.Run()
    tournament.PrintOutcome()
    tournament.Leaderboard()