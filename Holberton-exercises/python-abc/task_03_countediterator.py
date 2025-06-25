#!/usr/bin/python3

class CountedIterator():
    def __init__(self, data):
        self.iterator = iter(data)
        self.count = 0 #can be accesssed by all other methods

    def get_count(self):
        return self.count
    
    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item
    
    def __iter__(self):
        return self

iter1 = CountedIterator([10, 20 ,30])
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
print(iter1.get_count())

for item in iter1:
    print(item)
    print("Total items iterated:", iter1.get_count())

