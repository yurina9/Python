#INT & FLOAT
age = 15
students = 28
score = -5

price = 9.99
height = 1.75
pi = 3.14159

#ARITHMETIC OPERATORS
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333333333333335
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 8)   # 256
print(round(3.14159, 2))  # 3.14

price = 250
quantity = 4
discount = 50
total = price * quantity - discount
print(f"Total: Rs. {total}")

#int() WITH input()
age = int(input("Enter your age: "))
print(age + 10)

price = float(input("Price: "))
print(price * 1.13)

#SHORTHAND OPERATORS
score = 0
score += 10
score -= 5
score *= 2

count = 0
count += 1
count += 1
count += 1
print(count)

total = 0
total += 120
total += 350
print(f"Total: Rs. {total}")

#STRINGS
greeting = "Hello, World!"
city = 'Kathmandu'
mood = "Python is on fire"

print("Hello, " + "world!")
print("*" * 15)

#STRING METHODS
word = "python"
print(word.upper())
print(word.lower())
print(word.title())
print(len(word))

name = input("Name: ").strip()

sentence = "Hello World"
print(sentence.startswith("Hello"))
print(sentence.endswith("World"))
print(sentence.replace("World", "Python"))
print("hello" in sentence)
print("Hello" in sentence)

#STRING INDEXING & SLICING
word = "Python"
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])
print(word[0:3])
print(word[2:])

#type() & CONVERSION
print(type("Hello"))
print(type(42))
print(type(3.14))
print(type(True))

age = input("Age: ")
print(type(age))

print(int("100"))
print(float("3.14"))
print(str(42))

age = int(input("Your age: "))
print(f"Next year: {age + 1}")

#BOOLEANS 
is_raining = False
has_homework = True

print(10 == 10)
print(10 != 5)
print(10 > 20)
print(10 <= 10)

#COMMON MISTAKES 
age = int(input("Age: "))
print(age + 10)

print(f"Age: {15}")

score = 100
if score == 100:
    print("correct comparison")
