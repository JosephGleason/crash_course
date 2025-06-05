#!/usr/bin/python3
cities = {
    'san juan': {
        'country': 'puerto rico',
        'population': 3400000,
        'fact': "it's a colony",
    },
    'tokyo': {
        'country': 'japan',
        'population': 13900000,
        'fact': 'it has the busiest train station in the world',
    },
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'home of the Eiffel Tower',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f" Country: {city_info['country'].title()}")
    print(f" Population: {city_info['population']}")
    print(f" Fact: {city_info['fact'].capitalize()}")
