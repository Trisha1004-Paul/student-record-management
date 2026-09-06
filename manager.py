class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_by_name(self, name):
        results = []

        for student in self.students:
            if student.name.lower() == name.lower():
                results.append(student)

        return results

    def search_by_department(self, department):
        results = []

        for student in self.students:
            if student.department.lower() == department.lower():
                results.append(student)

        return results

    def search_by_average(self, value):
        results = []

        for student in self.students:
            if student.calculate_average() > value:
                results.append(student)

        return results

    def display_all_students(self):
        for student in self.students:
            student.display_student()