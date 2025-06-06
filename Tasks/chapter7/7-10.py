#!/usr/bin/python3
dreamers = {}

active = True
while active:
    name = input("What is your name? ")
    mountain = input('Where is your dream vacation? ')
    
    dreamers[name] = mountain
    
    question = input('Would you like another person to respond? (y/n)')
    if question == 'n':
        active = False

print('--Poll Results--')
for name, mountain in dreamers.items():
    print(f"{name.title()} would like to visit {mountain.title()}")
