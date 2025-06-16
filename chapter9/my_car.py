#!/usr/bin/python3

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_beetle = Car('volki', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
