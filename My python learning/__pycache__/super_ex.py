class Shape:
    def __init__(self, color: str, is_filled: bool) -> None:
        self.color = color
        self.is_filled = is_filled
 
    def describe(self) -> None:
        print(f"It is {self.color} and "
              f"{'filled' if self.is_filled else 'not filled'}")
 
 
class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)  # reuse Shape's __init__
        self.radius = radius
 
    def describe(self) -> None:
        print(f"It is a circle with area "
              f"{3.14 * self.radius ** 2} cm^2")
        super().describe()  # add to, rather than replace, the parent's version
 
 
class Square(Shape):
    def __init__(self, color, is_filled, width) -> None:
        super().__init__(color, is_filled)
        self.width = width
 
 
circle = Circle("red", True, 4)
circle.describe()
 
