from classes import info, courses
import json


def get_operation():
    global operation
    operation = int(
        input(
            "Enter you considered operation. [1]>Add Student, [2]>Search Student: "
        ))
    if operation == 1 or operation == 2:
        pass
    else:
        get_operation()


get_operation()

if operation == 1:
    #get info
    name = input("Enter Student's name: ")
    age = input("Enter Student's age: ")
    nationalid = input("Enter Student's NationalID: ")
    studentid = input("Enter Sudent's StudentID: ")
    edu = input("Enter Student's Edu year: ")
    student_ginfo = info(name, age, nationalid, studentid, edu)
    #get grades
    mathgrd = input("Enter Student's math grade: ")
    phisicgrd = input("Enter Student's phisic grade: ")
    historygrd = input("Enter Student's history grade: ")
    csgrd = input("Enter Student's computer science grade: ")
    student_cinfo = courses(mathgrd, phisicgrd, historygrd, csgrd)
    #merge informations
    all_info = {}
    all_info.update(student_ginfo.infos())
    all_info.update(student_cinfo.infos())
    #make file and save data
    try:
        user_file = open(
            "/Volumes/Files/Projects/Python-oop-database/data/database.txt",
            "w")
        user_file.write(json.dumps(all_info))
        user_file.close()
        print("Student added successfuly!")
    except:
        print("Couldn't add student")
else:
    #search person
    studentid = input("Enter the StudentID to show info: ")
    try:
        database = open(
            "/Volumes/Files/Projects/Python-oop-database/data/database.txt",
            "r+")
        all_students = database.readlines()
        for std in range(len(all_students)):
            student = json.loads(all_students[std])
            if student["StudentID"] == studentid:
                report = {
                    "name: ": student["name"],
                    "math grade: ": student["math grade"],
                    "phisic grade: ": student["phisics grade"],
                    "history grade: ": student["history grade"],
                    "computer science grade: ":
                    student["computer science grade"]
                }

        student_report = open(
            f"/Volumes/Files/Projects/Python-oop-database/gradereport/{studentid}.txt",
            "w")
        student_report.write(json.dumps(report))
        student_report.close()
        database.close()
        print("Grade report successfuly added to /gradereport!")

    except:
        print("Student not found!")

#Developed By Moein Rezaie