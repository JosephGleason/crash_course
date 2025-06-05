#!/usr/bin/python3
favorite_numbers = {
    'joe': [1, 2, 3],
    'heathy': [4, 5, 6],
    'paco': [7, 8, 9],
}

for name, number in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for num in number:
        print(f"{num}")
