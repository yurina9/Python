#MINI PROJECT

# HELPER FUNCTIONS
def calculate_average(*scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_status(grade):
    return "Pass" if grade != "F" else "Fail"

# BUILDER + PRINTER
def create_student(name, *scores, **extras):
    avg = calculate_average(*scores)
    grade = get_grade(avg)
    status = get_status(grade)

    student = {
        "name": name,
        "scores": scores,
        "average": avg,
        "grade": grade,
        "status": status,
    }
    student.update(extras)
    return student

def print_report_card(student):
    print("=" * 30)
    print(f"Name    : {student['name']}")
    print(f"Scores  : {student['scores']}")
    print(f"Average : {student['average']:.1f}")
    print(f"Grade   : {student['grade']} ({student['status']})")

    core_keys = ("name", "scores", "average", "grade", "status")
    for key, value in student.items():
        if key not in core_keys:
            print(f"{key.title()}  : {value}")
    print("=" * 30)

def class_summary(students):
    total = 0
    for s in students:
        total += s["average"]
    class_avg = total / len(students)
    print(f"\nClass Average: {class_avg:.1f}")
    print(f"Total Students: {len(students)}")

# COORDINATOR / DRIVER
def run():
    yuri = create_student("Yuri", 92, 88, 95, age=14, city="Dubai")
    roji = create_student("Roji", 65, 72, 58, age=15)
    kritika = create_student("Kritika", 55, 60, 48, age=14, city="Doha")

    students = [yuri, roji, kritika]

    for student in students:
        print_report_card(student)

    class_summary(students)

run()