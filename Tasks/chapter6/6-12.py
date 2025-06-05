#!/usr/bin/python3
cities = {
    'san juan': {
        'country': 'puerto rico',
        'population': 3400000,
        'fact': "it's a colony",
        'founded': 1521,
        'language': 'spanish',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13900000,
        'fact': 'it has the busiest train station in the world',
        'founded': 1603,
        'language': 'japanese',
    },
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'home of the Eiffel Tower',
        'founded': -300,  # BCE
        'language': 'french',
    },
    'new york': {
        'country': 'usa',
        'population': 8800000,
        'fact': 'nicknamed the Big Apple',
        'founded': 1624,
        'language': 'english',
    },
    'london': {
        'country': 'england',
        'population': 9000000,
        'fact': 'home to Buckingham Palace',
        'founded': 43,
        'language': 'english',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f" Country: {city_info['country'].title()}")
    print(f" Population: {city_info['population']}")
    print(f" Fact: {city_info['fact'].capitalize()}")
    print(f" Founded: {city_info['founded']}")
    print(f" Language: {city_info['language'].title()}")

    if city_info['population'] > 10000000:
        print(" Note: Wow, that's a megacity!")
