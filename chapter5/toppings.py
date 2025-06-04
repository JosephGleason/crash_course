#!/usr/bin/python3

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for topping in requested_toppings:
#     if topping == 'green peppers':
#         print(f"Sorry, we’re out of green peppers.")
#     else:
#         print(f"Adding {topping}.")
# print(f'\nFinished making the pizza!')

# requested_toppings = []
# # requested_toppings = ['pepperoni', 'olives']

# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}.")
#     print(f"\nFinished making your pizza!")
# else:
#     print(f"Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don’t have {topping}.")
