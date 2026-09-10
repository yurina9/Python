class Student:
    class_year = 2024   # class variable - shared by every Student
    num_students = 0    # class variable - acts as a counter
 
    def __init__(self, name: str, age: int) -> None:
        self.name = name  # instance variable - unique to each object
        self.age = age
        Student.num_students += 1
 
 
student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)
 
print(student1.name)          # SpongeBob
print(Student.class_year)     # 2024
print(Student.num_students)   # 2