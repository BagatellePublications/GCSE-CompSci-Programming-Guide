import random
import turtle
import csv

# grid origin lies at (10, 40)
OX = 10
OY = 40

# messages go to (10,10)
MSG_X = 10
MSG_Y = 10

# box has dimensions (30,40) to make it look square
BOX_X = 30
BOX_Y = 40

# turtle speed
NORMAL = 8
SLOW = 3
FAST = 5
SUPERFAST = 0

# real dice or SIMULATION
# change this flag to False to produce a real dice version of this program
SIMULATION = True

#-------------------------------------
# Turtle graphics code
#-------------------------------------
def jumpto(x,y):
	turtle.penup()
	turtle.goto(x,y)

#-------------------------------------
def line(x1, y1, x2, y2):
	jumpto(x1, y1)
	turtle.pendown()
	turtle.goto(x2, y2)
	turtle.penup()

#-------------------------------------
def clearMessageLine():
	jumpto(MSG_X-2, MSG_Y-4)
	turtle.setheading(90)
	turtle.fillcolor("white")
	turtle.begin_fill()
	for _ in range(2):
		turtle.forward(14)
		turtle.right(90)
		turtle.forward(300)
		turtle.right(90)
		turtle.end_fill()

#-------------------------------------
def message(msg):
	clearMessageLine()
	jumpto(MSG_X, MSG_Y)
	turtle.pencolor("black")
	turtle.write(msg, True, align="left", font = ("Arial", 16, "normal"))

#-------------------------------------
def drawGrid():
	turtle.color('black')
	turtle.pensize(2)
	jumpto(OX, OY)
	for i in range(0,8):
		line(OX, i*BOX_Y + OY, OX + 7*BOX_X, i*BOX_Y + OY)
		line(i*BOX_X + OX, OY, i*BOX_X + OX, 7*BOX_Y + OY)

#-------------------------------------
def initialiseScreenAndTurtle():
	screen = turtle.Screen()
	screen.reset
	screen.setworldcoordinates(0, 0, OX + 8*BOX_X - 20, OY + 8*BOX_Y - 20)
	turtle.title("Sample 3 - Game of dice")
	turtle.mode("world")
	turtle.hideturtle()
	turtle.speed(SUPERFAST)
	
#-------------------------------------
def drawN(n, col, row):
	jumpto(OX + col*BOX_X+10, OY + row*BOX_Y+10)
	turtle.write(str(n), True, align="left", font = ("Arial", 28, "normal"))

#-------------------------------------
def getColRowFor(n):
	row = (n-1) // 7
	if (row % 2) == 0:  # i.e. numbers increase from left to right
		col = (n-1) % 7
	else:               # numbers decrease from left to right
		col = 6 - ((n-1) % 7)

	return col, row

#-------------------------------------
def drawNumbers():
	for n in range (1,50):
		col, row = getColRowFor(n)
		drawN(n, col, row)

#-------------------------------------
def drawPlayerAt(col, row, Player, stampID):
	turtle.clearstamp(stampID)
	if Player == "A":
		jumpto(OX + col*BOX_X+5, OY + row*BOX_Y + BOX_Y - 5)
		turtle.color("red")
		return turtle.stamp()
	else:
		jumpto(OX + col*BOX_X+BOX_X-5, OY + row*BOX_Y + BOX_Y - 5)
		turtle.color("blue")
		return turtle.stamp()

#-------------------------------------
def showPlayerOnGrid(position, Player, stampID):
	col, row = getColRowFor(position)
	return drawPlayerAt(col, row, Player, stampID)

#-------------------------------------
def closeDown():
	turtle.done()

#-------------------------------------
# Gameplay code
#-------------------------------------
def loadObstacles(m):
# start by trying to load our data file.
  try:
    f = open("obstacles.csv", "r")

  except IOError as e:
    return []

  else:
    message(m[2])
    obstacles = []
    for line in csv.reader(f):
      obstacles.append(line)
    f.close()
    return obstacles

#-------------------------------------
def loadMessages():
# start by trying to load our data file.
	try:
		f = open("messages.data", "r")

	except IOError as e:
		return []

	else:
		m = f.read().splitlines()
		f.close()
		return m

#-------------------------------------
def throwDice(player, m):
	if (SIMULATION):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
	else:
		d1 = int(turtle.numinput(m[7] + Player, m[17], minval=1, maxval=6))
		d2 = int(turtle.numinput(m[7] + Player, m[18], minval=1, maxval=6))

	if d1 == d2:
		score = -(d1+d2)
		message (m[7] %(player, str(d1), str(score)))
	else:
		score = d1+d2
		message (m[8] %(player, str(d1), str(d2), str(score)))
	return score

#-------------------------------------	
def checkForObstacles(position, player, obstacles, m):
	for obstacle in obstacles:
		if int(obstacle[0]) == position:
			message(m[9] %(player, str(position), obstacle[1]))
			return position + int(obstacle[1])
	return position

#-------------------------------------
def turn(position, player, obstacles, m):
  position = position + throwDice(player, m)
  position = checkForObstacles(position, player, obstacles, m)
  if position < 1:
    position = 1
  return position

#-------------------------------------
def winner(position):
  if position > 48:
    return True
  else:
    return False

#---------------------------------
# program starts here
initialiseScreenAndTurtle()
drawGrid()
drawNumbers()

# both players start on the first square of the grid
A = 1
B = 1

# having drawn the grid quickly we can slow down
turtle.speed(NORMAL)

# load messages and obstacles
m = loadMessages()
obstacles = loadObstacles(m)

# keep track of the last turtle position for each players
# so that we can delete in before showing the new position
stampA = None
stampB = None

# quick welcome message
message(m[1])

while True:
	if (SIMULATION):
		turtle.speed(FAST)

	A = turn(A, "A", obstacles, m)
	if winner(A):
		message (m[3] %str(A))
		stampA = showPlayerOnGrid(49, "A", stampA)
		break
	else:
		message (m[4] %str(A))
		stampA = showPlayerOnGrid(A, "A", stampA)

	if (SIMULATION):
		turtle.speed(NORMAL)
		turtle.speed(FAST)

	B = turn(B, "B", obstacles, m)
	if winner(B):
		message (m[5] %str(B))
		stampB = showPlayerOnGrid(49, "B", stampB)
		break
	else:
		message (m[6] %str(B))
		stampB = showPlayerOnGrid(B, "B", stampB)

	if (SIMULATION):
		turtle.speed(NORMAL)
	
closeDown()
