import pickle

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
		
def matchEachCustomer(customer, films):
	any_in = lambda a,b: any(i in a for i in b)
	recommended = []
	counter = 0
	for film in customer[7]:
		if film[4] == 'Y':
			genres = film[1]
			for f in films:
				if any_in(genres, f[1]):
					recommended.append(f[0])
					counter = counter + 1
					if counter > 4:
						return recommended
	return recommended


def matchGenre(customers, films):
	for customer in customers:
		L = matchEachCustomer(customer, films)
		print ('Recommended films for ' + customer[2])
		print (L)


# main code starts here
Films = loadPickleFile('films.pkl')
Customers = loadPickleFile('customers.pkl')
matchGenre(Customers, Films)
