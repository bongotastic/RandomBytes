''' Zombie Dice Game Engine 

	cblouin@dal.ca

'''
import random

class ZDGame:

	dice = {'G':list('BBBFFS'), 'Y':list('BBFFSS'),'R':list('BFFSSS')}

	def __init__(self):
		# player roster
		self.players = []

		# Tally
		self.tallies = []

		# Cup
		self.cup = []

		# hand
		self.hand = []

		# Table
		self.table = []

	def InitRound(self):
		'''
		   Refill the cup and flush the table
		'''
		self.cup = list('GGGGGGYYYYRRR')

		self.table = []

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


