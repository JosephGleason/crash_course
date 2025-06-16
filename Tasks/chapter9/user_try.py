#!/usr/bin/python3

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
        
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class Privileges:
    def __init__(self,):
        self.privileges =  ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges:")
        for right in self.privileges:
            print(f"- {right}")
