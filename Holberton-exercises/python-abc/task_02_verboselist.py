#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self,item):
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
