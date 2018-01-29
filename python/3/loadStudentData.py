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

# main program starts here
StudentList = loadStudentData()
