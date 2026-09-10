#OOP
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
 
    def drive(self) -> None:
        print(f"You drive the {self.color} {self.model}")
 
    def stop(self) -> None:
        print(f"You stop the {self.color} {self.model}")
 
    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")