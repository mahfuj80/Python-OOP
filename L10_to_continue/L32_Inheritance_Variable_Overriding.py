class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "white"
    
    def eat(self):
        print(self.color, self.name, "is Eating")

#=============================================================

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color  # variable override for color

    def bark(self):
        print(self.color, self.name, "is Barking")

#=============================================================

a1 = Animal("Jack")
d1 = Dog("Rover", "Brown")

d1.bark()
d1.eat()

a1.eat()