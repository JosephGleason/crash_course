#!/usr/bin/python3
def build_profile(first, last, **user_info):
    """"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Joe', 'Gleason',
                             location='Puerto Rico',
                             age='39')
print(user_profile)
