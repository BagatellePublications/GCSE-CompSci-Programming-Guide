import turtle

SLOW = 1


def jumpto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    
def initialiseScreenAndTurtle():
    screen = turtle.Screen()
    screen.reset
    screen.setworldcoordinates(0, 0, 300, 300)
    turtle.title("A square")
    turtle.speed(SLOW)

def closeDown():
    turtle.done()

def square(side):
    turtle.pencolor("red")
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)

    
# program starts here
initialiseScreenAndTurtle()
jumpto(100,200)
square(100)
closeDown()
