#!/usr/bin/python3
prompt = "Enter topping (or 'quit'): "

active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(f"I'll add {message} to your pizza.")
    else:
        active = False
