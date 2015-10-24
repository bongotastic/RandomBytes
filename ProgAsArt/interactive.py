''' 
    Interactive graphics setup.
    
    Just load this file into IDLE, run it (F5 on Windows), and access the Python console.
'''
# Import the graphics library so that you may use its object in the console.
from graphics import *

win = GraphWin('This is awesome', 500, 500)
win.setBackground('blue')

poly = Circle( Point(250, 250), 175)
poly.setFill( 'orange' )
poly.draw(win)

mytext = Text( Point(250, 250), "Hello world")
mytext.setFill('black')
mytext.setSize(30)
mytext.draw(win)

for i in range(10):
    mypoint = win.getMouse()
    newcircle = Circle( mypoint, 25)
    newcircle.setFill('red')
    newcircle.draw(win)

win.getMouse()
win.close()

