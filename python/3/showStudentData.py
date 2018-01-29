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

# main program starts here
studentList = loadStudentData()
displayList(studentList)
