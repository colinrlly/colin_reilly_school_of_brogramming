import turtle

# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 3

s = turtle.getscreen()

t = turtle.Turtle()

# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)

max_branch_length = 5


def build_tree(t, branch_length, shorten_by, angle):
    if branch_length > max_branch_length:
        t.forward(branch_length)
        new_length = branch_length  - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)

        t.right(angle*2)
        build_tree(t, new_length, shorten_by, angle)
        
        t.left(angle)
        t.backward(branch_length)


t.hideturtle()
t.setheading(90)
t.color('green')

build_tree(t, 50, 5, 30)
t.mainloop()

