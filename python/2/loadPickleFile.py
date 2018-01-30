import pickle

def displayList(L):
	if L != []:
		for s in L:
			print (s)
	else:
		print("List is empty")

def loadPickleFile(filename):
	try:
		f = open(filename, 'rb')

	except IOError as e:
		print("Failed to open %s" %filename)
		return []

	else:
		content = pickle.load(f)
		f.close()
		return content

# main code starts here
print ("--- Films ---")
Films = loadPickleFile('films.pkl')
displayList(Films)

print ("--- Customers ---")
Customers = loadPickleFile('customers.pkl')
displayList(Customers)
