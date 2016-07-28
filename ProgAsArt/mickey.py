''' 
    Interactive graphics setup.
    
    Just load this file into IDLE, run it (F5 on Windows), and access the Python console.
'''
# Import the graphics library so that you may use its object in the console.
from graphics import *

# Create a window
mywindow = GraphWin(title="My Mickey head!", width=600, height=600 )
mywindow.setBackground('white')

# Create three circles
head = Circle( Point(50,50), 40)
head.setFill('pink')
head.setOutline('black')
head.setWidth(1)

head.draw(mywindow)


ear1 = Circle( Point(150,50), 30)
ear1.setFill('pink')
ear1.setOutline('black')
ear1.setWidth(1)

ear1.draw(mywindow)


ear2 = Circle( Point(250, 50), 20)
ear2.setFill('pink')
ear2.setOutline('black')
ear2.setWidth(1)
ear2.draw(mywindow)

mywindow.getMouse()
mywindow.close()