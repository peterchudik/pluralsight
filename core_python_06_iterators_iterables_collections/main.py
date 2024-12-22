# -----------------------------------------------
# basic iterator for iterable
# -----------------------------------------------

# iterator is an object which allow us to iterate through iterable
# iterators in pyhon are forward iterators
# create iterator object on iterable using iter()

# my_iterator = iter([1,2,3,4,5])


# calling build in function next allow us to retreive elements from iterable
# exeption StopIteration is raised when iterable is exhausted

# while True:
#     try:
#         item = next(my_iterator)
#         print(item)
#     except StopIteration:
#         print("No more items")
#         break

# creating iterables examples
# there are multiple ways how to create iterables

# way 1: creating collections

# iterable_list = [1,2,3,4,5]
# iterable_tuple = ("orange", "banana", "apple")
# iterable_dict = dict(a = "alpha", b = "bravo", c = "charlie")

# way 2: defining generator by function of expresion

# def generator_function():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# generator_expresion = (x*x for x in range(10))

# we can define our own both iterator and iterable objects

# class MyIterable:
#     def __iter__(self):
#         return iterator

# class Iterator:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return next_item
#         # or
#         raise StopIteration

# -----------------------------------------------
# implement our own iterator
# -----------------------------------------------

# just for debuging here. which anywy should not happen here
# from tree_iterators import _is_perfect_length
# from tree_iterators import *

# print({i : _is_perfect_length(["x"]*i) for i in range(0, 32)})

# -----------------------------------------------
# # Ordering iterator - Level Order

# my_list = ["1", "2", "+", "-", "5", "6", "*"]
# iterator = LevelOrderIterator(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# my_list = ["H", "e", "l", "l", "o"]
# iterator = LevelOrderIterator(my_list)
# print(" ".join(iterator))

# -----------------------------------------------
# Ordering iterator - Pre Order

# expr_tree = "* + - a b c d".split()
# print(expr_tree)

# iterator = PreOrderIterator(expr_tree)
# print(" ".join(iterator))

# -----------------------------------------------
# Ordering iterator - In Order

# expr_tree = "* + - a b c d".split()
# print(expr_tree)

# iterator = InOrderIterator(expr_tree)
# print(" ".join(iterator))


# -----------------------------------------------
# Filtering iterator

# expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
# iterator = SkipMissingIterator(expr_tree)
# print(list(iterator))

# iterator is also iterable
# so we can pass it as input to another iterator

# iterator = SkipMissingIterator(InOrderIterator(expr_tree))
# print(" ".join(iterator))


# -----------------------------------------------
# Transforming iterator

# translating_table = {
#     "-": "minus",
#     "+": "plus",
#     "*": "multiplied by",
#     "/": "divided by"
# }

# m = missing

# expr_tree = [
#                "-",
#        "*",            "/",
#    "p",     "q",   "r",     "+",
#   m,  m,   m,  m, m,  m,  "s","t"
# ]

# iterator = Translationterator(translating_table, SkipMissingIterator(InOrderIterator(expr_tree)))
# print(" ".join(iterator))


# some usefull iterators are impemented in pythos standart itertools library

# -----------------------------------------------
# Iterables

# my own iterable
# tree = PerfectBinaryTree("+ * / u v w x".split())

# # we can create our own iterator for it
# iterator = iter(tree)
# print(iterator)
# # and the iterate using iterator
# print(next(iterator))
# print(next(iterator))

# # we can use itarable in any place where it is accepted
# # when use like below, our iterators are created behind the scene
# # StopIteration is handled for us
# print(" ".join(tree))
# for item in tree:
#     print(item)


# -----------------------------------------------
# Alternative iterable protocol

# __getitem__

# class MyAlternativeIterable
#   ...
#   def __getitem__(self, index):
#       if index > self-number_of_items():
#           raise IndexError
#       return self.get_element_at(index)

# to make it work with iterator protocol
# it must return value for consequtive integer indexes starting with 0
# if index is out of itarable range, it must raise IndexError

# from rational_range import RationalRange

# r = RationalRange(2, 4, 7)
# for item in r:
#     print(item)

# iterator = iter(r)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# print([float(item) for item in r])
# print(sum(r))


# -----------------------------------------------
# Extended iter() form

# iterator = iter(
#     callable,  # zero argument callable invoked once each iteraton
#     sentinel   # iteration ends when callable produce this value
# )

# read file until END is reached

# with open("end_terminated_file.txt", 'rt') as f:
#     lines = iter(lambda: f.readline().strip(), "END")
#     readings = [int(line) for line in lines]

# print(readings)

# infinite iterator for timespamps and free disk space

# from pathlib import Path
# cwd = Path.cwd()

# from shutil import disk_usage
# def free_space():
#     return disk_usage(cwd).free

# free_space_readings = iter(free_space, None)

# from datetime import datetime

# timestamps = iter(datetime.now, None)

# from time import sleep

# i = 0
# for timestamp, free_bytes in zip(timestamps, free_space_readings):
#     print(timestamp, free_bytes)
#     sleep(1)
#     i += 1
#     if i == 5:
#         print("End")
#         break


# -----------------------------------------------
# collection protocols
# -----------------------------------------------

# Protocols
# Container -> "in" and "not in" operators
# Sized -> len() for number of elements
# Iterable -> produce iterator with iter()
# Sequence -> retreive element by index : seq[index]
#          -> find item by value : index = seq.index[item]
#          -> count items with particular value : num = seq.count(item)
#          -> produce reversed sequence t = reversed(seq)
# Set -> set algebra protocols subst, superset, union, intersection, ...
# Mapping -> Associate hashable keys with values : mapping[key] = value, value = mapping[key]


# -----------------------------------------------
# lets build SortedFrozenSet
# A collection which is sized, iterable, sequence container of distinct items,
# and constructible from iterable
# -----------------------------------------------

# Using Test Driven Development
# 1. Test    -> Write test and let it fail, as no code yet
# 2. Code    -> Write code
# 3. Improve -> Refactor 


# -----------------------------------------------
# Container protocol :
# delegates to special method __contains__
# fallback to the iterable protocol (as itarable protocol supports in/not in)


# -----------------------------------------------
# Sized protocol :
# len() function must not consume or modify collection
# delegates to special method __len__ of a object passed to it


# -----------------------------------------------
# Iterable protocol :
# iter(iterable)
# delegates to special method __iter__ of a object passed to it
# fallback to alternative iterable protocol __getitem__

# -----------------------------------------------
# Sequence protocol :
#
# Get item by index
# seq.[index] - delegates to __getitem__
#
# Slicing
# slicing -> items = seq[x:y] - is optional
# seq[start:stop] -> stop is excluding
# seq[start:stop:step] -> default step is 1
# seq[:stop] -> from beginning
# seq[start:] -> until end
# seq[:] -> full slice - usefull for copying sequence
# 
# Reversed
# Produce reverse iterator r = reversed(sequence)
# delegate to __reversed__
# fallback to __getitem__(index) and __len__() if supported 
#
# find item index by item value
# index = s.index(item)
# index() is regular method
#
# Count items with particular value
# num = seq.count(item)
# count() is regular method
#
# Optional extensions of sequence protocol
# for mutable and imutable sequence:
# concatenation = __add__ ad __radd__
# repetition = __mul__ and __rmul__
# for mutable sequences:
# In-place concatenation = __iadd__
# In-place repetition = __imull__
# In-place append, extend, insert, pop, reverse, remove, sort



# -----------------------------------------------
# Hashable protocol :
# hashable object can be passed to build in hash(hashable) function
# hash() function will return an integer hash code
# hashable object can be used in dictionary as key, or as set element
# Objects which are value equality comparable should be hashable
# __hash__() method to implemet Hashable protocol
# Mutable objects should disable hashable protocol by setting __hash__ = None
# equal objects must return same hash code
# unequal objects may return different hash code


# SortedFrozenSet class inherits from
# Sequence
#   Reversible
#   Collection
#       Container
#       Sized
#       Iterable
# 
# the index() method from Sequence, does not know, that our class has sorted items
# the count() method from Sequence, does not know, that our class has unique items
# both have O(n) complexity
# we can overide these and implement it with O(log n) complexity


# -----------------------------------------------
# improving performance of SortedFrozenSet
# -----------------------------------------------


# from itertools import islice
# from recaman import recaman
# from frozen_sorted_set import SortedFrozenSet

# # from first 1000 numbers of recaman sequence get those which are less then 1000
# s = SortedFrozenSet(r for r in islice(recaman(), 1000) if r < 1000)
# print(len(s))
# print(s)

# # show all less then 1000 in 1000 liat as 1
# # use SortedFrozenSet count() method, inhereted fro abc.Sequence
# print([s.count(i) for i in range(1000)])

# from timeit import timeit

# print(timeit(
#     setup="from __main__ import s",
#     stmt="[s.count(i) for i in range(1000)]",
#     number=2000
# ))


# -----------------------------------------------
# Collections Abstract Base Classes
# -----------------------------------------------

# When removing inheritance from Sequence, all tests will pass
# because we overwritten all the protocol methods we are using

# When keeping inheritance from, we can do simple checks using isinstance()
# if our class support certain protocols

# from collections.abc import *

# # is built-in list supporting Sequence protocol
# print(issubclass(list, Sequence))
# print(issubclass(list, Sized))
# print(issubclass(dict, Mapping))
# print(issubclass(dict, Sequence))


# It is encouradged, but not a must, to inherit from ABC
# It has some advantages, such as default methods implementations
# and ability to distinguisch between similar colection types, such as 
# sequences and mappings
# PEP 3119


# -----------------------------------------------
# collection protocols - set protocol
# -----------------------------------------------
# Special methods
# __le__ - <= - issubset     - subset
# __lt__ - <  -              - proper subset
# __eq__ - >= -              - equal
# __ne__ - != -              - not equal
# __gt__ - >  -              - proper superset
# __ge__ - >= - issuperset   - superset
#             - isdisjoint   - disjoint
# Set algebra operators
# __and__ - & - intersection
# __or__  - | - union
# __sub__ - - - difference
# __xor__ - ^ - symmetric_difference
#
# infix methods support is provided by abc.Set + named method isdisjoint
# named method has to be provided by built-in set
# infix operators only support same type on lhs and rhs
# named functions support any iterable

# For exercise - create mutable version of SortedFrozenSet
