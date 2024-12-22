# ---------------------------------------------
# Introspecting types
# ---------------------------------------------

# --------------------
# type()

# i = 7
# print(type(i))
# print(int)
# print(repr(int))
# print(type(i) == int)
# # call constructor on a type return value directly
# j = type(i)(78)
# print(type(j))
# print(j)
# print(type(type(i)))

# # type() returns __class__ attribute
# print(i.__class__)
# print(i.__class__.__class__)
# print(i.__class__.__class__.__class__)

# --------------------
# issubclass()
# determines, if 1st argument is subclass ob 2nd
# 2nd argument can be single class or tuple os classes (checks any)

# print(issubclass(type, object))
# print(type(object))

# --------------------
# isinstance()
# determines if 1st argument is instance of 2nd argument (class)
# 1st argument can be an object of any type
# 2nd argument can be single class or tuple os classes (checks any)

# i = 7
# print(isinstance(i, int))


# ---------------------------------------------
# Introspecting objects
# ---------------------------------------------

# --------------------
# dir()
# return a list of attribute names for an instance
# returned list has both attributes names and method names

# a = 42
# print(dir(a))

# --------------------
# getattr(object, attribute_name)
# retrieve corresponding attribute object

# print(getattr(int, 'numerator'))
# print(getattr(int, 'denominator'))
# # attributes
# a = 42
# print(getattr(a, 'numerator'))
# print(getattr(a, 'denominator'))
# print(a.numerator)
# print(a.denominator)
# # methods
# print(getattr(a, 'conjugate'))

# --------------------
# callable()
# Return whether the object is callable

# print(callable(getattr(a, 'conjugate')))

# --------------------
# hasattr()
# Return whether the object has an attribute with the given name.

# print(hasattr(a, 'conjugate'))
# print(hasattr(a, 'index'))

# print(a.conjugate.__class__)
# # class objects store their name in __name__ attribute
# print(a.conjugate.__class__.__name__)

# generally preffered is EAFP style in Python, LBYL is not considered to by Pythonic
# this means, catch AttributeError, do not check before if object has an attribute
# this way you get more informations also from original object which is not having the called attribute


# ---------------------------------------------
# Introspecting scopes
# ---------------------------------------------

# --------------------
# globals()
# Return the dictionary containing the current scope's global variables.

# print(globals())
# a = 42
# print(globals())
# globals()['test'] = 6.3
# print(globals())
# print(test / 2)

# --------------------
# locals()
# Return a dictionary containing the current scope's local variables.

# print(locals())

# def report_locals(arg):
#     from pprint import pprint as pp
#     x = 123
#     pp(locals(), width=10)

# report_locals(42)

# unpacking the local namespace
# name = 'John'
# age = 20
# country = 'New Zealand'
# # extended call syntax ** allow us to unpack dictionary into functions kwargs
# # str.format() accepts keyword arguments
# print("{name} is {age} years old and is from {country}.".format(**locals()))

# # PEP 498 - f-strings
# # f-strings interpolate names from namespaces directly
# print(f"{name} is {age} years old and is from {country}.")


# ---------------------------------------------
# Inspect module
# ---------------------------------------------

# import batch
# import inspect

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# batch = Batch(list1)
# batch.append(list2)

# for item in batch:
#     print(item)

# --------------------
# ismodule()
# Return true if the object is a module.
# print(inspect.ismodule(batch))

# --------------------
# getmembers()
# Return all members of an object as (name, value) pairs sorted by name
# Optionally, only return members that satisfy a given predicate.

# print(inspect.getmembers(batch))
# print(dir(inspect))
# print(inspect.isclass)
# print(inspect.getmembers(batch, inspect.isclass))

# retrieving all functions of a class
# print(inspect.getmembers(batch.Batch, inspect.isfunction))

# inspect function parameters
# init_sig = inspect.signature(batch.Batch.__init__)
# print(init_sig.parameters)
# print(init_sig.parameters['iterable'])
# print(init_sig.parameters['iterable'].name)
# print(init_sig.parameters['iterable'].default)


# ---------------------------------------------
# Obect introspection tool
# ---------------------------------------------
# from introspector import dump

# x = 42
# dump(x)


