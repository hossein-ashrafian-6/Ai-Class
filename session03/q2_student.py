class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
        else:
            self.grades[course] = grade

    def average(self):
        if not self.grades:
            return 0

        return sum(self.grades.values()) / len(self.grades)

    def best_course(self):
        if not self.grades:
            return None

        return max(self.grades, key=self.grades.get)

    def failed_courses(self):
        failed = []

        for course, grade in self.grades.items():
            if grade < 10:
                failed.append(course)

        return failed

    def status(self):
        avg = self.average()

        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        print()

        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
            print()

        print(f"Average: {self.average()}")
        print()
        print(f"Best course: {self.best_course()}")
        print()
        print(f"Failed courses: {self.failed_courses()}")
        print()
        print(f"Status: {self.status()}")


# Bonus: Classroom class

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.average())

    def class_average(self):
        if not self.students:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)


# Testing the Student class

student1 = Student("Sara Ahmadi", "40312345")
student1.add_grade("Math", 18)
student1.add_grade("Physics", 9)
student1.add_grade("Programming", 20)
student1.add_grade("English", 15)

student2 = Student("Ali Mohammadi", "40312346")
student2.add_grade("Math", 16)
student2.add_grade("Physics", 14)
student2.add_grade("Programming", 17)
student2.add_grade("English", 13)

# Print student reports
student1.report()
print("\n" + "=" * 40 + "\n")
student2.report()

# Test invalid grade
print("\nTesting invalid grade:")
student1.add_grade("Chemistry", 25)

# Testing the Classroom class
classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)

top = classroom.top_student()

print("\nClassroom Results:")
if top is not None:
    print(f"Top student: {top.name}")
    print(f"Top student average: {top.average()}")

print(f"Class average: {classroom.class_average()}")
