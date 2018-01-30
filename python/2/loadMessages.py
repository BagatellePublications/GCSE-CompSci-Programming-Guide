def loadMessages():
# start by trying to load our data file.
  try:
    f = open("messages.data", "r")

  except IOError as e:
    return None

  else:
    m = f.read().splitlines()
    f.close()
    return m

# program starts here
m = loadMessages()
print(m)
