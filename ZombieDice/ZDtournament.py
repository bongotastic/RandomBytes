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
        self.disqualified = []
        
        # Ranking system
        self.pool = 0
        self.stakes = 20.0
        self.pool_init = 200.0
        self.table_round = 100
        
    def RegisterPlayer(self, player_instance):
        # Add a player instance
        self.players.append(player_instance)
        
        # Seed ranking system
        player_instance.rank = self.pool_init
            

    def LoadFolder(self, foldername):
        # Set tournament name
        self.name = foldername

        # Import all files of the pattern zd_*
        for fname in listdir(foldername):
            if fname.startswith('zd_') and fname.endswith('.py'):
                # Remove extension
                x = import_module(fname[:-3])

                for i in range(2):
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
        fout = open('leaderboard_%d_%d.html'%(self.n_player, self.n_round),'w')
        
        # Header bit
        fout.write('<html>\n<title>Zombie Dice Leaderboard</title><body>\n')
        
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
                effwin = -1
                if p.n_win != 0:
                    effwin = 1000*p.clock/p.n_win
                    
                fout.write('<tr><td>%d</td><td>%s</td><td>%f</td><td>%d</td><td>%.3f</td></tr>\n'%(ranking, p.name, p.rank, p.n_win, effwin))
            del ranks[mx_rank]   
            ranking += 1
        
        # End table
        fout.write('</table>')
        
        # Close file
        fout.write('</body>\n</html>\n')
        fout.close()
        
    def LeaderboardCSV(self):
        ''' output to a csv file
        '''
        # Open file
        fout = open('leaderboard_%d_%d.csv'%(self.n_player, self.n_round),'w')
        fout.write('Name, rank, wins, games, efficiency, division\n')
        
        for p in self.players:
            # Efficiency
            efficiency = "--"
            if p.n_win:
                efficiency = str(1000*p.clock/p.n_win)
            
            fout.write('%s, %f, %d, %d, %s, %d\n'%(p.name, p.rank, p.n_win, p.n_game, efficiency, p.division))
        
        # Close file
        fout.close()
            
    def BuildPool(self, players):
        ''' Determine the expected earnings for each players
        '''
        # Reset
        self.pool = 0.0
        
        # Calculate priors
        pool = 0.0
        for i in players:
            pool += i.rank
            
        # Determine expected victory frequency
        for i in players:
            i.expected = i.rank/pool
            
            # Withdraw from AI
            i.rank -= i.expected * self.stakes
            
            # Add to pool
            self.pool += i.expected * self.stakes
            
            
        
        
    def Run(self):
        ''' Run tournament of n_rounds and n_players
        '''
        # determine number of game to average n_rounds of n_players for all players
        if self.n_player >= len(self.players):
            n_rounds = self.n_round
        else:
            n_rounds = int(self.n_round * (float(len(self.players))/self.n_player))
            
        print('Will need to run %d mini-tournament of %d games [Total of: %d games]'%(n_rounds, self.table_round, n_rounds*self.table_round))
            
        
            
        for i in range(n_rounds):
            # Pick players for next game
            shuffle(self.players)
            players = self.players[:self.n_player]  
            
            # Set pool of credits
            self.BuildPool(players)   
            
            # Local wins
            local_wins = {}
            for p in players:
                local_wins[p] = 0
            
            
            for j in range(self.table_round):
                # Create a game
                game = ZDGame()
                
                # Add players
                for p in players:
                    game.AddPlayer(p)
                    
                # Run Game
                game.PlayGame()
                
                # Clean up disqualified AI
                for ai in game.GetDisqualified():
                    self.players.remove(ai)
                    players.remove(ai)
                    self.disqualified.append(ai)
                
                # Register winner
                winner = game.GetWinner()       
                
                # Grant awards
                winner.n_win += 1
                
                # record win locally
                local_wins[winner] += 1
            
            # Update the ranks
            for ai in players:
                # Actual frequency of winnings
                freq_win = float(local_wins[ai]) / self.table_round
                
                # Update ranks
                ai.rank += freq_win * self.pool
                
            # write partial results for impatient people
            if i % 200 == 0:
                self.LeaderboardCSV()
                self.Leaderboard()
                print("Concluded game %d of %d ."%(i, n_rounds))
                
        

if __name__ == "__main__":
    # Create a tournament with 4 players per table
    tournament = ZDTournament(5000)
    tournament.n_player = 4
    
    # Add players
    tournament.LoadFolder('.')   
    
    # Add baseline
    tournament.RegisterPlayer(ZDPlayer())
    
    tournament.Run()
    tournament.PrintOutcome()
    tournament.Leaderboard()
    
    # Create a tournament -- 1 vs 1
    tournament = ZDTournament(5000)
    tournament.n_player = 2
    
    # Add players
    tournament.LoadFolder('.')   
    
    # Add baseline
    tournament.RegisterPlayer(ZDPlayer())
    
    tournament.Run()
    tournament.PrintOutcome()
    tournament.Leaderboard()    