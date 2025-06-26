#!/usr/bin/python3

class Student():
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
    
    def to_json(self):
        return self.__dict__


s = Student("Ada", "Lovelace", 30)
data = s.to_json()
print(data)
