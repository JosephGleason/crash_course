#!/usr/bin/python3

#2-3, 2-4
name = 'heather'
print('Hello, ' + name.upper() + ' would you like to learn Python today?')
print('Hello, ' + name.lower() + ' would you like to learn Python today?')
print('Hello, ' + name.title() + ' would you like to learn Python today?')
#2-5
print('Frank Herbert once said, \n"Fear is the mind-killer. \n Fear is the little-death that brings total obliteration. \n I will face my fear. \n I will permit it to pass over me and through me."')

# 2-6
famous_person = "Frank Herbert"
message = "Fear is the mind-killer. \nFear is the little-death that brings total obliteration. \nI will face my fear. \nI will permit it to pass over me and through me."
print(famous_person + ' once said, \n' + message)

#2-7
person = '\t Pedro \n'
print(person)
print(person.lstrip())
print(person.rstrip())
print(person.strip())
