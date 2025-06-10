#!bn/usr/bin/python3

#returning a dictionary

# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

#adding values
def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

print(build_person('jimi', 'hendrix'))
print(build_person('jimi', 'hendrix', age=27))
