import turtle
import math

HARD_LENGTH = 100
SOFT_LENGTH = 20

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(1)

t.right(45)
t.forward(30)
t.right(45)
t.forward(SOFT_LENGTH)
t.right(90)
t.back(20)
t.circle(30)
t.forward(90)
t.circle(30)
t.backward(10)
t.right(90)
# t.backward(30)
# t.right(90)
# t.backward(30)
# t.right(90)
# t.backward(90)
# t.right(90)
# t.backward(30)
# t.right(90)
# t.backward(30)
# t.right(90)
t.forward(SOFT_LENGTH)
t.right(45)
t.forward(30)
t.right(45)
t.forward(20)

turtle.done()
