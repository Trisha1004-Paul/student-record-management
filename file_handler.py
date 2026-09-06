import csv
import json
from student import Student


def read_txt(filename):
    students = []

    with open(filename, "r") as file:
        for line in file:
            data = [item.strip() for item in line.split(",")]

            student = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4:7]
            )

            students.append(student)

    return students


def read_csv(filename):
    students = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4:7]
            )

            students.append(student)

    return students


def save_csv(filename, students):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student_ID",
            "Name",
            "Department",
            "Semester",
            "Subject1",
            "Subject2",
            "Subject3"
        ])

        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.department,
                student.semester,
                student.marks[0],
                student.marks[1],
                student.marks[2]
            ])


def read_json(filename):
    students = []

    with open(filename, "r") as file:
        data = json.load(file)

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["department"],
                item["semester"],
                [
                    item["marks"]["subject1"],
                    item["marks"]["subject2"],
                    item["marks"]["subject3"]
                ]
            )

            students.append(student)

    return students


def save_json(filename, students):
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "department": student.department,
            "semester": student.semester,
            "marks": {
                "subject1": student.marks[0],
                "subject2": student.marks[1],
                "subject3": student.marks[2]
            }
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)