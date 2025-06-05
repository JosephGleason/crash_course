#!/usr/bin/python3
favorite_places = {
    'joe': ['austin', 'la', 'ny'],
    'heathy': ['ny', 'spain', 'georgia'],
    'paco': ['japan', 'spain', 'colombia'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f" {place.title()}")
