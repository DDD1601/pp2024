from background_persistence import BackgroundPersistence
from input import (
    input_number_of_students,
    input_student_info,
    input_number_of_courses,
    input_course_info,
    input_marks_for_course,
    write_to_file
)
from output import curses_output  
from domains.student import Student
from domains.course import Course


DATA_FILE = "students.dat"
background_persistence = BackgroundPersistence(DATA_FILE)


background_persistence.start()

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def main(self):
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
                self.list_courses()
            elif choice == "2":
                self.list_students()
            elif choice == "3":
                self.input_marks_for_students()
            elif choice == "4":
                self.show_student_marks_for_course()
            elif choice == "5":
                self.calculate_and_sort_by_gpa()
            elif choice == "6":
                self.save_data()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def input_marks_for_students(self):
        self.list_courses()
        course_id = input("Enter course ID to input marks: ")
        if course_id in self.courses:
            print(f"Entering marks for course {course_id}:")
            course_students = [(student.student_id, student.student_name) for student in self.students]
            self.marks[course_id] = input_marks_for_course(course_students)
            background_persistence.set_data((self.students, self.courses, self.marks))
        else:
            print("Invalid course ID")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.student_name}")

    def show_student_marks_for_course(self):
        course_id = input("Enter course ID to show marks: ")
        if course_id in self.marks:
            print(f"Student marks for course ID {course_id}:")
            for student_id, mark in self.marks[course_id].items():
                student_name = next((student.student_name for student in self.students if student.student_id == student_id), "Unknown")
                print(f"ID: {student_id}, Name: {student_name}, Mark: {mark}")
        else:
            print("Invalid course ID")

    def calculate_and_sort_by_gpa(self):
        sorted_students = self.sort_students_by_gpa()
        for student in sorted_students:
            print(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {self.calculate_gpa(student.student_id)}")

    def calculate_gpa(self, student_id):
        total_credits = 0
        weighted_sum = 0

        for course_id, marks in self.marks.items():
            if student_id in marks:
                course = next((course for course in self.courses if course.course_id == course_id), None)
                if course:
                    total_credits += course.credits
                    weighted_sum += course.credits * marks[student_id]

        if total_credits == 0:
            return 0
        else:
            return weighted_sum / total_credits

    def sort_students_by_gpa(self):
        return sorted(self.students, key=lambda student: self.calculate_gpa(student.student_id), reverse=True)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with gzip.open(DATA_FILE, 'rb') as f:
                data = f.read()
                if data:
                    self.students, self.courses, self.marks = pickle.loads(data)
        else:
            print("No data file found.")

    def save_data(self):
        background_persistence.set_data((self.students, self.courses, self.marks))

if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.load_data()  
    school_system.main()
