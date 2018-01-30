# sample 2
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

def secure(password):
	nums = set('0123456789')
	caps = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	foundNumber = False
	foundCaps = False

	for n in password:
		if (n in nums):
			foundNumber = True
		if (n in caps):
			foundCaps = True

	if foundNumber and foundCaps:
		return True
	else:
		return False

def getPassword():
	while True:
		password = raw_input('Enter Password : ')
		if secure(password):
			return password
		else:
			print("%s must contain at least one number and one capital letter" %(password))

def setupAccount():
	account = []
	username = raw_input ('Username : ')
	account.append(username)
	password = getPassword()
	account.append(password)
	name = raw_input('Name : ')
	account.append(name)
	address = raw_input('Address : ')
	account.append(address)
	dob = raw_input('Date of Birth [dd-mm-yyyy] : ')
	account.append(dob)
	gender = raw_input('Gender M/F : ')
	account.append(gender)

	interests = []
	moreInterests = True
	while moreInterests:
		interest = raw_input('Interests, empty string to quit : ')
		if interest == "":
			moreInterests = False
		else:
			interests.append(interest)

	account.append(interests)
	return account

def getSingleFilm():
	film = []
	name = raw_input('Film name : ')
	film.append(name)

	genres = []
	moreGenres  = True
	while moreGenres:
		genre = raw_input('Genre (terminate entries by hitting Enter on its own) : ')
		if genre == "":
			moreGenres = False
		else:
			genres.append(genre)
	film.append(genres)

	actors = []
	moreActors = True
	while moreActors:
		actor = raw_input('Actor (terminate entries by hitting Enter on its own) : ')
		if actor == "":
			moreActors = False
		else:
			actors.append(actor)
	film.append(actors)

	director = raw_input('Director : ')
	film.append(director)

	like = raw_input('Like (Y/N) : ')
	film.append(like)
	return film

def getNFilms(n):
	films = []
	for _ in range(n):
		film = getSingleFilm()
		films.append(film)
	return films

def createCustomer(n):
	customer = setupAccount()
	films = getNFilms(n)
	customer.append(films)
	return customer

def recommend(Customers, Films):
	while True:
		print ('1. Recommend on Genre')
		print ('2. Recommend on actors/actresses')
		print ('3. Recommend on Director')
		print ('4. Main menu')
		
		option = raw_input('Select an option : ')
		if option == '1':
			print('--- Matching on genre ---')
			matchCriteria(Customers, Films, GENRE)
		elif option == '2':
			print('--- Matching on actors/actresses ---')
			matchCriteria(Customers, Films, ACTOR)
		elif option == '3':
			print('--- Matching on director ---')
			matchCriteria(Customers, Films, DIRECTOR)
		elif option == '4':
			return
		else:
			print ('Not a valid choice - try again')


def mainMenu(Customers, Films):
	while True:
		print ('1. Enter new customer information')
		print ('2. Recommend films')
		print ('3. Logout')

		option = raw_input('Select an option : ')
		if option == '1':
			customer = createCustomer(2)
			Customers.append(customer)
		elif option == '2':
			recommend(Customers, Films)
		elif option == '3':
			return
		elif option == '0':
			print("--- Customers ---")
			print(Customers)
		else:
			print ('Not a valid choice - try again')

# main code starts here
Films = loadPickleFile('films.pkl')
Customers = loadPickleFile('customers.pkl')
mainMenu(Customers, Films)
