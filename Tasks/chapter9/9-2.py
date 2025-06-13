#!/usr/bin/python3
class Restaurant():

 def __init__(self, name, cuisine):
    self.name = name
    self.cuisine = cuisine
    
 def description(self):
    print(f"Restaurant: {self.name}")
    print(f"Cuisine: {self.cuisine}")
    
 def open_restaurant(self):
    print(f"{self.name} is now open.")
    
my_restaurant1 = Restaurant('La Isla', 'Puerto Rican')
my_restaurant2 = Restaurant('Cayo Caribe', 'Seafood')
my_restaurant3 = Restaurant('Panoteca', 'Bakery')

my_restaurant1.description()
my_restaurant2.description()
my_restaurant3.description()
