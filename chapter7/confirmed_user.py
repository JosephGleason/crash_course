#!/usr/bin/python3
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = [] #empty list to hold users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())
