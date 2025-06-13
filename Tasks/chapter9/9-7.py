#!/usr/bin/python3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
        
user1 = User('Joe', 'Gleason')
user2 = User('Heather', 'Mundinger')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges:")
        for right in self.privileges:
            print(f"- {right}")

class Privileges:
    def __init__(self,):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges:")
        for right in self.privileges:
            print(f"- {right}")
               
admin_user = Admin("Joe", "Gleason")

print("\n--- Admin Privileges ---")
admin_user.describe_user()
admin_user.show_privileges()

print("\n--- Admin Info ---")
admin_user.describe_user()

