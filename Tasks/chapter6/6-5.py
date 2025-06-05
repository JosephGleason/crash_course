#!/usr/bin/python3
rivers = {
    'hudson': 'america',
    'nile': 'egypt',
    'ganges': 'india',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")
