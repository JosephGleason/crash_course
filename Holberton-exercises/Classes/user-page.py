#!/usr/bin/python3

class User:
    def __init__(self, email):
        self.__email = email
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            print('Invalid email')

u = User("user@example.com")
print(u.email)         # ✅ user@example.com

u.email = "bademail"   # ❌ Invalid email
print(u.email)         # ✅ still user@example.com

u.email = "new@email.com"
print(u.email)         # ✅ new@email.com
