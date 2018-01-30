def getColRowFor(n):
	row = (n-1) // 7
	if (row % 2) == 0:  # i.e. numbers increase from left to right
		col = (n-1) % 7
	else:               # numbers decrease from left to right
		col = (7 - (n%7)) % 7

	return col, row

def printNColRow():
  for n in range (1,50):
    col, row = getColRowFor(n)
    print (str(n) + ': (' + str(row) + ', ' + str(col) + ')')
        
# program begins here
printNColRow()
