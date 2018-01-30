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

# main program starts here
StudentList = loadStudentData()
report = report3(StudentList)
displayList(report)
