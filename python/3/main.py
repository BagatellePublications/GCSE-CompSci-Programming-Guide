from random import *

def throwDice(player):
    d1 = randint(1,6)
    d2 = randint(1,6)
    #d1 = int(input("First dice: "))
    #d2 = int(input("Second dice: "))

    if d1 == d2:
        score = -(d1+d2)
        print (player + ': double ' + str(d1) + ': returns ' + str(score))
    else:
        score = d1+d2
        print (player +' ' +str(d1) + ',' +str(d2) +': returns ' +str(score))
    return score


def turn(position, player):
    position = position + throwDice(player)
    if position < 1:
        position = 1
    return position


def winner(position):
    if position > 48:
        return True
    else:
        return False


# program starts here
# Players A and B both start in square 1
A = 1
B = 1

while True:
    A = turn(A, "A")
    if winner(A):
        print ('Player A scored ' + str(A) + ', Player A has won')
        break
    else:
        print ('Player A new position: ' + str(A))
        B = turn(B, "B")
        if winner(B):
            print ('Player B scored ' + str(B) + ', Player B has won')
            break
        else:
            print ('Player B new position: ' + str(B))
