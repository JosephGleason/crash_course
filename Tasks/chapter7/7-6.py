#!/usr/bin/python3
prompt = "Please enter age (or type 'quit' to exit): "

#1
message = ""
while message != 'quit':
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

#2
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#          active = False
    
#     age = int(message)
#     if age < 3:
#          print(f"Your ticket is FREE!")
#     elif age >= 3 and age <= 12:
#          print(f"Your ticket is $10.")
#     else:
#          print(f"Your ticket is $15")

#3
# see 7-5.py code
