#!/usr/bin/python3

def no_c(my_string):
    no_c = []
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            no_c.append(letter)
    return "".join(no_c)

