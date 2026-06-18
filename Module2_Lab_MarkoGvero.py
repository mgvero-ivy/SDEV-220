#|Author: Marko Gvero
#|File Name: Module2_Lab_MarkoGvero.py
#|This app will take a Student's name and GPA and determine if they are on honor roll or Dean's List

student_last_name = str
student_first_name = str
student_gpa = float

while True:
    print("please enter the student's last name or 'ZZZ' to quit: ")
    student_last_name = input()

    if student_last_name == 'ZZZ':
        break

    print("please enter the student's first name")
    student_first_name = input()
    print("please enter the student's GPA")
    student_gpa = float(input())

    if student_gpa < 3.25:
        print(f"{student_first_name} {student_last_name} has not made the Honor Roll or Dean's List")
    elif student_gpa < 3.5:
        print(f"{student_first_name} {student_last_name} has made the Honor Roll")
    else:
        print(f"{student_first_name} {student_last_name} has made the Dean's List")


'''
Testing Results
-----------------------------------------------------------------------

please enter the student's last name or 'ZZZ' to quit: 
Simpson
please enter the student's first name
Bart
please enter the student's GPA
1.3
Bart Simpson has not made the Honor Roll or Dean's List
please enter the student's last name or 'ZZZ' to quit: 
Simpson
please enter the student's first name
Lisa
please enter the student's GPA
4.0
Lisa Simpson has made the Dean's List
please enter the student's last name or 'ZZZ' to quit: 
VanHouten
please enter the student's first name
Milhouse
please enter the student's GPA
2.7
Milhouse VanHouten has not made the Honor Roll or Dean's List
please enter the student's last name or 'ZZZ' to quit: 
Wiggum
please enter the student's first name
Ralph
please enter the student's GPA
0.0
Ralph Wiggum has not made the Honor Roll or Dean's List
please enter the student's last name or 'ZZZ' to quit: 
Powell
please enter the student's first name
Janey
please enter the student's GPA
3.4
Janey Powell has made the Honor Roll
please enter the student's last name or 'ZZZ' to quit: 
Muntz
please enter the student's first name
Nelson
please enter the student's GPA
0.9
Nelson Muntz has not made the Honor Roll or Dean's List
please enter the student's last name or 'ZZZ' to quit: 
ZZZ

Process finished with exit code 0'''