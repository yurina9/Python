class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
 
    def eat(self) -> None:
        print(f"{self.name} is eating")
 
    def sleep(self) -> None:
        print(f"{self.name} is sleeping")
 
 
class Prey(Animal):
    def flee(self) -> None:
        print(f"{self.name} is fleeing")
 
 
class Predator(Animal):
    def hunt(self) -> None:
        print(f"{self.name} is hunting")
 
 
class Rabbit(Prey):
    pass
 
 
class Hawk(Predator):
    pass
 
 
class Fish(Prey, Predator):  # multiple inheritance - two parents
    pass
 
 
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")
 
rabbit.flee()  # Bugs is fleeing
hawk.hunt()    # Tony is hunting
fish.eat()     # Nemo is eating
fish.flee()    # Nemo is fleeing
fish.hunt()    # Nemo is hunting
 
