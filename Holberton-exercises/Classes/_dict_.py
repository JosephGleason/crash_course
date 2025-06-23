#!/usr/bin/python3

class Animal:
    def __init__(self, species):
        self.species = species
        self.sound = "unknown"
        
a = Animal("cat")

# These should print safely
print(getattr(a, "species"))                  # → "cat"
print(getattr(a, "sound"))                    # → "unknown"
print(getattr(a, "color", "no color info"))   # → "no color info"

