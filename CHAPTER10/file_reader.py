#!/usr/bin/python3

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

#-reading line by line

filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#-making list of lines from file

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

