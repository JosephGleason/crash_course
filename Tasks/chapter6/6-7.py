#!/usr/bin/python3
joe0 = {
    'firstname': 'Joseph',
    'lastname': 'Gleason',
    'age': '39',
    'city': 'San Juan',
    }
joe1 = {
    'firstname': 'Joseph',
    'lastname': 'Gleason',
    'age': '39',
    'city': 'San Juan',
    }
joe2 = {
    'firstname': 'Joseph',
    'lastname': 'Gleason',
    'age': '39',
    'city': 'San Juan',
    }

people = [joe0, joe1, joe2]

for joes in people:
    print(f"\nFull Name: {joes['firstname']} {joes['lastname']}")
    print(f"Age: {joes['age']}")
    print(f"City: {joes['city']}")
