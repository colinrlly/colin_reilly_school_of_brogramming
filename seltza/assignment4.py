import turtle

# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 4

s = turtle.getscreen()

t = turtle.Turtle()



circle_sides = 36
circle_side_len = 10
shaft_length = 400

#for i in range(4):
t.left(90)
for s in range(circle_sides):
    t.forward(circle_side_len)
    t.left(360/circle_sides)

for s in range(circle_sides):
    t.forward(circle_side_len)
    t.right(360/circle_sides)

for s in range(int(circle_sides/4)):
    t.forward(circle_side_len)
    t.left(360/circle_sides)

t.right(90)

t.forward(shaft_length)

for s in range(int(circle_sides/2)):
    t.forward(circle_side_len)
    t.right(360/circle_sides)

t.forward(shaft_length+10)

#for s in range(int(circle_sides/2)):
#    t.forward(circle_side_len)
#    t.right(360/circle_sides)

#    t.right(90)


turtle.done()
