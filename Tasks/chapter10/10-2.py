#!/usr/bin/python3

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
remove_lines = ''
for text in lines:
    remove_lines += text.replace("Python", "C".strip())
    print(remove_lines)
