#!/usr/bin/python3

class Book:
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value:
            self.__title = value

b = Book("The Hobbit")
b.title = ""
print(b.title)
