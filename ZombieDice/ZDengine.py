''' 
	Zombie Dice Game Engine 

	cblouin@dal.ca

'''
import random
from time import time

'''
    Class that models a single game. All of the game logic is incoded here. Contestant do not need to know any of the interface in this 
    class.
'''
class ZDGame:

	# Structure of dice in Zombie Dice
	dice = {'G':list('BBBFFS'), 'Y':list('BBFFSS'),'R':list('BFFSSS')}

	def __init__(self):
		# player roster
		self.players = []
		
		# Current player (needed to cashing in)
		self.cursor = 0

		# Tally
		self.tallies = []

		# Cup - What dice can be drawn in the next round
		self.cup = []

		# hand - what was rolled as feet, or initially drawn
		self.hand = []

		# Table - Keep track of outcomes, regardless of color
		self.brains = []
		self.shotguns = []
		
		# Set pool
		self.pool = 0

	'''Metagaming methods'''
	def AddPlayer(self, player):
		''' INPUT:
		        player - an instance of a ZDPlayer child class
		'''
		self.players.append(player)
		self.tallies.append([])
		

	def PlayTurn(self):
		''' 
		    Iterate over all players and get them to complete their turn
		'''

		# Iterate over each players
		for pid in range(len(self.players)):
			# set current player
			self.cursor = pid
			
			# Initialize round
			self.InitRound()

			# Get Player
			player = self.players[pid]

			# Initial Run
			self.RollAgain()

			# Ask for decision
			decision = player.Play(pid, self.tallies, self.hand, self.cup, len(self.brains), len(self.shotguns))
			
			if decision == False or self.ShotgunCount() >= 3:
				self.CashIn()
				#print('Player %d scored %d for a total of %d'%(pid,len(self.brains), sum(self.tallies[pid])))			
				continue

			# Iterate
			while decision and len(self.shotguns) < 3 and len(self.hand) > 0:
				if decision:
					self.RollAgain()

				# Ask for decision #########
				# Before time
				beforetime = time()
				decision = player.Play(pid, self.tallies, self.hand, self.cup, len(self.brains), len(self.shotguns))
				player.clock += time() - beforetime
			
			# Cash in
			self.CashIn()
			#print('Player %d scored %d for a total of %d'%(pid,len(self.brains), sum(self.tallies[pid])))

	def PlayGame(self):
		''' 
		    Play turns until a player is victorious
		'''
		# Check for victory
		while self.Gameover() == False:
			self.PlayTurn()
		
	def GetWinner(self):
		'''
		    Obtain the instance of the victorious player. Used by the tournament class
		'''
		# Finds the winner
		final_scores = []
		
		# Compute scores
		for t in self.tallies:
			final_scores.append(sum(t))
			
		# Get max scores
		max_score = max(final_scores)
		
		# return the first to score max_score
		for i in range(len(final_scores)):
			if final_scores[i] == max_score:
				# update rank
				self.players[i].rank += self.pool
				return self.players[i]

	''' Mechanics that are not needed for the AI
	'''
	def Gameover(self):
		'''
		    Returns True if at least one player has a tally of 13 or more. Do not use unless a full turn is completed.
		'''
		for T in self.tallies:
			if sum(T) >= 13:
				return True
		return False
	
	def InitRound(self):
		'''
		   Refill the cup and clear the table
		'''
		self.cup = list('GGGGGGYYYYRRR')

		self.brains = []
		self.shotguns = []
		

	def RollOnce(self, color):
		'''
		    Draws a die outcome depending on the color of the dice.
		    INPUT: 
		        color (string) - Either R, G or Y (Red, Green or Yellow)
		    OUTPUT:
		        (string) - Either B, F, or S (Brain, Feet, Shotgun)
		'''
		# Get dice
		d = ZDGame.dice[color]

		# Pick a side
		return random.choice(d)

	def PullFromCup(self, n):
		'''
		    Draws n dice from the cup.
		    INPUT:
		       n (int) - number of dice to draw
		'''
		# pulls n dice from cup
		random.shuffle(self.cup)

		out = self.cup[:n]

		self.cup = self.cup[n:]
		return out

	def FillHand(self):
		'''
		    Transfer pulled dice from cup into the hand.
		'''
		# Refill the hand by drawing from a cup
		self.hand.extend(self.PullFromCup( 3 - len(self.hand)))

	def AleaIactaEst(self):
		'''
		    Roll three dice and hope for the best. Record Brains and Shotguns and keep feets into the hand.
		'''
		# temporary hand
		temphand = []
		
		# Roll and sort each dice in hand
		for d in self.hand:
			outcome = self.RollOnce(d)

			if outcome == 'B':
				self.brains.append(d)

			elif outcome == 'S':
				self.shotguns.append(d)
			else:
				temphand.append(d)
		
		self.hand = temphand



	''' Possible Action to take
	'''
	def RollAgain(self):
		# AI triggers this method for another impulse
		self.FillHand()
		self.AleaIactaEst()

	def CashIn(self):
		# Cash in brains and move on
		if len(self.shotguns) >= 3:
			self.tallies[self.cursor].append(0)
		else:
			self.tallies[self.cursor].append( self.BrainCount() )


	''' Informational methods for the AI
	'''
	def BrainCount(self):
		return len(self.brains)

	def ShotgunCount(self):
		return len(self.shotguns)


''' Base class for the AI player
'''
class ZDPlayer:
	name = 'Base class'
	def __init__(self):
		# These attributes are off bound for manipulation
		self.n_game = 0
		self.n_win = 0
		self.rank = 100
		self.clock = 0
		
	def Name(self):
		return self.name
	
	def RecordWin(self):
		self.n_win += 1

	def Play(self, player_id, tallies, hand, cup, n_brain, n_shotgun):
		''' 
		    Method used to request a decision from the player
		    returns:
		       True -> when the player decides to have another round.
		       False -> when the player decides to cash in the brains for the turn.
		'''
		# The base class player dumbly rolls only once, regardless of outcome.
		return False


def SetupTestGame(n):
	out = ZDGame()
	for i in range(n):
		out.AddPlayer( ZDPlayer() )
	return out


if __name__ == "__main__":

	game = SetupTestGame(4)
	game.PlayGame()

