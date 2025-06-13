#!/usr/bin/python3
def make_pizza(size, *toppings):
    print(f"\nMaking a {str(size)}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#see making_pizzas.py for calls
