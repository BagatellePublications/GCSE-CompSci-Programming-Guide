import os
import csv

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
                print ("students backup file has been deleted")

            os.rename("students.csv", "students.backup")
            print ("Students data file has been renamed to 'students.backup'")

        f = open("students.csv", "w")
        writer = csv.writer(f)
        writer.writerows(L)
        f.close()

        print ("Student data has been saved successfully in 'students.csv'")

    else:
        print ("No data to save")

# main program starts here
StudentList = loadStudentData()
logout(StudentList)
