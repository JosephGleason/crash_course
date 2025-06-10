#!/usr/bin/python3
def sandwich(*toppings):
    print("\nMaking a sandwich with:")
    for topping in toppings:
        print(f" - {topping.title()}")

sandwich('turkey', 'lettuce', 'tomato')
sandwich('ham')
sandwich('cheese', 'mayo')
