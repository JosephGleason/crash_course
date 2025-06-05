#!/usr/bin/python3
message = input("Enter a number: ")
message = int(message)

if message % 10 == 0:
    print("Number is a multiple of 10.")
else:
    print("It's not a multiple of 10.")
