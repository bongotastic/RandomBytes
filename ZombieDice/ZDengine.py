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

	def InitRound(self):
		'''
		   Refill the cup and flush the table
		'''
		self.cup = list('GGGGGGYYYYRRR')

		self.brains = []
		self.shotguns = []

	def AddPlayer(self, player):
		self.players.append(player)
		self.tallies.append([])

	''' Mechanics that are not need for the AI
	'''
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




if __name__ == "__main__":

	game = ZDGame()

	game.InitRound()

	print game.PullFromCup(3)


