# using build in property descriptor

# class Test:

#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     def _xget(self):
#         return self._x
#     def _xset(self, value):
#         self._x = value
#     x = property(_xget, _xset)


# t = Test(1, 2)

# print(t.x)
# t.x = 3
# print(t.x)


# using own descriptor

class MyDescriptor:

    def __set_name__(self, owner, name):
        print("__set_name__ :", self, owner, name)
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        print("__get__ :", self, instance, owner)
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        print("__set__ :", self, instance, value)
        setattr(instance, self.private_name, value)

class Test:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    x = MyDescriptor()
    # y = MyDescriptor()


# print(dir(Test))
# print(vars(Test))

# t1 = Test(1, 2)
# t2 = Test(4, 5)

# print(vars(t1))
# print(vars(t2))

# print(t1.x)
# t1.x = 3
# print(t1.x)

# print(Test.x)

