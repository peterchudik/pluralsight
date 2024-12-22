######################
# Dynamic attributes
######################

# __dict__
# dictionary, where object attributes (name and value) are stored 
# can be modified directly or using build in functions


# class Test:
#     pass

# t = Test()
# print(t.__dict__)
# # directly
# t.__dict__["x"] = 15
# print(t.__dict__)
# t.__dict__["y"] = 20
# print(t.__dict__)
# del t.__dict__["x"]
# print(t.__dict__)
# # build in functions
# print(hasattr(t, "x"))
# setattr(t, "x", 30)
# print(t.__dict__)
# print(getattr(t, "x"))
# delattr(t, "x")
# print(t.__dict__)



# class MyClass:

#     def __init__(self, **my_attributes):
#         self.__dict__.update(my_attributes)
    
#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k,
#                     v=v,
#                 ) for k, v in self.__dict__.items()
#             )
#         )

# m = MyClass(x = 1, y = 2)
# print(m)

# m1 = MyClass(a = 1, b = 2)
# print(m1)



######################
# Customize attributes read access
######################
# __getattr__
# method invokes after the failed attribute lookup

# class Test:
#     def __getattr__(self, name):
#         return f"Name {name} exists and has value 1"

# t = Test()
# print(t.x)




######################
# Prevent attributes write access
######################
# __setattr__
# method invokes when setting attribute


# class Test:
#     def __setattr__(self, name, value):
#         raise AttributeError(f"Name {name} cannot be set")

# t = Test()
# t.x = 10



######################
# Prevent attributes deletion
######################

class Test:
    def __delattr__(self, name):
        raise AttributeError(f"Name {name} cannot be deleted")

t = Test()
t.x = 10
print(t.x)
delattr(t, "x")


