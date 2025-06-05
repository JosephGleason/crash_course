#!/usr/bin/python3
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# print(f"Sarah's fav language is {favorite_languages['sarah'].title()}")

# for name in favorite_languages.keys():
#     print(f"{name.title()}")

# friends = ['phil', 'sarah']
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}")
    
#     if name in friends:
#         print(f" Hi {name.title()}, I see your favoite language is {favorite_languages[name].title()}!")
# if 'erin' not in favorite_languages.keys():
#     print(f"\nErin, please take our poll.")

for language in set(favorite_languages.values()):
    print(f"{language.title()}")
