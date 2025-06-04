#!/usr/bin/python3
current_users = ['Joe', 'Heathy', 'Geo', 'Alice', 'Ed']
new_users = ['hella', 'Joe', 'sara', 'Heathy', 'alex']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Username {user} is taken. Please enter a new username.')
    else:
        print(f'Username {user} is available.')
