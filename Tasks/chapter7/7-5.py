#!/usr/bin/python3
prompt = "Please enter age (or type 'quit' to exit): "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    
    age = int(message)
    if age < 3:
        print(f"Your ticket is FREE!")
    elif age >= 3 and age <= 12:
        print(f"Your ticket is $10.")
    else:
        print(f"Your ticket is $15")
