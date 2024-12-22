# override __new__ method
# create new object, only if it does not exists yet


class OptimizedAllocations:

    _my_objects = {}

    def __new__(cls, x):
        if x not in cls._my_objects:
            obj = object.__new__(cls)
            cls._my_objects[x] = obj
        return cls._my_objects[x]

    def __init__(self, x):
        pass

o1 = OptimizedAllocations(1)
o2 = OptimizedAllocations(2)
o3 = OptimizedAllocations(2)

print(o1)
print(o2)
print(o3)

