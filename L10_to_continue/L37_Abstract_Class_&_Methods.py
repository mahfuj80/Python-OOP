from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print(self.name, " is eating")
    
#=========================================================

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name + " is barking")
    
#=========================================================

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name + " is meowing")

#========================================================

class Snake(Animal):
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(self.name + " is His His")

#========================================================



d1 = Dog("tuhin")
d1.make_sound()
d1.eat()

c1 = Cat("Pusi")
c1.eat()
c1.make_sound()

s1 = Snake("Kobra")
s1.eat()
s1.make_sound()
