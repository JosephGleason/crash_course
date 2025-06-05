#!/usr/bin/python3
pet1 = {
    'animal': 'dog',
    'name': 'Rex',
    'owner': 'Alice',
}

pet2 = {
    'animal': 'cat',
    'name': 'Whiskers',
    'owner': 'Bob',
}

pet3 = {
    'animal': 'parrot',
    'name': 'Polly',
    'owner': 'Charlie',
}

pets = [pet1, pet2, pet3]

for animals in pets:
    print(f"\nAnimal: {animals['animal'].title()}")
    print(f"Name: {animals['name']}")
    print(f"Owner: {animals['owner']}")
