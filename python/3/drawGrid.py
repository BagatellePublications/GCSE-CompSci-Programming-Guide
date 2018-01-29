import turtle

# grid origin lies at (10, 40)
OX = 10
OY = 40

# each cell (box) has dimensions (30,40) to make it look square
BOX_X = 30
BOX_Y = 40

#-------------------------------------
# Turtle graphics code
#-------------------------------------
def jumpto(x,y):
    turtle.penup()
    turtle.goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

def initialiseScreenAndTurtle():
    screen = turtle.Screen()
    screen.reset
    screen.setworldcoordinates(0, 0, OX + 8*BOX_X - 20, OY + 8*BOX_Y - 20)
    turtle.mode("world")
    turtle.speed(3)

def drawGrid():
    turtle.color('black')
    turtle.pensize(2)
    jumpto(OX, OY)
    for i in range(0,8):
        line(OX, i*BOX_Y + OY, OX + 7*BOX_X, i*BOX_Y + OY)
        line(i*BOX_X + OX, OY, i*BOX_X + OX, 7*BOX_Y + OY)

def closeDown():
    turtle.done()


# program starts here
initialiseScreenAndTurtle()
drawGrid()
closeDown()
