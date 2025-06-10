#!/usr/bin/python3
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " The Great"
    return magicians

def show_magicians(magicians):
    for name in magicians:
        print(f"{name.title()}")

magicians = ['Helbert', 'Domekan', 'Elkasor']
great_magicians = make_great(magicians[:])

print("\nOriginal magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)
