#FUNCTIONS

# DEFINING AND CALLING
def say_hello():
    print("Hello, world!")

say_hello()

# FUNCTION ANATOMY
def greet_user(name):
    """Greet someone by name."""
    print(f"Hello, {name}!")

greet_user("Alice")

# PARAMETERS VS ARGUMENTS
def greet_person(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Alice")           # "Alice" is an argument
greet_person("Bob")

# MULTIPLE PARAMETERS
def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Fluffy", "cat")
describe_pet("Rex", "dog")
describe_pet("Nemo", "fish")

# order matters — arguments match positionally, left to right
describe_pet("cat", "Fluffy")   # wrong order → confusing output

# RETURN VALUES
def add_numbers(a, b):
    total = a + b
    return total

answer = add_numbers(3, 5)
print(answer)                     # 8
print(add_numbers(10, 20) + 5)    # 35

# RETURN PATTERNS
def check_age(age):
    if age < 18:
        return "Minor"
    return "Adult"

print(check_age(15))   # Minor
print(check_age(25))   # Adult

def square(n):
    return n * n

def c_to_f(c):
    return (c * 9/5) + 32

print(square(4))       # 16
print(c_to_f(100))     # 212.0

# DEFAULT PARAMETERS
def greet(name="friend"):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet()          # Hello, friend!

def make_smoothie(fruit, size="medium", ice=True):
    ice_txt = "with ice" if ice else "no ice"
    print(f"{size} {fruit} smoothie ({ice_txt})")

make_smoothie("mango")
make_smoothie("banana", "large")
make_smoothie("berry", "small", False)

# mutable default gotcha
def bad(item, lst=[]):          # DANGER — shared across calls!
    lst.append(item)
    return lst

def good(item, lst=None):        # correct way
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# KEYWORD ARGUMENTS
def describe_pet2(name, animal, age):
    print(f"{name} is a {age}-year-old {animal}.")

describe_pet2(animal="dog", age=5, name="Rex")   # order doesn't matter

# SCOPE
def demo():
    x = 5   # local
demo()
# print(x)   # ERROR — x doesn't exist outside demo()

y = 10       # global
def show():
    print(y)   # works — reading a global variable

show()