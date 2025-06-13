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
    
my_restaurant = Restaurant('La Isla', 'Puerto Rican')
print(f"{my_restaurant.name.title()}")
print(f"{my_restaurant.cuisine.title()}")

my_restaurant.description()
my_restaurant.open_restaurant()
