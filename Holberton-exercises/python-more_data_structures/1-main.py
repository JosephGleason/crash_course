#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 2, 2]
new_list = search_replace(my_list, 2, 99)

print(new_list)
print(my_list)
