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

    # Other methods from the original implementation

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

            # The rest of the main functionality goes here

if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
