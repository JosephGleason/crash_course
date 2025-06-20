#!/usr/bin/python3

class Book:
    def __init__(self, title):
       self.__title = title

    def get_title(self):
        return self.__title

    def set_title(self, title):
        if title:
            self.__title = title

b = Book("The Alchemist")
print(b.get_title())     # should print the title

b.set_title("")          # should reject this
print(b.get_title())     # should still be "The Alchemist"

b.set_title("1984")      # should update it
print(b.get_title())     # should print "1984"
