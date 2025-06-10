#!/usr/bin/python3
def city_country(city, country):
    place = f"{city.title()}, {country.title()}"
    return place

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
