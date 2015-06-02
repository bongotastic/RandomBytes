'''
	A dot, by you. - Python.
	cblouin@dal.ca

	Hackable: Experiment with colors, text, and the location of the elements. 
	You can also cange the color of the background window.
'''
# Import everything from Graphics
from graphics import *

# Build a window
win = GraphWin('Test 1', 600, 600)
win.setBackground('white')

# Repeat someting a number of times
for repeat in range (10):
	poly = Oval( Point(50 + (repeat*50) ,50), Point(100 + (repeat*50), 550) )
	poly.setFill('blue')
	poly.draw(win)

# Wait to stop
win.getMouse()
win.close()
