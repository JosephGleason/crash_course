#!/usr/bin/python3
def make_car(manufacturer, model, **args):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    
    for key, value in args.items():
        car[key] = value
    return car

car_profile = make_car('Ford', 'Escape', color='grey', type='SUV')
print(car_profile)
