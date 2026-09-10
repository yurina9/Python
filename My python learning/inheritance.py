class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.is_alive = True
 
    def eat(self) -> None:
        print(f"{self.name} is eating")
 
    def sleep(self) -> None:
        print(f"{self.name} is sleeping")
 
 
class Dog(Animal):
    def speak(self) -> None:
        print("Woof!")
 
 
class Cat(Animal):
    def speak(self) -> None:
        print("Meow!")
 
 
class Mouse(Animal):
    def speak(self) -> None:
        print("Squeak!")
 
 
dog = Dog("Scooby")
print(dog.name)       # Scooby
print(dog.is_alive)   # True
 
dog.eat()     # Scooby is eating
dog.sleep()   # Scooby is sleeping
dog.speak()   # Woof!
 
