#!/usr/bin/python3

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()
    
#     pi_string = ''
#     for line in lines:
#         pi_string += line.strip()
        
#     print(pi_string)
#     print(len(pi_string))


#-large files

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

birthday = input("Enter Bday, in mmddyy form: ")
if birthday in pi_string:
    print("your bday appears in pi")
else:
    print("your bday doesnt appear in pi")
    print(pi_string[:52] + "...")
    print(len(pi_string))
