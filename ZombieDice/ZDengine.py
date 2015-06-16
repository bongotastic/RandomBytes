''' Zombie Dice Game Engine 

	cblouin@dal.ca

'''
import random

class ZDGame:

	dice = {'G':list('BBBFFS'), 'Y':list('BBFFSS'),'R':list('BFFSSS')}

	def __init__(self):
		# player roster
		self.players = []
		self.cursor = 0

		# Tally
		self.tallies = []

		# Cup
		self.cup = []

		# hand
		self.hand = []

		# Table
		self.brains = []
		self.shotguns = []

	'''Metagaming methods'''
	def AddPlayer(self, player):
		self.players.append(player)
		self.tallies.append([])

	def PlayTurn(self):
		pass

	''' Mechanics that are not need for the AI
	'''
	def InitRound(self):
		'''
		   Refill the cup and flush the table
		'''
		self.cup = list('GGGGGGYYYYRRR')

		self.brains = []
		self.shotguns = []

	def RollOnce(self, color):
		# Get dice
		d = ZDGame.dice[color]

		# Pick a side
		return random.choice(d)

	def PullFromCup(self, n):
		# pulls n dice from cup
		random.shuffle(self.cup)

		out = self.cup[:n]

		self.cup = self.cup[n:]
		return out

	def FillHand(self):
		# Refill the hand by drawing from a cup
		self.hand.extend(self.PullFromCup( 3 - len(self.hand)))

	def AleaIactaEst(self):
		# Roll and sort each dice in hand
		for d in self.hand:
			outcome = self.RollOnce(d)

			if outcome == 'B':
				self.brains.append(d)

			elif outcome == 'S':
				self.shotguns.append(d)

		self.hand.remove('B')
		self.hand.remove('S')

	''' Possible Action to take
	'''
	def RollAgain(self):
		# AI triggers this method for another impulse
		self.FillHand()
		self.AleaIactaEst()

	def CashIn(self):
		# Cash in brains and move on
		if ShotgunCount() >= 3:
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
	def __init__(self):
		pass

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


