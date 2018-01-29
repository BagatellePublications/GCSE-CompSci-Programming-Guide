def displayList(L):
    if L != []:
        for s in L:
            print (s)
    else:
        print("List is empty")

def enterNewStudentInformation(L):
    print ('-- enterNewStudentInformation --')

def searchForStudentByID(L):
    print ('-- searchForStudentByID --')

def reportMenu(L):
    print ('-- reportMenu --')

def mainMenu(L):
    while True:
        print ('1. Enter new student information')
        print ('2. Search by ID')
        print ('3. Report Menu')
        print ('4. Logout')

        option = input('Select an option : ')
        if option == '1':
            enterNewStudentInformation(L)
        elif option == '2':
            searchForStudentByID(L)
        elif option == '3':
            reportMenu(L)
        elif option == '4':
            return
        elif option == '0':
            displayList(L)
        else:
            print ('Not a valid choice - try again')

# main program starts here
StudentList = []
mainMenu(StudentList)
