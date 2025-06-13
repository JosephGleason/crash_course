#!/usr/bin/python3

#parent class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
#child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        #add new attribute
        self.battery_size = 70
    
    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())  # → "2024 Tesla Model S"
my_tesla.update_odometer(5000)
my_tesla.read_odometer()
my_tesla.describe_battery()
