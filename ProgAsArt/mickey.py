'''
    Test art - Python.
    cblouin@dal.ca
'''
# Import everything from Graphics
from graphics import *
from random import randint

# Create a window
win = GraphWin('Mickey Mouse', 600, 600)

# Draw a head
head = Circle(Point(300, 400), 200)
head.setFill('black')
head.draw(win)

# Draw the ears
ears_y = 160
ears_sep = 150

# Left ear
l_ear = Circle(Point(300 - ears_sep, ears_y), 100)
l_ear.setFill('black')
l_ear.draw(win)

# right ear
r_ear = Circle(Point(300 + ears_sep, ears_y), 100)
r_ear.setFill('black')
r_ear.draw(win)

# Wait to stop
win.getMouse()
win.close()
