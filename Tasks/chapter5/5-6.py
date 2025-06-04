#!/usr/bin/python3
age = 39

if age < 2:
    print(f'baby')
elif age >= 2 and age < 4:
    print(f'toddler')
elif age >= 4 and age < 13:
    print(f"The person is a kid.")
elif age >= 13 and age < 20:
    print(f"The person is a teenager.")
elif age >= 20 and age < 65:
    print(f"The person is an adult.")
else:
    print(f"The person is an elder.")
