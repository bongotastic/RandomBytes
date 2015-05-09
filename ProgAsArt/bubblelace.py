'''
    Test art - Python.
    cblouin@dal.ca
'''
# Import everything from Graphics
from graphics import *
from random import randint

def RandomColor():
	return color_rgb(randint(0,255), randint(0,255), randint(0,255))

def Replicant(x,y,height, radius):
	# Master circle
	c = Circle(Point(x,y), radius)

	relx = (x/600.)*255
	color = color_rgb(255-relx,randint(0,255),relx)
	c.setFill(color)
	c.draw(win)

	if height > 0:
		height -= 1
		Replicant(x-(radius/2),y,height,radius/2)
		Replicant(x+(radius/2),y,height,radius/2)


# Build a window
win = GraphWin('Test 1', 600, 600)

# Make a circle
Replicant(300,300,6,290)

# Wait to stop
win.getMouse()
win.close()
