#!/usr/bin/python3
sandwich_orders = ['cubano', 'club', 'pastrami', 'pastrami', 'pastrami', 'phillycheese']
finished_sandwiches = []

print(f"\nDeli has run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwies in finished_sandwiches:
    print(f"Finished sandwich: {sandwies.title()}")
