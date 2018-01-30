import random
import csv

def loadObstacles():
# start by trying to load our data file.
  try:
    f = open("obstacles.csv", "r")

  except IOError as e:
    return []

  else:
    print("Obstacles file opened successfully")
    obstacles = []
    for line in csv.reader(f):
      obstacles.append(line)
    f.close()
    return obstacles

def throwDice(player):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    #d1 = int(input("First dice: "))
    #d2 = int(input("Second dice: "))

    if d1 == d2:
        score = -(d1+d2)
        print (player + ': double ' + str(d1) + ': returns ' + str(score))
    else:
        score = d1+d2
        print (player +' ' +str(d1) + ',' +str(d2) +': returns ' +str(score))
    return score

def checkForObstacles(position, player, obstacles):
    for obstacle in obstacles:
        if int(obstacle[0]) == position:
            print (player +": obstacle @ " +str(position) +", value " + obstacle[1])
            return position + int(obstacle[1])
    return position

def turn(position, player, obstacles):
    position = position + throwDice(player)
    position = checkForObstacles(position, player, obstacles)
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

obstacles = loadObstacles()
print(obstacles)

while True:
    A = turn(A, "A", obstacles)
    if winner(A):
        print ('Player A scored ' + str(A) + ', Player A has won')
        break
    else:
        print ('Player A new position: ' + str(A))
        B = turn(B, "B", obstacles)
        if winner(B):
            print ('Player B scored ' + str(B) + ', Player B has won')
            break
        else:
            print ('Player B new position: ' + str(B))
