# ------------------------------------------
# Metaclasses
# ------------------------------------------

class Widget:
    pass

w = Widget()

# type() of an instance is its class
print(type(w))

# type() of class is class type
print(type(Widget))

# type of any class in python is its metaclass and default metaclass is type
# type of class type is again class type

print(w.__class__)
print(w.__class__.__class__)
print(w.__class__.__class__.__class__)

# below is the same is 
# class Widget:
#     pass
# first positional argument is defalut base class
# default metaclass as keyword argument is type
class Widget(object, metaclass=type):
    pass

# bit

value = 3
bit_value = 0
bit_value |= value

print(bin(bit_value))
