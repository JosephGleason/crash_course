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

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            
#child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        #add new attribute
        self.battery = Battery()
    
    def describe_battery(self):
        print(f"This car has a {str(self.battery.battery_size)}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2024)

print(my_tesla.get_descriptive_name())  # → "2024 Tesla Model S"
my_tesla.update_odometer(5000)
my_tesla.read_odometer()
my_tesla.describe_battery()

print("\nMake an electric car, and check the range:")
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
