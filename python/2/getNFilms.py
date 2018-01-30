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

# main code starts here
Films = getNFilms(2)
print (Films)
