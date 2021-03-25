import turtle as sköldpadda

def shaft(length: int, girth: int):
    sköldpadda.home()
    sköldpadda.circle(girth, 90)
    sköldpadda.right(90)
    sköldpadda.forward(length)
    sköldpadda.circle(-1 * girth, 180)
    sköldpadda.forward(length)
    sköldpadda.right(90)
    sköldpadda.circle(girth, 90)

def balls(r: int):
    sköldpadda.home()
    sköldpadda.circle(r)
    sköldpadda.left(180)
    sköldpadda.circle(r)

length = 100
ball_size = 30

balls(ball_size)
shaft(length, ball_size)

sköldpadda.done()
