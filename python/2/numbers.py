import turtle

# grid origin lies at (10, 40)
OX = 10
OY = 40

# box has dimensions (30,40) to make it look square
BOX_X = 30
BOX_Y = 40

# turtle drawing speed
SUPERFAST = 0

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
    screen.setworldcoordinates(0, 0, OX + 8*BOX_X -20, OY + 8*BOX_Y - 20)
    turtle.mode("world")
    turtle.hideturtle()
    turtle.speed(SUPERFAST)

def drawGrid():
    turtle.color('black')
    turtle.pensize(2)
    jumpto(OX, OY)
    for i in range(0,8):
        line(OX, i*BOX_Y + OY, OX + 7*BOX_X, i*BOX_Y + OY)
        line(i*BOX_X + OX, OY, i*BOX_X + OX, 7*BOX_Y + OY)

def drawN(n, col, row):
    jumpto(OX + col*BOX_X+10, OY + row*BOX_Y+10)
    turtle.write(str(n), True, align="left", font = ("Arial", 28, "normal"))

def getColRowFor(n):
    row = (n-1) // 7
    if (row % 2) == 0:  # i.e. numbers increase from left to right
        col = (n-1) % 7
    else:               # numbers decrease from left to right
        col = 6 - ((n-1) % 7)

    return col, row

def drawNumbers():
    for n in range (1,50):
        col, row = getColRowFor(n)
        drawN(n, col, row)

def closeDown():
    turtle.done()


# program starts here
initialiseScreenAndTurtle()
drawGrid()
drawNumbers()
closeDown()
