#!/usr/bin/python3
def make_pizza(*toppings):
    """"""
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'peppers', 'cheese')
