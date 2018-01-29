def getSingleFilm():
	film = []
	name = input('Film name : ')
	film.append(name)

	genres = []
	moreGenres  = True
	while moreGenres:
		genre = input('Genre (terminate entries by hitting Enter on its own) : ')
		if genre == "":
			moreGenres = False
		else:
			genres.append(genre)
	film.append(genres)

	actors = []
	moreActors = True
	while moreActors:
		actor = input('Actor (terminate entries by hitting Enter on its own) : ')
		if actor == "":
			moreActors = False
		else:
			actors.append(actor)
	film.append(actors)

	director = input('Director : ')
	film.append(director)

	like = input('Like (Y/N) : ')
	film.append(like)
	return film

# main code starts here
Film = getSingleFilm()
print (Film)
