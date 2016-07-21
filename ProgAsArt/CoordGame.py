'''
   Coordinate guessing game
'''

# Import the graphics library
from graphics import *

# Import the random function randint
from random import randint

# Functions 
def Feedback( tgt, guess ):
	# Draw tgt
	ctgt = Circle( tgt, 5 )
	ctgt.setFill('red')
	ctgt.draw(win)

	# Draw error
	eline = Line(tgt, guess)
	eline.draw(win)

	# Coords
	ccds = Text( Point( tgt.getX(), tgt.getY()+15 ), '(%d,%d)'%(tgt.getX(), tgt.getY()) )
	ccds.draw(win)


# Main game logic

# A window
width = 600
height = 600
win = GraphWin('Coordinate Guessing Game', width, height)

score = 0

# Labels
label_x = Text(Point(30,20), 'x=%d'%(0))
label_x.setSize(12)
label_x.draw(win)
label_y = Text(Point(90,20), 'y=%d'%(0))
label_y.setSize(12)
label_y.draw(win)

label_score = Text( Point(width-60, height-20), 'Error=%d'%(score) )
label_score.setSize(12)
label_score.draw(win)

for iteration in range(6):
	# Pick a coordinate on the surface
	x = randint(0,width)
	y = randint(0, height)

	# Write it
	label_x.setText('x=%d'%(x))
	label_y.setText('y=%d'%(y))

	# Wait for input
	guess = win.getMouse() 

	# Evaluate error
	temp_error = ((guess.getX()-x)**2 + (guess.getY()-y)**2)**0.5
	score += temp_error
	label_score.setText('Error=%d'%(score))

	# Draw feedback
	Feedback( Point(x,y), guess )


# Achievement
name = 'San'
if score < 1000:
	name = 'Sensei'
if score < 300:
	name = 'Ninja'
if score < 120:
	name = 'Grand Master'


# Close the window
final = Text( Point(width/2, height/2) ,'Score=%d! you are a %s'%(score, name))
final.setSize(20)
final.draw(win)
label_x.undraw()
label_y.undraw()
win.getMouse() 
win.close()
