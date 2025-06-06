#!/usr/bin/python3
sandwich_orders = ['cubano', 'club', 'phillycheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwies in finished_sandwiches:
    print(f"Finished sandwich: {sandwies.title()}")
