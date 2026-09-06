import argparse
from manager import StudentManager
from file_handler import read_txt, read_csv, read_json


def main():
    parser = argparse.ArgumentParser(
        description="Student Record Management System"
    )

    parser.add_argument("--file", required=True)
    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"]
    )

    args = parser.parse_args()

    manager = StudentManager()

    if args.format == "txt":
        students = read_txt(args.file)
    elif args.format == "csv":
        students = read_csv(args.file)
    else:
        students = read_json(args.file)

    for student in students:
        manager.add_student(student)

    print("\n===== ALL STUDENTS =====")
    manager.display_all_students()

    print("\n===== SEARCH BY STUDENT ID =====")
    student = manager.search_student(101)

    if student:
        student.display_student()

    print("\n===== SEARCH BY NAME =====")
    results = manager.search_by_name("Priya")

    for student in results:
        student.display_student()

    print("\n===== SEARCH BY DEPARTMENT =====")
    results = manager.search_by_department("Computer Science")

    for student in results:
        student.display_student()

    print("\n===== AVERAGE ABOVE 80 =====")
    results = manager.search_by_average(80)

    for student in results:
        student.display_student()


if __name__ == "__main__":
    main()