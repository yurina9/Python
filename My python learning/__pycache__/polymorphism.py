from abc import ABC, abstractmethod
 
 
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
 
 
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
 
    def area(self) -> float:
        return 3.14 * self.radius ** 2
 
 
class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side
 
    def area(self) -> float:
        return self.side ** 2
 
 
class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
 
    def area(self) -> float:
        return self.base * self.height * 0.5
 
 
class Pizza(Circle):  # inherits area() from Circle, adds a topping
    def __init__(self, topping: str, radius: float) -> None:
        super().__init__(radius)
        self.topping = topping
 
 
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]
 
for shape in shapes:
    print(f"{shape.area()} cm^2")  # same call works for every shape
 
