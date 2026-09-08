# FOR LOOP BASICS
friends = ["Alice", "Bob", "Charlie"]
for name in friends:
    print(f"Hello, {name}!")

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    upper = fruit.upper()
    length = len(fruit)
    print(f"{upper} — {length} letters")
print("Done!")

scores = [85, 42, 91, 38, 77, 55]
for score in scores:
    if score >= 60:
        print(f"{score} → PASS")
    else:
        print(f"{score} → FAIL")

# RANGE()
for i in range(5):            # 0 1 2 3 4
    print(f"Round {i}")

for i in range(1, 6):          # 1 2 3 4 5
    print(f"5 x {i} = {5 * i}")

for i in range(1, 6, 2):       # 1 3 5
    print(i)

for i in range(10, 0, -1):     # countdown 10..1
    print(i)

# ACCUMULATOR PATTERN
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

scores = [85, 42, 91, 38, 77]
total = 0
count = 0
for s in scores:
    total += s
    if s >= 60:
        count += 1
print(f"Sum: {total}, Passing: {count}")

numbers = [34, 78, 12, 99, 56]
biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n
print(f"Biggest: {biggest}")

# WHILE LOOP
countdown = 5
while countdown > 0:
    print(f"T minus {countdown}...")
    countdown -= 1
print("Liftoff!")

secret = "python"
guess = input("Password: ")
while guess != secret:
    print("Wrong! Try again.")
    guess = input("Password: ")
print("Access granted!")

running = True
while running:
    entry = input("Number (or 'quit'): ")
    if entry == "quit":
        running = False
    else:
        n = float(entry)
        print(f"Square: {n}² = {n * n}")
print("Bye!")

# BREAK & CONTINUE
for fruit in fruits:
    if fruit == "mango":
        break               # stop everything
    print(fruit)

numbers = [5, -3, 8, -1, 4]
for num in numbers:
    if num < 0:
        continue             # skip to next
    print(num)

# NESTED LOOPS
for day in range(1, 4):          # outer
    print(f"Day {day}")
    for meal in range(1, 3):      # inner
        print(f"  Meal {meal}")

for row in range(1, 5):
    for star in range(row):
        print("*", end=" ")
    print()

# COMMON MISTAKES
# Wrong — countdown never changes, infinite loop:
# while countdown > 0:
#     print(countdown)

# Right:
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

# Prefer += over total = total + price
total = 0
price = 15
total += price