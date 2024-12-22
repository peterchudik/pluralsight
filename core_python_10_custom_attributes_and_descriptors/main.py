#----------------------------------------
# Object internals
#----------------------------------------

# Version 1
# from vector import Vector

# v = Vector(1, 5)

# print(v)
# print(dir(v))

#---------------------
# # __dict__ -> returns dictionary
# keys = names of object attributes
# values = values of object attributes
# print(v.__dict__)
# print(v.__dict__['x'])

#---------------------
# modify object attributes using __dict__ dictionary
# v.__dict__['x'] = 17
# print(v.x)

#---------------------
# delete object attributes using __dict__ dictionary
# del v.__dict__['x']
# print(v.x)
# print(v)
# print('x' in v.__dict__)
# print('y' in v.__dict__)

#---------------------
# insert object attributes using __dict__ dictionary
# v.__dict__['x'] = 22
# print(v.x)
# print(v)
# v.__dict__['z'] = 42
# print(v.z)
# print(v)

# in generall, do not use __dict__ directly
# but rather use built-in functions

#---------------------
# hasattr() -> return whether the object has an attribute with the given name.
# print(hasattr(v, 'x'))

#---------------------
# getattr() -> get a named attribute from an object
# print(getattr(v, 'x'))
# print(getattr(v, 'q')) # if attribute does not exists, raise AttributeError

#---------------------
# setattr() -> sets the named attribute on the given object to the specified value.
# if name does not exists, then it will be created
# setattr(v, 'x', 100)
# print(v.x)
# setattr(v, 'q', -1)
# print(v.q)

#---------------------
# delattr() -> deletes the named attribute from the given object.
# delattr(v, 'q')
# delattr(v, 'z')
# delattr(v, 'z') # if attribute does not exists, raise AttributeError


#---------------------
# Dynamic Attributes

# what to do, if we want to have dynamic vector attributes
# Vector(x=2, y=4), Vector(p=3, q=5), Vector(v=1, u=6), ...

#---------------------
# Version 2

# from vector import Vector

# v = Vector(a=1, b=5, c=8)
# print(v)
# print(dir(v))
# print(v.a)
# print(v.b)
# print(v.c)

# what is we want to have the Vector class to by immutable
# meaning, you cannot change the attributes once object is created

# option 1 - provide _ version of attributes and only property getters on attributes
# this only works for fixed names of attributes
# as the property getter must be named at the class definition time, not at object instantiation time

# option 2 - fake the existence of attribute for read access
# we can use __getattr__() method -> invoked AFTER failed attribute lookup
# rather do not use (only if you must) __getattribute__(), this is invoke BEFORE attribute lookup

#---------------------
# Version 3

# from vector import Vector

# v = Vector(a=1, b=5, c=8)
# print(dir(v))
# print(v._a)
# print(v.a)
# v._a = 7
# print(v._a)
# print(v.a)
# we can still assign to a, because Python will create it in case it doesnot exists :-)
# this also creates a mismatch between _a and a
# v.a = 17
# print(v._a)
# print(v.a)
# print(dir(v))

#---------------------
# Version 4
# make all attributes read-only

# from vector import Vector

# v = Vector(a=1, b=5, c=8)
# print(dir(v))
# print(v._a)
# print(v.a)
# v._a = 7

# print(v.x) # -> raises RecursionError -> maximum recursion depth exceeded

#---------------------
# Version 5
# preventing unwanted reccursion, when asking for attribute which does not exist directly or as _ version

# from vector import Vector

# v = Vector(a=1, b=5, c=8)
# print(dir(v))
# print(v.a)
# print(v._a)
# print(v.x) # now raises AttributeError as intended


#---------------------
# Version 6
# preventing attribute deletion
# just to demonstrate, as it is normally rare you need to prevent deletion

# from vector import Vector

# v = Vector(a=1, b=5, c=8)
# print(dir(v))
# delattr(v, "a")
# del v._a


#---------------------
# Version 7
# customizing attribute storage

# we can store attributes in any way, must not be dictionary

# from vector import ColoredVector

# cv = ColoredVector(red=20, green=120, blue=155, a=1, b=5, c=8)
# print(dir(cv))
# print(cv.red)
# print(cv.green)
# print(cv.blue)
# print(cv.a)
# print(cv.b)
# print(cv.c)
# cv.red = 200
# print(cv.red)
# print(cv)
# __repr__ NOK -> ColoredVector(a=1, b=5, c=8, color=[200, 120, 155])
# __repr__ OK -> ColoredVector(red=200, green=120, blue=155, a=1, b=5, c=8)

# The Version 7 is only for demonstration, not really to be used as the inheritance is not preffered in this case
# inheritance from Class which was not designed as base class
# instead of inheritance in this case, better would be composition = passing Vector to initializer of ColoredVector as argument



#---------------------
# vars() - return dictionary corresponding to the current local symbol table
# without args, vars() acts like locals()
# with argument it returns __dict__ attribute for mudule, class, instance, or any other object with __dict__ attribute
# vars(obj) == obj.__dist__
# vars(obj) is more Pythonic :-)
# it is stylistic prefference, what is more understandable for you
# self.__dict__["_color"] = [red, green, blue]
# vars(self)["_color"] = [red, green, blue]

#---------------------
# intercepting attributes
# __getattribute__ -> calls on each attribute access using . syntax -> object.attribute
# should not be required to use it ever


# from vector import ColoredVector
# from loggingproxy import LoggingProxy

# cv = ColoredVector(red=20, green=120, blue=155, a=1, b=5, c=8)
# cw = LoggingProxy(cv)
# cw.a
# cw.red = 40
# cw.a = 40

# __getattribute__ is not triggered by built-in protocols like repr(), len(), iter(), etc. -> bypass __getattribute__ for performance reasons
# if you use object.__repr__() syntax it triggers __getattribute__
# so LoggingProxy forwards it to passed object
# but if you use repr() call, this one is not trigerring __getattribute__
# so you would need to also provide custom __repr__ in LoggingProxy to forward it to passed object
# print(repr(cw))

#----------------------------------------
# Class internals
#----------------------------------------

# from vector import Vector

# v = Vector(a = 5, b = 6)
# print(v.__dict__)
# where are methods ???
# {'_a': 5, '_b': 6}

# methods are in dictionary of class, not object (class instance)
# print(v.__class__.__name__)
# print(v.__class__.__dict__)
# print(type(v.__class__.__dict__))
# <class 'mappingproxy'>
# mappingproxy does not allow direct modification like __dict__ on object
# Can call methods from class __dict__ directly
# print(v.__class__.__dict__["__repr__"](v))
# same as above
# print(vars((type(v)))["__repr__"](v))

# print(getattr(v, "__repr__"))
# # <bound method Vector.__repr__ of Vector(a=5, b=6)>
# print(getattr(v.__class__, "__repr__"))
# # <function Vector.__repr__ at 0x000001F4A616A0C0>

# Vector.x = 5
# print(Vector.x)
# print(v.x)

# def inject_function(self, value):
#     print("Injected :", value)


# v.__class__.__dict__['inject_function'] = inject_function
# TypeError: 'mappingproxy' object does not support item assignment
# instead setattr
# setattr(v.__class__, 'inject_function', inject_function)
# print(v.__dict__)
# print(v.__class__.__dict__)

# v.inject_function(10)


#---------------------
# Simplified Attribute lookup algorithm


# class Object:
#     """
#     This code is ilustrative. The real Object class and its methods are implemented in C
#     """
#     def __getattribute__(obj, name):
#         # get a class of a object
#         cls = type(obj)
#         # check if the name exists in __dict__ of object
#         if name in vars(obj):
#             return vars(obj)[name]
#         # check if the name exists on the class (including searching base classes in __mro__ order)
#         if hasattr(cls, name):
#             return getattr(cls, name)
#         # if the class defines __getattr__, call it
#         if hasattr(cls, "__getattr__"):
#             return cls.__getattr__(obj, name)
#         raise AttributeError(f"{cls.__name__} object has no attribute {name}")


#----------------------------------------
# Optimizing memory usage with slots
#----------------------------------------

# import sys

# class TestSlots:
    
#     # when using __slots__, __dict__ will no longer exists (replaced???)
#     __slots__ = ["value1", "value2", "value3", "value4"]

#     def __init__(self, value1, value2, value3, value4):
#         self.value1 = value1
#         self.value2 = value2
#         self.value3 = value3
#         self.value4 = value4

# ts = TestSlots("1", "22", "333", [1, 2, 3, 4, 5, 6, 7, 8])


# print(sys.getsizeof(ts) + sys.getsizeof(ts.__dict__)) # 352
# print(sys.getsizeof(ts)) # 64
# print(sys.getsizeof(ts.value1))
# print(sys.getsizeof(ts.value2))
# print(sys.getsizeof(ts.value3))
# print(sys.getsizeof(ts.value4))

# when using __slots__, adding new attributes dynamically is no longer possible
# ts.value1 = 30
# print(ts.value1)
# #ts.valueX = 50
# print(ts.__slots__)
# print(dir(ts))
# print(type(getattr(ts, "__slots__")))
# print(ts.__slots__[1])


#----------------------------------------
# Messing arround

# class Vector:
#     """A two dimensional vector."""

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"{type(self).__name__}({self.x}, {self.y})"

# v = Vector(1, 2)
# Vector.__init__(v, 1, 3)
# print(Vector.__mro__)
# print(Vector.__name__)
# print(type(v).__name__)
# print(v.__dict__)
# v.__dict__['z'] = 5
# print(v.__dict__)
# print(v.z)
# print(vars(v))

# print(Vector.__dict__)

# def inject_print(self):
#     print(self.x)
#     print(self.y)
#     print(self.z)

# Vector.__dict__['inject_print'] = inject_print

# print(v.__class__.__dict__['__repr__'](v))


#----------------------------------------
# Descriptors
#----------------------------------------
# A descriptor is what we call any object that defines __get__(), __set__(), or __delete__().
# Optionally, descriptors can have a __set_name__() method.

# __get__(self, instance, owner)
# --
# self = descriptor object
# instance = object from which descriptor was retreived
# owner = class to which descriptor is bound
# --
# so for pluto.radius_metres => Positive.__get__(Planet.__dict__["radius_metres"], pluto, Planet)
# Planet.__dict__["radius_metres"] -> is not triggering descriptor protocol

# __set__(self, instance, value)
# self = descriptor object
# instance = object from which descriptor was retreived
# value = value
# so for pluto.radius_metres = 10 => Positive.__set__(Planet.__dict__["radius_metres"], pluto, 10)

# __delete__()

# __set_name__(self, owner, name)
# is called at the time the owning class is created, to let te descriptor instance to know its name
# self = descriptor object
# owner = class to which descriptor is bound
# name = name of the descriptor in the owning class = "attribute" name in the owning class

# from solar_system import *

# mercury, venus, earth, mars = inner_planets()

# print(Planet.__dict__["radius_metres"]._instance_data)
# print(dict(Planet.__dict__["radius_metres"]._instance_data))

# del venus
# # auto removed from WeakKeyDictionary
# print(dict(Planet.__dict__["radius_metres"]._instance_data))


# Retrieve descriptor object via owning class doesnot work
# mercury, venus, earth, mars = inner_planets()

# next invokes __get__ using None as instance parameter
# Positive.__get__(Planet.__dict__["radius_metres"], None, Planet)
# print(Planet.radius_metres)

#----------------------------------------
# data                  vs. non-data descriptors
# has only __get__          has __get__ and __set__ or __delete__
# read only                 writeable
# 

# from precedence import *

# obj = Owner()

# # data descriptor a
# obj.a
# obj.__dict__["a"] = "instance-data"
# # a is data descriptor and takes precedence over instance attribute
# obj.a

# # non-data descriptor b
# obj.b
# obj.__dict__["b"] = "instance-data"
# # b instance attribute takes precedence over non-data descriptor
# print(obj.b)

