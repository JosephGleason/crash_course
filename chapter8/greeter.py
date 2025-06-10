#!/usr/bin/python3
# def greet_user(username):
#     """Displays a greeting"""
#     print(f"Hello {username.title()}!")
    
# greet_user('joseph')

#USING A FUNCTION WITH A WHILE LOOP
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
