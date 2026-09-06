class Student:
    def __init__(self, student_id, name, department, semester, marks):
        self.student_id = int(student_id)
        self.name = name
        self.department = department
        self.semester = int(semester)
        self.marks = [int(mark) for mark in marks]

    def calculate_total(self):
        return self.marks[0] + self.marks[1] + self.marks[2]

    def calculate_average(self):
        return self.calculate_total() / 3

    def get_result(self):
        if (self.marks[0] >= 40 and
                self.marks[1] >= 40 and
                self.marks[2] >= 40):
            return "Pass"
        else:
            return "Fail"

    def update_marks(self, marks):
        self.marks = [int(mark) for mark in marks]

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", round(self.calculate_average(), 2))
        print("Result:", self.get_result())
        print("-" * 40)