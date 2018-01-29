import random
import csv

def loadObstacles(m):
# start by trying to load our data file.
  try:
    f = open("obstacles.csv", "r")

  except IOError as e:
    return []

  else:
    print(m[2])
    obstacles = []
    for line in csv.reader(f):
      obstacles.append(line)
    f.close()
    return obstacles

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

def throwDice(player, m):
  d1 = random.randint(1,6)
  d2 = random.randint(1,6)
  #d1 = int(input("First dice: "))
  #d2 = int(input("Second dice: "))

  if d1 == d2:
    score = -(d1+d2)
    print (m[7] %(player, str(d1), str(score)))
  else:
    score = d1+d2
    print (m[8] %(player, str(d1), str(d2), str(score)))
  return score

def checkForObstacles(position, player, obstacles, m):
	for obstacle in obstacles:
		if int(obstacle[0]) == position:
			print(m[9] %(player, str(position), obstacle[1]))
			return position + int(obstacle[1])
	return position

def turn(position, player, obstacles, m):
  position = position + throwDice(player, m)
  position = checkForObstacles(position, player, obstacles, m)
  if position < 1:
    position = 1
  return position

def winner(position):
  if position > 48:
    return True
  else:
    return False


# program starts here
# Players A and B both start in square 1
A = 1
B = 1

m = loadMessages()
print(m[0])
print(m[1])	# welcome message
obstacles = loadObstacles(m)
print(obstacles)


while True:
  A = turn(A, "A", obstacles, m)
  if winner(A):
    print (m[3] %str(A))
    break
  else:
    print (m[4] %str(A))
    B = turn(B, "B", obstacles, m)
    if winner(B):
      print (m[5] %str(B))
      break
    else:
      print (m[6] % str(B))
