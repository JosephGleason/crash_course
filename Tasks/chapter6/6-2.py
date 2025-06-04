#!/usr/bin/python3
favorite_numbers = {
    'alice': 7,
    'bob': 3,
    'carla': 9,
    'joe': 8,
    'heathy': 6,
}
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")
