#!/usr/bin/python3
message = input("How many people are in your dinner group?: ")
message = int(message)

if message > 8:
    print(f"You'll have to wait for a table.")
else:
    print('Your table is ready.')
