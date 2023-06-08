from classes import info, courses
import json, os
def get_operation():
    global operation
    operation = int(input("Enter you considered operation. [1]>Add Studen, [2]>Search Studen: "))
    if operation== 1 or operation==2:
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
    #path = os.path("/media/moein/01D70E1AFEF55AF0/Projects/Python-oop-database/data")
    user_file = open(f"/media/moein/01D70E1AFEF55AF0/Projects/Python-oop-database/data/{studentid}.txt", "w")
    user_file.write(json.dumps(all_info))
    user_file.close()
else:
    #search person
    pass

