import sys

class A:

    __slots__ = {"x", "y"}

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(10, 20)
# print(sys.getsizeof(a), sys.getsizeof(a.__dict__))
# slots remove __dict__
print(sys.getsizeof(a))

print(a.x)
print(a.y)
