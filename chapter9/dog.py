#!/usr/bin/python3
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Willie', 6)
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
