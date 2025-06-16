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
