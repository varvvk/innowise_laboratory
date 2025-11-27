students = []

def add_student():
    name = input("Enter student name: ")

    if any(student["name"] == name for student in students):
        print("This student already exists")
        return

    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)

def add_grade():
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:

            while True:
                grade = input("Enter a grade 0-100 (or 'done' to finish): ")
                if grade == "done":
                    return

                try:
                    grade_int = int(grade)
                    if 0 <= grade_int <= 100:
                        student["grades"].append(grade_int)
                    else:
                        print("Value must be from 0 to 100")
                except ValueError:
                    print("Invalid input. Enter a grade 0-100 (or 'done' to finish)")
                    continue

    print(f"Student {name} doesn't exist")

def show_report():
    if not students:
        print("List of students is empty")
        return

    all_averages = []

    for student in students:
        if not student["grades"]:
            print(f"Student {student["name"]} has no grades")

        try:
            average = round(sum(student["grades"]) / len(student["grades"]), 1)
            print(f"{student["name"]} average grade is {average}")
            all_averages.append(average)
        except ZeroDivisionError:
            average = "N/A"
            print(f"{student["name"]} average grade is {average}")

    overall_avg = sum(all_averages) / len(all_averages)
    max_avg = max(all_averages)
    min_avg = min(all_averages)

    print("\n------------------------")
    print(f"Max average: {max_avg}")
    print(f"Min average: {min_avg}")
    print(f"Overall Average: {overall_avg}")

def find_top_performer():
    if not students:
        print("No students in the list.")
        return

    students_with_grades = [student for student in students if student["grades"]]

    if not students_with_grades:
        print("No grades available for any student.")
        return

    top_student = max(
        students,
        key=lambda student: sum(student["grades"]) / len(student["grades"])
    )

    top_avg = round(sum(top_student["grades"]) / len(top_student["grades"]), 1)
    print(f"The student with the highest average is {top_student["name"]} with a grade of {top_avg}")

while True:
    print("----------------------------------\n"
          "1. Add a new student\n"
          "2. Add a grades for a student\n"
          "3. Show report (all students)\n"
          "4. Find top performer\n"
          "5. Exit\n")
    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a correct number (1-5)")
        continue
    match user_input:
        case 1:
            add_student()
        case 2:
            add_grade()
        case 3:
            print("--- Student Report ---")
            show_report()
        case 4:
            find_top_performer()
        case 5:
            break