import csv

def loadStudentData():
    try:
        f = open("students.csv", "r")

    except IOError as e:
        print("Failed to open data file")
        return []

    else:
        print("Students data file opened successfully")
        students = []
        for line in csv.reader(f):
          students.append(line)
        f.close()
        return students

def displayList(L):
    if L != []:
        for s in L:
            print (s)
    else:
        print("List is empty")

def enterNewStudentInformation(L):
    print ('-- enterNewStudentInformation --')

def searchForStudentByID(L):
    if L != []:
        uniqueID = int(raw_input("Please enter a unique ID: "))
        for s in L:
            if int(s[0]) == uniqueID:
                print ("Found " + str(s))
                return

        # if we've tried every student in StudentList
        print("Sorry, couldn't find a match")
    else:
        print("No student data found")

def reportMenu(L):
    print ('-- reportMenu --')

def mainMenu(L):
    while True:
        print ('1. Enter new student information')
        print ('2. Search by ID')
        print ('3. Report Menu')
        print ('4. Logout')

        option = raw_input('Select an option : ')
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
StudentList = loadStudentData()
mainMenu(StudentList)
