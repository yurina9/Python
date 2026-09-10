from car import Car
 
# Create multiple objects from the same class blueprint
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "black", False)
 
# Each object stores its own independent data
print(car1.model)  # Mustang
print(car2.model)  # Corvette
print(car3.model)  # Charger
 
# Call methods with dot notation
car1.drive()
car1.stop()
car1.describe()
 
car2.describe()