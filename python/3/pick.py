import pickle

films = [["Avatar",["sci-fi","action"],["Sam Worthington","Sigourney Weaver","Zoe Saldana"],"James Cameron"],
["Guardians of the Galaxy",["sci-fi","comedy"],["Chris Pratt","James Gunn","Vin Diesel","Zoe Saldana"],"James Gunn"],
["Pirates of the Caribbean:The curse of the Black Pearl",["action","comedy"],["Johnny Depp","Orlando Bloom","Keira Knoghtley"],"Gore Verbinski"],
["Tootsie",["comedy"],["Dustin Hoffman","Jessica Lange","Bill Murray"],"Sydney Pollack"],
["The Godfather",["drama"],["Marlon Brando","Al Pacino","James Caan"],"Francis Ford Coppola"],
["A Woman Under the Influence",["drama"],["Gena Rowlans","Peter Falk","Fred Draper"],"John Cassavetes"],
["Cinema Paradiso",["romantic"],["Philippe Noiret","Enzo Cannavale","Antonella Attili"],"Giuseppe Tornatore"],
["To Kill a Mockingbird",["drama"],["Gregory Peck","John Megna","Frank Overton"],"Robert Mulligan"],
["The Godfather: Part II",["drama"],["Al Pacino","Robert De Niro","Robert Duvall"],"Francis Ford Coppola"],
["Annie Hall",["comedy","romance"],["Woody Allen","Diane Keaton"],"Woody Allen"],
["Boogie Nights",["comedy","drama"],["Mark Wahlberg","Julianne Moore","Burt Reynolds"],"Paul Thomas Anderson"],
["Taxi Driver",["drama"],["Robert De Niro","Jodie Foster","Cybill Shepherd"],"Martin Scorsese"],
["Dog Day Afternoon",["drama"],["Al Pacino","John Cazale","Penelope Allen"],"Sidney Lumet"],
["Goodfellas",["drama"],["Robert De Niro","Ray Liotta","Joe Pesci"],"Martin Scorsese"],
["Withnail and I",["black comedy","indie"],["Richard E Grant","Paul McGann","Richard Griffiths"],"Bruce Robinson"],
["Kes",["drama"],["David Bradley","Brian Glover","Freddie Fletcher"],"Ken Loach"],
["The Wizard of Oz",["musical","fantasy","family"],["Judy Garland","Frank Morgan","Ray Bolger"],"Victor Fleming"],
["On the Waterfront",["drama"],["Marlon Brando","Karl Madden","Lee J Cobb"],"Elia Kazan"],
["The Shining",["horror"],["Jack Nicholson","Shelley Duval","Danny Lloyd"],"Stanley Kubrick"],
["Pulp Fiction",["thriller","black comedy","comedy","drama"],["John Travolta","Uma Thurman","Samuel L Jackson"],"Quentin Tarantino"],
["Gladiator",["action","drama"],["Russell Crowe","Joaquin Phoenix","Connie Nielsen"],"Ridley Scott"],
["Jaws",["action","thriller","drama"],["Roy Scheider","Robert Shaw","Richard Dreyfuss"],"Steven Spielberg"],
["Raging Bull",["drama","sports"],["Robert De Niro","Cathy Moriarty","Joe Pesci"],"Martin Scorcese"],
["Who's afraid of Virginia Woolf",["black comedy","drama"],["Elizabeth Taylor","Richard Burton","George Segal"],"Mike Nichols"],
["Some Like It Hot",["comedy"],["Marilyn Monroe","Tony Curtis","Jack Lemmon"],"Billy Wilder"],
["Fargo",["black comedy","drama"],["Frances McDormand","Steve Buscemi","William H Macy"],"Joel Coen"],
["The Night of The Hunter",["drama","thriller"],["Robert Mitchum","Shelley Wintera","Billy Chapin"],"Charles Laughton"],
["Rosemary's Baby",["horror"],["Mia Farrow","John Cassavetes","Ruth Gordon"],"Roman Polanski"],
["Chinatown",["thriller","drama"],["Jack Nicholson","Faye Dunaway","John Huston"],"Roman Polanski"],
["The Apartment",["comedy"],["Jack Lemmon","Shirley MacLaine","Fred MacMurray"],"Billy Wilder"]]

customers = [
["pwilliams","Password1","Peter Williams","26 High Street, Kensington, SW10 3ET","14-01-1993'","M",["films","tv","music"],
 [["Avatar",["sci-fi","action"],["Sam Worthington","Sigourney Weaver","Zoe Saldana"],"James Cameron","Y"],
  ["Guardians of the Galaxy",["sci-fi","comedy"],["Chris Pratt","James Gunn","Vin Diesel","Zoe Saldana"],"James Gunn","Y"],
  ["Fargo",["black comedy","drama"],["Frances McDormand","Steve Buscemi","William H Macy"],"Joel Coen","N"]
 ]],
["athos","P576swwd","Tom Sawyer","11 Trim Street, Kensington, SW10 2TY","15-12-1987","M",["movies","running","squash"],
 [["Taxi Driver",["drama"],["Robert De Niro","Jodie Foster","Cybill Shepherd"],"Martin Scorsese","Y"],
  ["The Wizard of Oz",["musical","fantasy","family"],["Judy Garland","Frank Morgan","Ray Bolger"],"Victor Fleming","N"],
  ["Some Like It Hot",["comedy"],["Marilyn Monroe","Tony Curtis","Jack Lemmon"],"Billy Wilder","N"]
 ]]
]

def display(L):
  if L != None:
    for s in L:
      print (s)
  else:
    print("No data found")


# program starts here
print ("---------------------------------------------------")
display(films)
print ("---------------------------------------------------")
display(customers)

output = open('films.pkl', 'wb')
pickle.dump(films, output, -1)
output.close()

output = open('customers.pkl', 'wb')
pickle.dump(customers, output, -1)
output.close()

fin = open('films.pkl', 'rb')
films1 = pickle.load(fin)
fin.close()

fin = open('customers.pkl', 'rb')
customers1 = pickle.load(fin)
fin.close()

print ("---------------------------------------------------")
display(films1)
print ("---------------------------------------------------")
display(customers1)
print ("---------------------------------------------------")
