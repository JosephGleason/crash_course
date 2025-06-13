#!/usr/bin/python3
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #1.setting default value on attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")
        
    def update_odometer(self, mileage): #2.method to modify attr through method
        self.odometer_reading = mileage
    
    def increment_odometer(self, miles): #3 increment attribute value
        self.odometer_reading += miles

my_car = Car('toyota', 'camry', 2022)
my_new_car = Car('audi', 'a4', 2024)
my_used_car = Car('subaru', 'outback', 2013)

print(my_car.get_descriptive_name())
print(my_new_car.get_descriptive_name())
print(my_used_car.get_descriptive_name())

my_car.update_odometer(50)
my_car.increment_odometer(10)

my_new_car.odometer_reading = 23 #1.access attribute directly through instance
my_new_car.update_odometer(23) #2.modify attribute throuh method

my_used_car.update_odometer(23500) #3. incremente through method

my_car.read_odometer()
my_new_car.read_odometer()
my_used_car.read_odometer()

