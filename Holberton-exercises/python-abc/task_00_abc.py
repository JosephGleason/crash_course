#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

#call them
# d = Dog()
# print(d.sound())  # → "Bark"

# c = Cat()
# print(c.sound())  # → "Meow"

# example: cant instantiate
# a = Animal()
# print(a.sound())
