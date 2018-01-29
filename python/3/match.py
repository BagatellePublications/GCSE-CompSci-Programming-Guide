import pickle

# field index
FILM_NAME = 0
CUSTOMER_NAME = 2

GENRE = 1
ACTOR = 2
DIRECTOR = 3
LIKE = 4
FILMS = 7
NUMBER_OF_FILMS_WANTED = 4

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
		
def matchEachCustomer(customer, films, criteria):
	if criteria == DIRECTOR:
		any_in = lambda a,b: (a == b)
	else:
		any_in = lambda a,b: any(i in a for i in b)
		
	watched = []
	for film in customer[FILMS]:
		watched.append(film[FILM_NAME])
		
	print(str(customer[CUSTOMER_NAME]) + " has watched " + str(watched))
	
	recommended = []
	counter = 0		
	for film in customer[FILMS]:
		if film[LIKE] == 'Y':
			for f in films:
				if any_in(film[criteria], f[criteria]):
					if not f[FILM_NAME] in watched:
						if not f[FILM_NAME] in recommended:
							recommended.append(f[FILM_NAME])
							counter = counter + 1
							if counter > NUMBER_OF_FILMS_WANTED:
								return recommended
	return recommended


def matchCriteria(customers, films, criteria):
	for customer in customers:
		L = matchEachCustomer(customer, films, criteria)
		print ('Recommended films for ' + customer[CUSTOMER_NAME])
		print (L)

# main code starts here
Films = loadPickleFile('films.pkl')
Customers = loadPickleFile('customers.pkl')

print('--- Matching on genre ---')
matchCriteria(Customers, Films, GENRE)
print('--- Matching on actors ---')
matchCriteria(Customers, Films, ACTOR)
print('--- Matching on director ---')
matchCriteria(Customers, Films, DIRECTOR)
