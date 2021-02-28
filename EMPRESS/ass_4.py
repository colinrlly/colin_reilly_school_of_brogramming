import turtle
import math

SHAFT_LENGTH = 200
BALLR = 100
BALLR_BIT = BALLR*0.75


s = turtle.getscreen()
t = turtle.Turtle()

t.speed(10)

t.circle(BALLR)
t.forward(BALLR*2)
t.circle(BALLR)
t.backward(BALLR*1.5)
t.left(90)
t.forward(SHAFT_LENGTH)
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.right(45)
t.forward((math.sqrt((BALLR_BIT)*(BALLR_BIT)+(BALLR_BIT)*(BALLR_BIT)))-5)
t.right(45)
t.forward(10)
t.right(45)
t.forward(50)
t.right(45)
t.forward(10)
t.right(90)
t.forward(10)
t.left(90)
t.forward(SHAFT_LENGTH)

turtle.done()
