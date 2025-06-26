#!/usr/bin/python3

class Student():
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
    
    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])



s = Student("Ada", "Lovelace", 30)
data = s.to_json()
print(data)

update_data = {"first_name": "Alan", "age": 42}
s.reload_from_json(update_data)
print(s.__dict__)
