#ADDITIONAL FUNCTIONS

# MULTIPLE RETURN
def min_and_max(numbers):
    return min(numbers), max(numbers)   # tuple!

low, high = min_and_max([3, 9, 1, 7])   # unpack
print(low, high)                          # 1  9

import math

def circle_stats(r):
    area = math.pi * r ** 2
    diam = 2 * r
    circ = 2 * math.pi * r
    return area, diam, circ

a, d, c = circle_stats(5)
print(f"area={a:.2f} diam={d}")

# classic swap trick using tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)   # 20  10

# *ARGS
def add_all(*numbers):
    total = 0
    for n in numbers:          # numbers is a tuple
        total = total + n
    return total

print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4))      # 10

def show(*items):
    print(items)          # a tuple
    print(len(items))     # how many

show("a", "b", "c")
# ('a', 'b', 'c')
# 3

def greet_all(greeting, *names):
    for name in names:
        print(greeting, name)

greet_all("Hi", "Alice", "Bob")
# Hi Alice
# Hi Bob

# **KWARGS
def show_profile(**info):
    for key, value in info.items():
        print(key, "=", value)

show_profile(name="Alice", age=30)
# name = Alice
# age = 30

def describe(**facts):
    print(facts)

describe(color="red", size="L")
# {'color': 'red', 'size': 'L'}

def introduce(name, **extra):
    print("Hi, I'm", name)
    for key, value in extra.items():
        print(key, ":", value)

introduce("Bob", age=25, job="dev")

# FUNCTIONS CALLING FUNCTIONS (COMPOSITION)
def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    else:
        return "F"

# test each helper alone
print(calculate_average([100, 80]))   # 90.0
print(get_grade(75))                    # F

def show_report(name, scores):
    avg = calculate_average(scores)
    grade = get_grade(avg)
    print(f"{name}: {avg:.1f} ({grade})")

show_report("Alice", [92, 88, 95])
show_report("Bob", [65, 72, 58])

# MINI PROJECT — STUDENT GRADE MANAGER
def get_status(grade):
    return "Pass" if grade != "F" else "Fail"

def create_student(name, *scores, **extras):
    avg = calculate_average(scores)
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
    print(f"Name: {student['name']}")
    print(f"Scores: {student['scores']}")
    print(f"Average: {student['average']:.1f}")
    print(f"Grade: {student['grade']} ({student['status']})")
    for key, value in student.items():
        if key not in ("name", "scores", "average", "grade", "status"):
            print(f"{key}: {value}")
    print()

def class_summary(students):
    total = 0
    for s in students:
        total += s["average"]
    print(f"Class average: {total / len(students):.1f}")

def run():
    alice = create_student("Alice", 92, 88, 95, age=14, city="Dubai")
    bob = create_student("Bob", 65, 72, 58, age=15)

    students = [alice, bob]

    for student in students:
        print_report_card(student)

    class_summary(students)

run()