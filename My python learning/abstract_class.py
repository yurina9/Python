from abc import ABC, abstractmethod
 
 
class Vehicle(ABC):
    @abstractmethod
    def go(self) -> None:
        pass
 
    @abstractmethod
    def stop(self) -> None:
        pass
 
 
class Car(Vehicle):
    def go(self) -> None:
        print("You drive the car")
 
    def stop(self) -> None:
        print("You stop the car")
 
 
class Motorcycle(Vehicle):
    def go(self) -> None:
        print("You ride the motorcycle")
 
    def stop(self) -> None:
        print("You stop the motorcycle")
 
 
class Boat(Vehicle):
    def go(self) -> None:
        print("You sail the boat")
 
    def stop(self) -> None:
        print("You anchor the boat")
 
 
# vehicle = Vehicle()  # TypeError! Can't instantiate an abstract class
car = Car()
car.go()
car.stop()