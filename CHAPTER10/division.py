#!/usr/bin/python3

# 1.
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# 2. Preventing crashes

print("give me two numbers, and ill divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divdie by 0!")
    else:  
        print(answer)
