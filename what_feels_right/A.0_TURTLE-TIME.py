# v1.0
import turtle

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
STARTING_DIRECTION = EAST

SHAFT_HEIGHT = 300

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(1)
currentDirection = STARTING_DIRECTION


def rotateToDirection(targetDirection):
    global currentDirection
    if targetDirection == currentDirection:
        return

    rotations = currentDirection - targetDirection
    # 1 - 0 = 1 // E -> N >> Rotate Left 90
    # 3 - 2 = 1 // W -> S >> Rotate Left 90
    # 2 - 3 = -1 // S -> W >> Rotate Left -90
    # 3 - 0 = 3 // W -> N >> Rotate Left 270
    t.left(rotations * 90)
    currentDirection = targetDirection


def move(targetDirection, distance):
    if distance == 0:
        return

    rotateToDirection(targetDirection)
    t.forward(distance)


move(EAST, 20)
move(SOUTH, 50)
move(EAST, 100)
move(NORTH, 100)
move(WEST, 110)
move(SOUTH, 10)
move(NORTH, 10)
move(EAST, 60)
move(NORTH, SHAFT_HEIGHT)
move(WEST, 60)

move(SOUTH, 10)
move(NORTH, 10)

move(WEST, 60)
move(NORTH, -SHAFT_HEIGHT)
move(EAST, 60)
move(WEST, 110)
move(NORTH, -100)
move(EAST, 100)
move(SOUTH, -50)
move(EAST, 20)

# TODO:
# - Improve efficiency of rotation/time
# - Integrate symmetrical turtle tech via looping and sequence caching
# - Configurable SHAFT_WIDTH
# - Configurable BALL_SPACING
# - Bevel that turtle!
# - Configurable per-component beveling

turtle.done()
