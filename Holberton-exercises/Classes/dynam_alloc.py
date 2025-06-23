#!/usr/bin/python3

class Car:
    def __init__(self, make):
        self.make = make
        
c = Car("toyota")

c.year = 2025
print(c.__dict__)
