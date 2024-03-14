from input import (
    input_number_of_students,
    input_student_info,
    input_number_of_courses,
    input_course_info,
    input_marks_for_course
)
from output import curses_output  # Placeholder for curses UI
from domains.student import Student
from domains.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def main(self):
        num_students = input_number_of_students()
        for _ in range(num_students):
            student_info = input_student_info()
            student = Student(*student_info)
            self.students.append(student)

        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course_info = input_course_info()
            course = Course(*course_info)
            self.courses.append(course)
            self.marks[course.course_id] = {}  # Using course ID as keys for marks dictionary

        while True:
            print("\nMenu:")
            print("1. List courses")
            print("2. List students")
            print("3. Select a course and input marks for students")
            print("4. Show student marks for a course")
            print("5. Calculate and sort students by GPA")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                for course in self.courses:
                    print(f"ID: {course.course_id}, Name: {course.course_name}")
            elif choice == "2":
                for student in self.students:
                    print(f"ID: {student.student_id}, Name: {student.student_name}")
            elif choice == "3":
                course_id = input("Enter course ID to input marks: ")
                if course_id in self.marks:
                    print(f"Entering marks for course {course_id}:")
                    course_students = [(s.student_id, s.student_name) for s in self.students]
                    self.marks[course_id] = input_marks_for_course(course_students)
                else:
                    print("Invalid course ID")
            elif choice == "4":
                course_id = input("Enter course ID to show marks: ")
                if course_id in self.marks:
                    print(f"Student marks for course ID {course_id}:")
                    for student_id, mark in self.marks[course_id].items():
                        student_name = next((student.student_name for student in self.students if student.student_id == student_id), "Unknown")
                        print(f"ID: {student_id}, Name: {student_name}, Mark: {mark}")
                else:
                    print("Invalid course ID")
            elif choice == "5":
                # Implement GPA calculation and sorting
                pass
            elif choice == "6":
                # Save data and exit
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
