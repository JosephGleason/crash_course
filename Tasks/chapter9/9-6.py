#!/usr/bin/python3
class Restaurant():

 def __init__(self, name, cuisine):
    self.name = name
    self.cuisine = cuisine
    self.number_served = 0
    
 def description(self):
    print(f"Restaurant: {self.name}")
    print(f"Cuisine: {self.cuisine}")
    
 def open_restaurant(self):
    print(f"{self.name} is now open.")
    
 def set_number_served(self, number_served):
     self.number_served = number_served
    
 def increment_number_served(self, served):
     self.number_served += served
     
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
       super().__init__(name, cuisine)
       self.flavors = ["vanilla", "chocolate", "strawberry"]
    
    def display_flavors(self):
        print(f"Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
my_restaurant = Restaurant('La Isla', 'Puerto Rican')
ice_cream_stand = IceCreamStand("La Heladería", "ice cream")

print(f"{my_restaurant.name.title()}")
print(f"{my_restaurant.cuisine.title()}")
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.number_served = 4
print(f"{my_restaurant.name.title()}")
print(f"{my_restaurant.cuisine.title()}")
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.set_number_served(1)
print(f"{my_restaurant.name.title()}")
print(f"{my_restaurant.cuisine.title()}")
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.increment_number_served(4)
print(f"{my_restaurant.name.title()}")
print(f"{my_restaurant.cuisine.title()}")
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.description()
my_restaurant.open_restaurant()

print("\n--- Ice Cream Stand ---")
ice_cream_stand.description()
ice_cream_stand.display_flavors()

