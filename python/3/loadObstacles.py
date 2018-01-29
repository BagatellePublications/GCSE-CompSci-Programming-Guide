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

# program starts here
L = loadObstacles()
print(L)
