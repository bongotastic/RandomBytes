'''
    Random triangle art - Python.
    cblouin@dal.ca
'''
# Import everything from Graphics
from graphics import *
from random import randint

# Return a random point on the surface
def RandomPoint():
	return Point( randint(5,595) , randint(5,595) )

# Return a random color
def RandomColor():
	return color_rgb( randint(0,255) , randint(0, 255) , randint(0, 255) )


# Build a window
win = GraphWin('Test 1', 600, 600)

# repeat something 40 times
number_of_triangle = 40
for t in range( number_of_triangle ):
	# Random triangle
	poly = Rectangle( RandomPoint(), RandomPoint() )
	poly.setFill( RandomColor() )
	poly.draw(win)

# Wait to stop
win.getMouse()
win.close()
