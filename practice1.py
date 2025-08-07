from turtle import *

#makes a donut, but Python isn't edible.
def donut():
    circle(30)
    left(90)
    left(180)
    color('white')
    forward(60)
    color('black')
    left(90)
    circle(90)

donut()

#makes a square.
def quad():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

quad()


#makes a triangle.
def threeshape():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

threeshape()