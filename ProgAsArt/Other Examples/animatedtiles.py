'''
    randommized tiles - Animated.
    cblouin@dal.ca
'''
# Import section
from graphics import *
from time import sleep
from random import randint

# Return a random color
def RandomColor():
	return color_rgb( randint(0,255) , randint(0, 255) , randint(0, 255) )

# some tweakable parameters
wait_time = 1000
width = 600
height = 600
boxesize = 20

# A list to store all box objects so that they can be modified later
boxes = []

# Create a window
win = GraphWin('Tiles!', width, height)
win.setBackground('black')

# Build the tile pattern
n_row = int(width / boxesize)
n_col = int(height / boxesize)

# This fills the window with tiles of random colours
for col in range(n_col):
	# Coordinate
	minX = col * boxesize
	maxX = 	( col + 1 ) * boxesize

	for row in range(n_row):
		# Coordinate
		minY = row * boxesize
		maxY = 	( row + 1 ) * boxesize

		# Make a box
		box = Rectangle( Point(minX, minY), Point(maxX, maxY) )
		box.setFill( RandomColor() )
		box.draw(win)

		# Add to the list
		boxes.append( box )

# Change random tiles black
for i in range( 2 * len( boxes )):
	# Pick a random box from the list
	rndbox = randint(0,len(boxes)-1)
	box = boxes[rndbox]

	# Set it to black
	box.setFill('black')
	
	# Wait for 50 millisecond
	sleep(0.05)

# Wait for a click to close
win.getMouse()
win.close()
