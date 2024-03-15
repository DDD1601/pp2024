import math

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return student_id, student_name, student_dob

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return course_id, course_name

def input_marks_for_course(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]}: "))
        mark = math.floor(mark * 10) / 10  
    return marks

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(','.join(map(str, item)) + '\n')