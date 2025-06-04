#!/usr/bin/python3
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)                      # Original list

motorcycles[0] = 'ducati'               # Change 'honda' to 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

moto = []
moto.append('bike1')
moto.append('bike2')
moto.append('bik3')
print(moto)

motorcycles.insert(0, 'harley-davidson')# Insert at the beginning
print(motorcycles)

del motorcycles[0]                      # Delete second item
print(motorcycles)

popped_moto = moto.pop()
print(moto)
print(popped_moto)

popped_bike = motorcycles.pop()         # Remove last item and store it
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_bike.title()}.")

popped_bike = motorcycles.pop(1)         
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_bike.title()}.")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)       # Remove by value
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
