#!/usr/bin/python3

filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating games.\n")

#appending
with open(filename, 'a') as file_object:
    file_object.write("I love pfinding meaning in large datasets.\n")
    file_object.write("I love creating apps.\n")
