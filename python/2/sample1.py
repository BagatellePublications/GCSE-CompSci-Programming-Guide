import os
import csv

MR_LEEMANS_USERNAME = 'pleeman'
MR_LEEMANS_PASSWORD = 'abcd1234'

def loginWasSuccessful():
    username = raw_input("Hello, please enter your username: ")
    if username == MR_LEEMANS_USERNAME:
        counter = 0
        while counter < 3:
            password = raw_input("Hello Mr. Leeman, please enter your password: ")
            if password == MR_LEEMANS_PASSWORD:
                return True
            else:
                counter = counter + 1

    return False

def displayList(L):
    if L != []:
        for s in L:
            print (s)
    else:
        print("List is empty")

def loadStudentData():
# start by trying to load our data file.
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

def logout(L):
    print ("Logging out ...")
    if L != []:
        if os.path.isfile("students.csv"):
            if os.path.isfile("students.backup"):
                os.remove("students.backup")
                print ("students backup file has been removed")

            os.rename("students.csv", "students.backup")
            print ("Students data file has been renamed to 'students.backup'")

        f = open("students.csv", "w")
        writer = csv.writer(f)
        writer.writerows(L)
        f.close()

        print ("Student data has been saved in file 'students.csv'")

    else:
        print ("No data to save")

def report1(L):
    report = []
    if L != []:
        for s in L:
            r = []
            r.append(s[1])
            r.append(s[0])
            report.append(r)

        report = sorted(report, key = lambda student: student[0])

    return report

def report2(L):
    boys = []
    girls = []

    if L != []:
        for s in L:
            r = []
            r.append(s[1])
            r.append(s[2])
            r.append(s[0])

            if s[6] in ['m','M']:
                boys.append(r)
            elif s[6] in ['f','F']:
                girls.append(r)
            else:
                print ("Missing gender for student with unique ID " + s[0])

        boys = sorted(boys, key = lambda student: student[0])
        girls = sorted(girls, key = lambda student: student[0])

    return boys, girls

def report3(L):
    report = []

    if L != None:
        for s in L:
            r = []
            r.append(s[2])
            r.append(s[1])

            for i in range(9):
                if (s[i] == ""):
                    r.append(str(i))

            report.append(r)

    return report

def reportMenu(L):
	while True:
		print ('1. Create report to match surname to unique ID')
		print ('2. Create report to identify girls and boys')
		print ('3. Create report to identify missing information')
		print ('4. Return to main menu')

		option = raw_input('Select an option : ')
		if option == '1':
			report = report1(L)
			displayList(report)
		elif option == '2':
			boys, girls = report2(L)
			print('Boys')
			displayList(boys)
			print('Girls')
			displayList(girls)
		elif option == '3':
			report = report3(L)
			print('Missing data')
			displayList(report)
		elif option == '4':
			return
		else:
			print ('Not a valid choice - try again')

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

def enterNewStudentInformation(L):
    s = []
    uniqueID = raw_input("Unique ID: ")
    s.append(uniqueID)
    surname = raw_input("Surname: ")
    s.append(surname)
    forename = raw_input("Forename: ")
    s.append(forename)
    dob = raw_input("Date of Birth [dd-mm-yyyy]: ")
    s.append(dob)
    address = raw_input("Home address: ")
    s.append(address)
    phone = raw_input("Phone number: ")
    s.append(phone)
    gender = raw_input("Gender [M/F]: ")
    s.append(gender)
    group = raw_input("Tutor group : ")
    s.append(group)
    s.append(str(uniqueID) + "@treeroad.sch.uk")

    L.append(s)
    return L

def mainMenu(L):
    while True:
        print ('1. Enter new student information')
        print ('2. Search by ID')
        print ('3. Report Menu')
        print ('4. Logout')

        option = raw_input('Select an option : ')
        if option == '1':
            L = enterNewStudentInformation(L)
        elif option == '2':
            searchForStudentByID(L)
        elif option == '3':
            reportMenu(L)
        elif option == '4':
            return L
        elif option == '0':
            displayList(L)
        else:
            print ('Not a valid choice - try again')

# main program starts here
if loginWasSuccessful():
    StudentList = loadStudentData()
    StudentList = mainMenu(StudentList)
    logout(StudentList)
else:
    print('Apologies, but login has failed - goodbye')
