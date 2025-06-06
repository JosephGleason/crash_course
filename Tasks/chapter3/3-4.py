#!/usr/bin/python3
#3-4
guests = ['Albert Einstein', 'Frida Kahlo', 'Nelson Mandela']

print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

#3-5
guests = ['Albert Einstein', 'Frida Kahlo', 'Nelson Mandela']
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

print(f"\n{guests[1]} can't make it.\n")

guests[1] = 'Ada Lovelace'

print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

#3-6
guests = ['Albert Einstein', 'Ada Lovelace', 'Nelson Mandela']

print("Good news! We found a bigger table.\n")

guests.insert(0, 'Marie Curie')                     # Beginning
guests.insert(2, 'Leonardo da Vinci')               # Middle
guests.append('Malala Yousafzai')                   # End

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

#3-7
guests = ['Marie Curie', 'Albert Einstein', 'Leonardo da Vinci', 'Ada Lovelace', 'Nelson Mandela', 'Malala Yousafzai']

print("Sorry, the new table won’t arrive on time. We can invite only two people.\n")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, we can’t invite you to dinner.")

print()
print(f"{guests[0]}, you’re still invited.")
print(f"{guests[1]}, you’re still invited.")

del guests[0]
del guests[0]

print("\nFinal guest list:", guests)
