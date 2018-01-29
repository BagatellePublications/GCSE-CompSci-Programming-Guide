import random

def throwDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if d1 == d2:
        score = -(d1+d2)
    else:
        score = d1+d2

    return score

# code starts here
for x in range(6):
	print (throwDice())
