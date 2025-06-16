#!/usr/bin/python3

#1.
# with open('/home/theinnerlight/crash-course/Tasks/chapter10/learning_python.txt') as learning:
    # content = learning.read()
    # print(content.strip())
    
#2.

filename = 'learning_python.txt'

# with open(filename) as file_object:
#     for text in file_object:
#         print(text.strip())


#3

with open(filename) as file_object:
    lines = file_object.readlines()
    
    for text in lines:
        print(text.strip())
