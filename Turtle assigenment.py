#Mark Hendri
#Professor Eckert
#CS175L
#Turtle assigment

import math
import turtle

#Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -45
TEXT_Y = -35

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s/math.sqrt(2)
diameter = s + (2 * x)

#Initialize the turtle
turtle.speed(ANIMATION_SPEED)

#Move the turtle to the starting point.
turtle.penup()
turtle.goto(-diameter/2, -s/2)
turtle.pendown()

#Draw the octagon.
for i in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

#Display 'STOP'
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.write('STOP', align='center', font=('Arial', 16, 'bold'))

turtle.hideturtle()

#Keep the window open until it is clicked.
turtle.done()



