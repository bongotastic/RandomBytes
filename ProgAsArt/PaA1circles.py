'''
	A dot, by you. - Python.
	cblouin@dal.ca

	Hackable: Experiment with colors, text, and the location of the elements. 
	You can also cange the color of the background window.
'''
# Import everything from Graphics
from graphics import *

# Build a window
win = GraphWin('A Dot', 600, 600)
win.setBackground('white')

# Draw one circle
poly = Circle( Point( 300, 300 ), 200 )
poly.setFill( 'red' )
poly.draw(win)

# Add some text
mytext = Text( Point(450, 520), 'by Random Bytes' )
mytext.setFill('red')
mytext.setSize( 30 )
mytext.draw(win)

# Wait to stop
win.getMouse()
win.close()
