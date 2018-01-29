def displayList(L):
    if L != []:
        for s in L:
            print (s)
    else:
        print("List is empty")

def enterNewStudentInformation(L):
    s = []
    uniqueID = input("Unique ID: ")
    s.append(uniqueID)
    surname = input("Surname: ")
    s.append(surname)
    forename = input("Forename: ")
    s.append(forename)
    dob = input("Date of Birth [dd-mm-yyyy]: ")
    s.append(dob)
    address = input("Home address: ")
    s.append(address)
    phone = input("Phone number: ")
    s.append(phone)
    gender = input("Gender [M/F]: ")
    s.append(gender)
    group = input("Tutor group : ")
    s.append(group)
    s.append(str(uniqueID) + "@treeroad.sch.uk")

    L.append(s)

    return L

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
