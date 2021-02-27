import turtle

SHAFT_LENGTH = 100
BALL_SIZE = 200
BALL_GAP_SIZE = 20
SHAFT_TIP_EDGE_SIZE = 20
SHAFT_TIP_SIZE = BALL_SIZE + BALL_GAP_SIZE

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(3)

# Right testicle
t.right(90)
t.forward(BALL_SIZE)
t.right(90)
t.forward(BALL_SIZE)

# Center of balls
t.right(90)
t.forward(BALL_GAP_SIZE)
t.left(90)
t.forward(BALL_GAP_SIZE)
t.left(90)
t.forward(BALL_GAP_SIZE)
t.right(90)

# Left testicle
t.forward(BALL_SIZE)
t.right(90)
t.forward(BALL_SIZE)
t.right(90)

# Shaft
t.forward(BALL_SIZE*.75)
t.left(90)
t.forward(SHAFT_LENGTH)
t.left(90)
t.forward(SHAFT_TIP_EDGE_SIZE)
t.right(90)
t.forward(50)
t.right(90)
t.forward(BALL_SIZE)
t.right(90)
t.forward(50)
t.right(90)
t.forward(SHAFT_TIP_EDGE_SIZE)
t.left(90)
t.forward(SHAFT_LENGTH)
t.left(90)
t.forward(BALL_SIZE*.75)

turtle.done()
