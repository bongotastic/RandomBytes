'''
    Bubble Lace - Python.
    cblouin@dal.ca
'''
# Import everything from Graphics
from graphics import *

# Import randint from random
from random import randint

# This function generate a random RGB color
def RandomColor():
	return color_rgb(randint(0,255), randint(0,255), randint(0,255))

# This function draws a circle, then calls itself to draw two smaller circles inside
def Replicant(x,y,height, radius):
	# Main circle
	c = Circle(Point(x,y), radius)

	# Random color which depends on where you are on the screen
	relx = (x/600.)*255
	color = color_rgb(255-relx,randint(0,255),relx)
	c.setFill(color)

	# Add to the window (important)
	c.draw(win)

	# Create circles with the circle if height is more than 0
	if height > 0:
		height -= 1
		Replicant(x-(radius/2),y,height,radius/2)
		Replicant(x+(radius/2),y,height,radius/2)


# Build a window
win = GraphWin('Bubble Lace', 600, 600)

# Start the pattern with one big circle
howdeep = 6
howbig  = 290
Replicant(300,300, howdeep, howbig)

# Wait to stop (don't modify this)
win.getMouse()
win.close()
