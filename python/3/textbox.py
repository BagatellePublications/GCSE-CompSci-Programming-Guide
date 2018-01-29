# messages start at (10,10)
MSG_X = 10
MSG_Y = 10

#-------------------------------------
def clearMessageLine():
    jumpto(MSG_X-2, MSG_Y)
    turtle.setheading(90)
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(280)
        turtle.right(90)
    turtle.end_fill()

#-------------------------------------
def message(msg):
    clearMessageLine()
    jumpto(MSG_X, MSG_Y)
    turtle.pencolor("black")
    turtle.write(msg, True, align="left", font = ("Arial", 16, "normal"))
