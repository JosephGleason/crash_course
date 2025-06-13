#!/usr/bin/python3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
    def increment_login_attempts(self, attempt):
        self.login_attempts += attempt
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User('Joe', 'Gleason')
user2 = User('Heather', 'Mundinger')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)

print(f"Login attempts for {user1.first_name}: {user1.login_attempts}")

user2.increment_login_attempts(1)
user2.increment_login_attempts(2)
user2.increment_login_attempts(1)

print(f"Login attempts for {user2.first_name}: {user2.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
