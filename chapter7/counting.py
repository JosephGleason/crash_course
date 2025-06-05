#!/usr/bin/python3
# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#bonus example
# countdown = 3

# while countdown > 0:
#     print(f"{countdown}...")
#     countdown -= 1

# print("Liftoff!")

#using continue in a loop
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
