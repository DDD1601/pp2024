class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        return Student(student_id, student_name, student_dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_marks_for_course(self, students):
        marks = {}
        for student in students:
            mark = float(input(f"Enter mark for {student.student_name}: "))
            marks[student.student_id] = mark
        return marks

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.student_name}")

    def show_student_marks(self, course_id):
        print(f"Student marks for course ID {course_id}:")
        for student in self.students:
            if student.student_id in self.marks[course_id]:
                print(f"ID: {student.student_id}, Name: {student.student_name}, Mark: {self.marks[course_id][student.student_id]}")
            else:
                print(f"ID: {student.student_id}, Name: {student.student_name}, Mark: Not available")

    def main(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            student_info = self.input_student_info()
            self.students.append(student_info)

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            course_info = self.input_course_info()
            self.courses.append(course_info)
            self.marks[course_info.course_id] = {}  # Using course ID as keys for marks dictionary

        while True:
            print("\nMenu:")
            print("1. List courses")
            print("2. List students")
            print("3. Select a course and input marks for students")
            print("4. Show student marks for a course")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.list_courses()
            elif choice == 2:
                self.list_students()
            elif choice == 3:
                self.list_courses()
                course_id = input("Enter course ID to input marks: ")
                if course_id in self.marks:
                    print(f"Entering marks for course {course_id}:")
                    course_students = self.students
                    self.marks[course_id] = self.input_marks_for_course(course_students)
                else:
                    print("Invalid course ID")
            elif choice == 4:
                course_id = input("Enter course ID to show marks: ")
                if course_id in self.marks:
                    self.show_student_marks(course_id)
                else:
                    print("Invalid course ID")
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
