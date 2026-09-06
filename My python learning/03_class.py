#LISTS
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits[0])                # apple
fruits[1] = "mango"
fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("cherry")
last = fruits.pop()
print(len(fruits))
print(fruits.index("apple"))
print(fruits.count("banana"))
fruits.sort()
fruits.reverse()
print(fruits[0:2])
print("mango" in fruits)

#TUPLES 
point = (10, 20, 10)
print(point[0])           # 10
# point[0] = 99            # ERROR — tuples are immutable
print(point.index(20))
print(point.count(10))
print(len(point))

#DICTIONARIES 
student = {
    "name": "Aisha",
    "age": 14,
    "grade": "A"
}
print(student["name"])
print(student.get("school", "N/A"))
student["age"] = 15
student["school"] = "Central High"
student.update({"city": "Dubai", "age": 15})
old_grade = student.pop("grade")
print(student.keys())
print(student.values())
print(student.items())
backup = student.copy()
print("name" in student)

#IF / ELSE 
if student["age"] >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")

password = input("Enter password: ")
if password == "python123":
    print("Access granted!")
else:
    print("Wrong password!")

score = 75
if score >= 60:
    print("You passed!")
    print("Well done!")
else:
    print("You failed.")
print("Exam is over.")   # not indented — always runs

#ELIF
score = 82
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

light = input("Colour? ").lower()
if light == "red":
    print("STOP!")
elif light == "yellow":
    print("Get ready...")
elif light == "green":
    print("GO!")
else:
    print("Unknown colour!")

month = int(input("Month (1-12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Autumn")

# LOGICAL OPERATORS 
age = 20
has_id = True
if age >= 18 and has_id:
    print("Welcome! You may enter.")
else:
    print("Entry denied.")

is_member = True
has_points = False
if is_member and has_points:
    print("Free gift!")          # won't run

if is_member or has_points:
    print("You get a discount!")  # runs

is_raining = False
if not is_raining:
    print("Great day for a walk!")

#  TRUTHY / FALSY 
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False
print(bool(1))        # True
print(bool("hello"))  # True
print(bool([1, 2]))   # True

name = input("Your name: ")
if name:
    print(f"Hello, {name}!")

#  GRADE CALCULATOR (putting it all together) 
name = input("Student name: ")
score = int(input("Score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score!")
elif score >= 90:
    print(f"{name}: A - Distinction!")
elif score >= 80:
    print(f"{name}: B - Well done!")
elif score >= 70:
    print(f"{name}: C - Good effort.")
elif score >= 60:
    print(f"{name}: D - Passing.")
else:
    print(f"{name}: F - Study harder!")