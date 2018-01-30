import csv

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

# main program starts here
StudentList = loadStudentData()
boys, girls = report2(StudentList)
print("Boys")
displayList(boys)
print("Girls")
displayList(girls)
