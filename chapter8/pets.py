#!/usr/bin/python3

# POSITIONAL ARGUMENTS
# def describe_pet(animal_type, pet_name):
#     """""" 
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
    
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

#KEYWORD ARGUMENTS
# def describe_pet(animal_type, pet_name):
#     """""" 
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
    
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(animal_type='dog', pet_name='willie')

#DEFAULT VALUES
def describe_pet(pet_name, animal_type='dog'):
    """""" 
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pet('harry')
describe_pet('willie')
