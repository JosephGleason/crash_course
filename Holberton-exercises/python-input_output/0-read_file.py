#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as text:
        content = text.read()
    print(content)
