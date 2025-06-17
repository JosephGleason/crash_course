#!/usr/bin/python3

count = 0

for count in range(97,123):
    if count == 113 or count == 101:
        continue
    print("{}".format(chr(count)), end='')
