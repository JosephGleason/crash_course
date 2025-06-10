#!/usr/bin/python3
def greet_users(names):
    """"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)
