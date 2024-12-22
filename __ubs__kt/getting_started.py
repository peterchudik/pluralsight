# -------------------------------------------------------
# Python Big Picture
# -------------------------------------------------------
# Easy to learn and read
# Only 1 way to solve problem
# Focus on simplicity
# Focus on beauty
# Great community - countless python libraries, great tools, PEPs
# PEPs - proposing new features, collecting imput and documenting new features
# Hgh popularity and demand (PYPL - https://pypl.github.io/PYPL.html)
# Used in many areas -> Web development, Data science, Education and learning, Scripting
# Web development -> API - Flask, Website - Django
# Data science -> Big Data, Machine learning
# Education - Jupiter notebooks
# Scripting

# What is Python
# Unique syntax -> beutifull is better then ugly, Readability counts
#  Uses colons (:) and significatn whitespaces
# General purpose - can be use in many areas
# High level language
# Multi paradigm
# -> supports structured programming (IF..THEN, LOOPS, Procedures, Functions, Methods)
#   -> object oriented programming
#   -> functional programming
# Interpreted language - do not need to compile Python program
# Garbage collected
# Dynamically typed
# -> no need for type declarations
# -> support for type hints PEP 483 and PEP 484
# -> same variable different types, type chacking at runtime (TypeError)
# -> dynamic typing enables bahaviour called Duck Typing
# Duck Typing = If it walks like a duck, and it quacks like a duck, it must be duck!
# -> Duck typing means, you can pass any objects into function, as long as it behavies the way function expects it and needs it to.
#   -> the code itself does not care about whether an object is a duck, but instead it does only care about whether it quacks.
# code example of duck typing

# class Duck:
#     def quack(self):
#         print("Quack!")

# class Person:
#     def quack(self):
#         print("I am person. Quack!")

# def quack(f):
#     f.quack()

# quack(Duck())
# quack(Person())

# Python Pros
# Comprehensive standard library -> https://docs.python.org/3/library/index.html
# Community driven
# -> PEP process (PEP - Python Enhancements Proposal)
# -> Comprehensive documentation
# -> Release notes -> https://docs.python.org/3/whatsnew/3.11.html
# 3rd party libraries - PIPY (Python Package Index) -> https://pypi.org/
# -> install libraries using pip.exe (pip install <package_name>)
# 3rd party tools
# -> Python IDEs (PyCharm, Visual Studie Code)
# -> Python editors (Sublime, Vim, Emacs), 
# -> Code analysis - PyLint
# -> Code formatter - black
# -> Stype guide enforcement - flake8
# -> Performance analysers

# Python Cons
# Interpreted -> slow
# No Native -> high memory usage
# Dynamic -> runtime errors rather at compiling



# -------------------------------------------------------
# Installing and starting python
# -------------------------------------------------------

# 2 Versions of Python - Python 2 legacy, Python 3 to be used

# Download Python - https://www.python.org/

# ------------
# REPL
# Python command line enviroment = REPL (Read Evaluate Print Loop)
# Interactive Python session - good for quick interactions, checks, testing, etc.

# ------------
# Some commands for REPL

# print("Hello World")
# 2 + 2
# 4 * 2

# Exit REPL -> quit(), or CTRL-Z + Enter

# ------------
# Significant whitespace
# start of new block :
# each new block must be intended by 4 spaces (or tab), preferable spaces
# never mix spaces and tabs

# show example in REPL with simple for loop
# for i in range(5):
#     print(i)

# Development of Python is managed throught 
# PEP - Python Enhancements Proposal
# PEP 8 - Style guide for Python
# PEP 20 - Zen of Python - in REPL can be accesses by import this


# ------------
# Python standart library

# ------------
# import keyword

# Example (at REPL)
# import math
# print(math.sqrt(81))
# print(math.floor(10.4) )
# print(math.factorial(5))

# ------------
# get help on library

# help(math)
# help(math.factorial)

# ------------
# different import variants

# import math
# n = 5
# k = 3
# print(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

# from math import factorial
# print(factorial(n) / (factorial(k) * factorial(n-k)))

# from math import factorial as f # use it carefully
# print(f(n) / (f(k) * f(n-k)))

# no limitation in large numbers for Python

# print(factorial(100))
# print(len(str(factorial(100))))


# -------------------------------------------------------
# Scalar types
# -------------------------------------------------------

# ------------
# int -> unlimited precision signed integers

# specified as decimal
# print(10)
# specified as binary (0b prefix)
# print(0b10)
# specified as octal (0o prefix)
# print(0o10)
# specified as hexadecimal (0x prefix)
# print(0x10)
# int() constructor - int is object with consructor
# print(int(3.5))
# print(int(-3.5))
# print(int("456"))
# print(int("10000", 3))

# ------------
# float - 64 bit floating point numbers

# print(3.125)
# scientific notation
# print(3e8)
# print(1.656e-65)
# float() constructor
# print(float(7))
# print(float("nan")) # nan = not a number
# print(float("inf")) # positive infinity
# print(float("-inf")) # negative infinity
# int + float is float
# print(3+10.2)
# print(type(3+10.2))

# ------------
# Null value = None - represent absence of value

# print(None)
# a = None
# if a is None:
# 	print("Is None")

# ------------
# Bool - logical values

# print(True)
# print(False)
# guess bool type of objects
# integers
# print(bool(0))
# print(bool(42))
# print(bool(-1))
# floats
# print(bool(0.0))
# print(bool(42.1))
# print(bool(-1.1))
# collections
# print(bool([]))
# print(bool([1, 2, 3]))
# print(bool(""))
# print(bool("Spam"))
# print(bool("True"))
# print(bool("False"))


# -------------------------------------------------------
# Relational operators
# -------------------------------------------------------

# ------------
# ==, !=, <, >, <=, >=
# return bool value
# used to comparing any objects

# g = 10
# print(g==10)
# print(g==20)

# if 2 == 2.0:
# 	print("True")


# -------------------------------------------------------
# Control flow
# -------------------------------------------------------

# ------------
# IF statements

# h = 9
# if h > 50:
#     print("Greater than 50")
# elif h >= 20:
# 	print("Between 20 and 50")
# elif h >= 10:
# 	print("Between 10 and 19")
# else:
#  	print("Less then 10")

# -------------------------------------------------------
# While Loops
# -------------------------------------------------------

# c = 5
# while c != 0:
# 	print(c)
# 	c -= 1 # augmented assigment operator
# shorter version, not recommended, explicit is better than implicit
# c = 5
# while c:
# 	print(c)
# 	c -= 1

# Infinite loops
# while True:
# 	response = input()
# 	if int(response) % 7 == 0: # modulus operator
# 		break

# -------------------------------------------------------
# Strings, collections and Iteration
# -------------------------------------------------------

# ------------
# strings have datatype str
# str is immutable - once its constructed, it cannot be modified
# str is sequence of unicode code points

# Single quotes
# print('This is string')
# Double quotes
# print("This is string")
# Advantage is you can avoid escaping in the text
# Combined
# print('This "is" string')
# print("This 'is' string")
# Automatically concatenated by python into single string
# a = "first" "second"
# print(a)
# Multiline strings usimg """
# a = """This
# is
# my
# string"""
# print(a)
# Multiline strings usimg new line character \n
# \n is universal multiline, same for Windows, Unix, etc. -> PEP 278
# a = "This\nis\nmy\nstring"
# print(a)

# ------------
# \ -> escape character

# print("This \"is\" string")
# print("This \"is\" string \\")
# print("This \"is\" string \\")

# ------------
# raw string - to avoid many excape characters

# path = r'c:\nxxx\nddd'
# print(path)

# use str constructor, o create string from other data types

# a = str(19)
# print(a)
# print(type(a))

# strings are sequences types, supporting some sequence operations

# s = 'string'
# print(s[2]) # returns new string
# print(type(s))
# print(type(s[2]))

# str is a class and has multiple named methods
# list the methods on the class using help
# help(str)

# c = 'oslo'
# print(c.capitalize()) # () to call method
# print(c.count('o'))
# print(c) # still lower case, as capitalize method is returning new str object

# ------------
# bytes
# similar to string, but is sequence of bytes

# bytes can be constructed using b"" or b''
# print(b'data data')
# print(b"data data")

# a = b'data data'
# print(a)
# print(a[0]) # integer value of specified byte
# print(a.split()) # return the list of bytes objects

# ------------
# to convert between str and bytes
# use
# encode str -> byte
# decode byte -> str

# name = 'olafhladj'
# data = name.encode('utf8')
# print(name)
# print(data)
# name_back = data.decode('utf8')
# print(name_back)
# if name == name_back:
# 	print('Yes')


# ------------
# list
# sequence of objects
# mutable - means you can change existing list object

# list of numbers
# a = [1, 2, 3]
# print(a)

# list of characters
# a = ["1", "2", "3"]
# print(a)

# list by index
# print(a[0])
# print(a[1])
# print(a[2])

# modify at index
# a[0] = "Start"
# print(a)

# create empty list
# a = []
# print(a)

# list object methods
# help(list)
# a = [1, 2, 3]
# a.append(4)
# print(a)

# list constructor
# print(list('characters'))
# a = [
#     1,
#     2,
#     3,
#     4, # can use comma after last element
# ]
# print(a)


# ------------
# dict - dictionary
# key value pairs
# {k1 : v1, k2: v2}

# a = {'name': 'Tom', 'city': 'Zurich', 'country': 'Switzerland'}
# print(a)

# retreive value by key
# print(a['city'])

# update value by key
# a['city'] = 'Basel'
# print(a)

# add new key value pair
# a['Canton'] = 'Basel'
# print(a)

# empty dictionary
# b = {}
# print(b)


# ------------
# for loops
# for item in iterable:
#	... body...

# cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
# for city in cities:
#     print(city)

# my_dict = {'name': 'Tom', 'city': 'Zurich', 'country': 'Switzerland'}
# for key in my_dict:
#     print(key, my_dict[key]) # print can accept multiple arguments

# for c in list('characters'):
# 	print(c)

# ------------
# Putting it together

# Read all the words from file into list

# f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
# file_words = []
# for line in f:
#     line_words = line.split()
#     for word in line_words:
#         file_words.append(word)
# f.close()
# print(file_words)


# -------------------------------------------------------
# Modularity
# -------------------------------------------------------

# ------------
# Modules

# running python module -> python filename
# python words.py

# importing module (in repl or program)
# code is executed when imported
# Version 1 of words.py
# import words

# ------------
# defining function

# def square(x):
#     return(x * x)
# a = square(5)
# print(a)

# return is optional, but preffered
# def print_it(x):
#     print(x)
# print_it('Hallo World')

# early return and return None
# def even_or_odd(n):
#     if n % 2 == 0:
#         print("even")
#         return
#     print("odd")

# w = even_or_odd(6)
# print(w)
# print(w is None)

# special functions names
# __feature__

# Version 2 of words.py
# import words
# function in words module ends to be called explicitly
# words.fetch_words()

# from words import fetch_words
# fetch_words()

# when running Version 2 of words.py directly in command line nothing will happen
# function is not executed
# to be able to run a module as a scrip and also beeing able to import it
# we need to use __name__ variable
# __name__ let us identify, if module was executed as script or imported in another module


# Version 3 of words.py

# from words import fetch_words
# __name__ = 'words'
# when import again, it will not run again

# run as script
# __name__ = '__main__'


# Version 4 of words.py

# from words import fetch_words
# fetch_words()

# run as script

# general recomendation is to make your code to be importable and also run as script


# Version 5 of words.py - bit of code refactoring

# from words import fetch_words, print_words
# print_words(fetch_words())

# from words import * # not recommended
# words = fetch_words()
# print(words)
# print_words(["One", "Two", "Three"])
# main()

# ------------
# command line arguments

# Version 6 of words.py

# run as script with parameter

# import
# from words import main
# main('lorem_ipsum.txt')

# PEP 8 - 2 lines between function names

# ------------
# docstrings

# provides documentation
# works with help function
# docstring mus be first statements in block, such as module or function
# use tripple quotes""" - PEP 257
# tools like Sphinx can create htl documentation from Python docstrings
# we will be following google python style guide

# from words import fetch_words
# help(fetch_words)

# import words
# help(words)

# ------------
# comments
# to comment some code features to improve understanding
# start with #

# ------------
# shebang - #!
# on unix systems
# allows the program loader to identify which interpreter to use
#! usr/bin/env python
# typicaly env program is used to locate python on your path enviroment variable


# -------------------------------------------------------
# Objects and types
# -------------------------------------------------------

# ------------
# assiging a variable

# ------------
# Immutable objects
# x = 1000
# Python creates an int object with value of 1000
# Python creates an object refference with name x which references to the int object with value of 1000
# x = 500
# it wll not change then value if int(1000) objects (int objects is immutable)
# but rather create a new int(500) object and assigne reference of name x to it
# python garbage collector will delete int(1000), as there is no refference to it anymore
# y = x
# this assign new y refference to the existing int(500) object
# x = 3000
# creates new int(3000) objects and assign x reference to it
# int(500) still exists, as it is still reachable throught y reference

# id() returns an integer identifier of a object that is constant and unique for the life of an object
# a = 1000
# print(id(a))
# b = 500
# print(id(b))
# b = a
# print(id(b))
# print(id(a) == id(b))

# identity equality  - is - test whether two references refers to the same object
# print(a is b)

# t = 5
# t += 2
# what happens here?
# int(5) is created, t reference is assigned to int(5)
# int(2) is created
# int(5) and int(2) are added and int(7) is created
# t is assigned as reference to int(7) and int(5) and int(2) are gabage collected

# core rule -> assigment operator only assigns objects to names it never copies an object

# ------------
# Mutable objects
# r = [2, 4, 6]
# s = r
# s[1] = 17
# print(s)
# print(r)
# print(s is r)
# if you want to create a copy of a list, you need to do it differently


# ------------
# value vs identity equality

# p = [1, 2, 3]
# q = [1, 2, 3]

# value equality
# print(p == q)

# identity equality
# print(p is q)

# identity equality is how python behaves, you cannot influence ir
# value equality can be change programatically
# for example you can define how to compare you own classes


# ------------
# passing arguments and returning values

# m = [1, 2, 3]
# def modify(k):
#     k.append(39)
#     print("k = ", k)

# modify(m)
# print(m)

# if passing reference to a function, it creates new reference to the same object, it will not make a copy
# if you want a copy, than the function itself should take care of it

# f = [1, 2, 3]

# def replace(g):
#     g = [4, 5, 6]
#     print("g = ", g)

# replace(f)
# print(f)

# by passing f to function, we had g referencing the same list
# but inside function we constrcted new list and assigned g to it

# if you want to replace, need to be like this

# f = [1, 2, 3]

# def replace(g):
#     g[0] = 4
#     g[1] = 5
#     g[2] = 6
#     print("g = ", g)

# replace(f)
# print(f)

# same as arguments are transferred by "passed-by-object-refference"
# applies to return values


# def f(d):
#     return d
# c = [1, 2, 3]
# e = f(c)
# print(c is e) # returns same objects, no copy was made


# ------------
# function arguments

# argument with default values - must come after those without default value
# def banner(message, border='-'):
#     line = border * len(message)
#     print(line)
#     print(message)
#     print(line)
# banner('Compliance DWH')
# banner('Compliance DWH with stars', '*')

# first is positional argument, second is keyword argument
# banner('Compliance DWH with dots', border='.')

# we can also pass all as keyword arguments
# banner(border = '|', message = 'Compliance DWH with pipes')

# default value evaulation
# import time
# print(time.ctime())

# def show_default(arg = time.ctime()):
#     print(arg)
# show_default()
# time.sleep(1)
# show_default()
# time.sleep(1)
# show_default()
# why?
# def is statement, when executed, binds function definition to the function name
# default arguments are evaluated only when def stetement is executed = only once
# Immutable defult values works fine

# Mutale default values can cause confusing effects
# def add_to_list(list=[]):
#     list.append("New")
#     return list

# without using default, ok
# k = [1, 2, 3]
# print(k)
# k = add_to_list(k)
# print(k)

# with using default, confusing
# a = add_to_list()
# print(a)
# b = add_to_list()
# print(b)
# c = add_to_list()
# print(c)

# always use immutable objects as default values
# def add_to_list(list=None):
#     if list is None:
#         list = []
#     list.append("New")
#     return list

# with using default, now fine
# a = add_to_list()
# print(a)
# b = add_to_list()
# print(b)
# c = add_to_list()
# print(c)


# ------------
# python type system

# Python has dynamic type system - means, type of object reference is resolved at runtime
# does not need to be specified, when program is written

# def add(a, b):
#     return a + b

# a = add(1, 2)
# print(a)
# b = add(1.2, 2.2)
# print(b)
# c = add("A", "B")
# print(c)
# d = add([1, 2], [3, 4])
# print(d)
# e = add("The answer is ", 42)
# python will not perform implicit conversion between types


# ------------
# scopes
# type declarations are unnecessary in Python
# names can be rebound to objects of any type
# name resolution to objects is managed by scopes and scoping rules

# Python has 4 types of scopes
# Each scope is a context in which names are stored and can be looked up

# Local scope -> inside the current function
# Enclosing scope -> inside any and all enclosing functions
# Global scope -> at the top level of module. Each module brings with it a new global scope
# Built-in scope -> names bilt into Python language throught the special builtins module

# LEGB rule -> names are looked up in the narrowest relevant context

# Scopes are not defined by code blocks, for example FOR LOOPS do not introduce new scope

# global scope -> for example our words module contains following global names
# main, fetch_words, print_items -> bound by def
# urlopen and sys -> bound by import
# __name__ -> provided by Python runtime

# normaly global module scope contains names from function, classes, constants and variables

# Local scope -> in the fetch_words
# filename, f, file_words, line, line_words, word
# exists until function completes and then these references will be desroyed

# Rebind global name into a local namespace
# global keyword

# count = 0

# def show_count():
#     print(count)

# def set_count(c):
#     # global count
#     count = c

# show_count()
# set_count(5)
# show_count()


# ------------
# everyting is an object

# import words
# # type - return type of a object
# print(type(words))

# # dir - display attributes of an object
# print(dir(words))

# # inspect attributes
# print(type(words.fetch_words))
# print(dir(words.fetch_words))

# print(type(words.fetch_words.__name__))
# print(words.fetch_words.__name__)

# print(dir(words.fetch_words.__name__))
# print(words.fetch_words.__name__.upper())

#  # used by help() function
# print(type(words.fetch_words.__doc__))
# print(words.fetch_words.__doc__)


# -------------------------------------------------------
# Built-in collections
# -------------------------------------------------------

# ------------
# tuple - immutable sequence of arbitrary objects
# once tuple is created, objects cannot be replaced or removed and new elements cannot be added

# # tuple is defined using ()
# t = ("A", 3.5, 2)
# print(t)

# # access elements by zero based index
# print(t[0])
# print(t[1])
# print(t[2])

# # number of elements usinf built-in function len()
# print(len(t))

# # iterate over using FOR loop
# for i in t:
#     print(i)

# # concatenate tuple +
# a = t + ("a", 1)
# print(a)

# # repeat tuples using *
# a = t * 3
# print(a)

# # nested tuples
# a = ((1, 2), (2, 3), (3, 4))
# print(a)
# print(a[2][1])

# # single element tuple
# a = (2)
# print(type(a))
# a = (2,)
# print(type(a))

# # empty tuple
# a = ()
# print(type(a))

# # () are optional
# a = 1, 2, 3, 4, 5, 6
# print(type(a))
# print(a)

# def min_max(items):
#     return min(items), max(items)

# a = min_max([3, 5, 7, 1, 0, 9, 4])
# print(type(a))
# print(a)

# # tuple unpacking - destructuring operation, that unpacks data structures into named references
# lower, upper = min_max([3, 5, 7, 1, 0, 9, 4])
# print(type(lower))
# print(lower)
# print(type(upper))
# print(upper)

# (a, (b, (c, d))) = (1, (2, (3, 4)))
# print(a)
# print(b)
# print(c)
# print(d)

# # tuple unpacking can be used to swaping 2 or more variables
# a = 1
# b = 2
# a, b = b, a
# # first packs b, a on right side into tuple, then unpacks it on the left reusing the names and b
# print(a)
# print(b)

# # tuple constructor
# a = tuple([1, 2, 3])
# print(a)
# a = tuple("CDWH")
# print(a)

# # test for containment
# a = 1, 2, 3, 4, 5, 6
# print(1 in a)
# print(7 not in a)


# ------------
# string - immutable sequence of unicode code points

# # length of string
# a = len("Characters")
# print(a)

# # concatenatiion
# a = "Alt" + "stetten"
# print(a)
# a = "Ur"
# a += "dorf" # Strings are immutable, so each time new string object is created and old is garbage collected
# print(a)

# # Use join() method instead of +, far more efficient
# a = ";".join(["A", "B", "C"])
# print(a)

# # split() method
# a = a.split(";")
# print(a)

# # partition() method
# # Split string into 3 parts, (before , separator and after) -> returns tuple
# a = "unforgetable".partition("forget")
# print(a)
# start, separator, destination = "ZH:BS".partition(":") # tuple unpacking
# print(start)
# print(destination)
# start, _, destination = "ZH:BS".partition(":")
# # _ is not a special variable in Python, it is just unwritten convention for dummy values
# # _ is also supressed by many Python tools
# print(start)
# print(destination)

# # String formatting
# # format() method can be called on string containing {} replacament fields
# # format() arguments will be used to replace {} replacament fields

# # format() with positional arguments
# a = "My collegue {0} is {1} years old".format("Peter", "18")
# print(a)
# a = "My collegue {0} is {1} years old. His age is {1}".format("Peter", "18")
# print(a)
# a = "My collegue {} is {} years old".format("Peter", "18") # number of {} must much number of positional arguments
# print(a)

# # format() with keyword arguments
# a = "Currrent position {latitude} {longitude}".format(latitude = "47N", longitude = "8E")
# print(a)
# a = "Currrent position {pos[0]} {pos[1]}".format(pos = ("47N", "8E"))
# print(a)
# import math
# a = "Math constants pi = {m.pi} e = {m.e}".format(m = math)
# print(a)
# # format() formatting strings
# a = "Math constants pi = {m.pi:.3f} e = {m.e:.3f}".format(m = math)
# print(a)

# # PEP 498 - introduce f string formattig aiming for minimal syntax
# # instead
# value = 4 * 20
# a = "The value is {value}.".format(value = value)
# print(a)
# # f string
# # expressions inside {} are evaluated and inserted at runtime
# a = f"The value is {4 * 20}."
# print(a)
# # also function can be used inside {}
# import datetime, time
# a = f"The current time is {datetime.datetime.now().isoformat()}"
# print(a)
# time.sleep(1)
# print(a)
# import math
# a = f"Math constants pi = {math.pi} e = {math.e}"
# print(a)
# a = f"Math constants pi = {math.pi:.3f} e = {math.e:.3f}"
# print(a)

# # Other str methods -> help(str)

# ------------
# range() - sequence representing aritmetic progression of integers
# range(stop)
# range(start, stop)
# range(start, stop, step)
# argumets like these are normally ot possible
# kwargs are not supported

# for i in range(5):
#     print(i)
# print(list(range(0, 5)))
# print(list(range(5, 10)))
# print(list(range(10, 20, 2)))

# never use like this, very bad code :-) 
# s = [1, 2, 3, 4]
# for i in range(len(s)):
#     print(s[i])

# but like this
# s = [1, 2, 3, 4]
# for i in s:
#     print(i)

# if for some reason you need counter, you should use built-in enumerate() function
# enumerate() function - creates an iterable of (index, value) tuples around another iterable object
# from list [2, 4, 6, 10] creates list [(1, 2), (2, 4), (3, 6), (4, 10)]
# s = [2, 4, 6, 10]
# for i in enumerate(s):
#     print(i)
# we can use tuple unpacking to avoid to deal directly with tuple
# s = [2, 4, 6, 10]
# for i, v in enumerate(s):
#     print(f"index = {i}, value = {v}")


# ------------
# lists
# we already learned : [], [].append(), get value at index and modify at index

# negative indexes
# start from end, so -1 is at element
# s = [2, 4, 6, 10]
# print(s[-1])
# print(s[-2])
# print(s[0])
# print(s[-0])

# slicing
# list[start:stop]
# s = [2, 4, 6, 10]
# print(s[0:2])
# print(s[:3])
# print(s[3:])
# print(s[:]) # important idiom for copying a list
# print(s[1:-1]) # all except first and last

# copy list
# s = [2, 4, 6, 10]
# t = s[:]
# we get 2 indipendent lists, but only references to the list elements are copied
# this is important, because if list contains mutable objects, then modifying this will change both lists

# alternative to full slice idiom
# s = [2, 4, 6, 10]
# t = list(s) # this works with any itarable serie as argument, not only list, so prefered
# print(s is t)
# u = s.copy()
# print(u is t)

# all above copies produce shallow copies
# a = [[1, 2], [3, 4]]
# b = list(a)
# print(a)
# print(b)
# print(a[0] is b[0]) # same mutable objects, so modifying it will result in changes in both lists
# a[0][0] = 99
# print(a)
# print(b)
# a[1].append(99)
# print(a)
# print(b)
# to create a deep copy of such hierarchical data structures, we can use copy mudule in Python standart library

# multiplication *
# a = [1, 2]
# b = a * 3
# print(a)
# print(b)
# init list with given length
# a = [0] * 100
# print(a)
# be carefull again, since it will create list wwith references to the same objects
# a = [ [0, 0] ] * 10
# print(a)
# a[2].append(99)
# print(a)

# find an object in the list
# list.index()
# s = [2, 4, 6, 10]
# print(s.index(6))
# print(s.index(99)) # raises ValueError

# count an object in the list
# list.count()
# s = [2, 4, 6, 10, 6]
# print(s.count(6))

# test for membership - in, not in
# s = [2, 4, 6, 10, 6]
# print(2 in s)
# print(3 not in s)

# remove element at index from list
# del list[index]
# s = [2, 4, 6, 10]
# print(s)
# del s[0]
# print(s)

# remove element by value from list
# s = [2, 4, 6, 10]
# print(s)
# s.remove(10) # same as : del s[s.index(10)]
# print(s)
# s.remove(99) # raises ValueError

# insert elementat index into list 
# s = [2, 4, 6, 10]
# print(s)
# s.insert(1, 99)
# print(s)

# concatenate lists
# a = [1, 2]
# b = [3, 4]
# c = a + b
# print(c)
# c += [5, 6]
# print(c)
# c.extend([7, 8])
# print(c)

# rearange list in place

# reverse() method
# a = [1, 2, 3]
# a.reverse()
# print(a)

# sort()  method
# a.sort()
# print(a)

# sort(reverse = True)  method
# a = [3, 2, 5, 4]
# a.sort(reverse = True)
# print(a)

# sort(key)  method
# key is callable object that accepts single parameter
# items are passed to the callable and sorted on its return value
# t = "items are passed to the callable and sorted on its return value".split()
# print(t)
# t.sort(key=len)
# print(t)

# sorted() and reversed() built-in functions

# sorted() creates new list
# a = [2, 3, 1]
# b = sorted(a)
# print(a is b)
# print(b)

# reversed() creates reverse iterator over list
# a = [2, 3, 1]
# r = reversed(a)
# print(r)
# b = list(r)
# print(b)

# ------------
# dictionaries
# key: value pairs
# key must be unique in dictionary, duplicate values is possible
# internally, dictionary maintain refferences to key and value objects
# key onjects must be immutable (string, numbers, tuples, ...)
# value object can be mutable
# dictionary does not maintan any order of items

# # dict() constructor
# name_and_age = dict([('Alice', 32), ('John', 18)])
# print(name_and_age)
# name_and_age = {'Alice': 32, 'John': 18}
# print(name_and_age)
# name_and_age = dict(Alice = 32, John = 18)

# # copy dictionary is shallow copy
# # option 1
# a = name_and_age.copy()
# print(a)
# # option 2
# a = dict(name_and_age)
# print(a)

# # update() dictionary
# # add entries from one dictionary to the other
# # call this method on dictionary to be udated
# # if keys already exists in target dict, then values are updated as in source
# n = dict(answer = 42, random = 99)
# a.update(n)
# print(a)
# n = dict(answer = 42, random = 1000)
# a.update(n)
# print(a)

# # Dictionary is itarable
# # Yields next key on each iteration, in arbitrary order

# for key in a:
#     print(f"Key => {key}")

# # keys() -> returns itarable object of keys
# print(name_and_age.keys())
# for key in a.keys():
#     print(f"Key => {key}")

# # values() -> return itarable object of values
# print(name_and_age.values())
# for value in a.values():
#     print(f"Value => {value}")

# # items() -> return itarable object of tuples
# # tiple unpacking to use in FOR loop
# print(name_and_age.items())
# for key, value in a.items():
#     print(f"Key, Value => {key}, {value}")

# # membership testing
# # IN and NOT IN -> works on keys
# print('John' in a)
# print('Jim' not in a)

# # del() built-in method
# del a['random']
# print(a)

# # mutable items in dictionary
# a['random'] = [1, 2, 3]
# print(a)
# a['random'] += [4, 5, 6]
# print(a)

# from pprint import pprint as pp
# pp(a)

# ------------
# set
# unordered collection of unique elements
# sets are mutable
# elements in set must be imutable

# p =  {1, 2, 4, 5, 6}
# print(type(p))
# print(p)

# # creating sets
# p = {} # creates dictionary
# print(type(p))
# p = set()
# print(type(p))
# print(p)
# # duplicates are discarded
# p = set([1,2,3,4,5,6,7,7,7])
# print(p)

# # sets are iterable, but in random order
# for i in p:
#     print(i)

# # membership testing
# # in
# print(2 in p)
# # not in
# print(3 not in p)

# # add() named method
# p.add(100)
# print(p)
# p.add(100)
# print(p)

# # update() named method
# p.update([1,2,300])
# print(p)

# # remove() named method
# # raises KeyError if element not present in set
# # p.remove(300)
# # print(p)
# # p.remove(1000)
# # print(p)

# # discard() named method
# # no error is raised if element not present in set
# p.discard(300)
# print(p)
# p.discard(300)
# print(p)

# # copy() named method
# c = p.copy()
# print(c)
# print(c == p)
# print(c is p)


# set algebra
# union, difference, intersection
# subset, superset, disjoint

# a = {1,2,3}
# b = {2,3,4}
# print("a : ", a)
# print("b : ", b)


# print("Union a b : ", a.union(b))
# print("Union b a: ", b.union(a))
# print(a.union(b) == b.union(a))
# print("Intersection : ", a.intersection(b))
# print("Difference a - b: ", a.difference(b))
# print("Difference b - a: ", b.difference(a))
# print("Symmetric difference : ", a.symmetric_difference(b))
# print("Is subset : ", a.issubset(b))
# print("Is superset : ", a.issuperset(b))
# print("Is disjoint : ", a.isdisjoint(b))

# ------------
# Protocols
# Protocol is set of operations, which type must support to implement a protocol
# In Python, protocol do not need to be defined as separate interface or base class

# Protocol           Implemented in collections                  Implementation require
# ------------------------------------------------------------------------------------------------------------------------------------
# Container          str, list, dict, range, tuple, set, bytes   in, not in
# Sized              str, list, dict, range, tuple, set, bytes   len()
# Itereble           str, list, dict, range, tuple, set, bytes   Yield items one by one as required, can be used in FOR LOOPS
# Sequence           str, list, range, tuple, bytes              item = sequence[index]
#                                                                i = sequence.index(item)
#                                                                num = sequence.count(item)
#                                                                r = reversed(sequence)
#                                                                Must support Container, Sized and Itereble
# Mutable Sequence   list
# Mutable Set        set
# Mutable Mapping    dict



# -------------------------------------------------------
# Exceptions
# -------------------------------------------------------

# from exceptional import convert

# # version 1
# print(convert("one three three seven".split()))
# #raises an exception
# print(convert("around two million".split()))
# # KeyError: 'around'


# # # version 2 -> KeyError exception handled
# print(convert("one three three seven".split()))
# # try block not fully executed
# print(convert("around two million".split()))

# # # version 3 -> TypeError exception handled
# lets pass not itereble parameter
# print(convert(512))
# TypeError: 'int' object is not iterable

# following errors should almost never be handled, but instaed of corrected while development
# IndentationError, SyntaxError, NameError


# Version 6 -> Accessing exception object
# print(convert("1"))
# print(convert(1))


# Version 7 -> add string_log and raising exception

# from exceptional import string_log
# #print(string_log("Error".split()))
# # we have 2 exceptions raised, one we handled in convert and new one from string_log
# # best is just to raise an exception from convert
# print(string_log("two five".split()))
# print(string_log("cat dog".split()))


# exceptions are part of a API
# they should be well documented, so calling prorgrams can properly handle them
# from roots import sqrt
# OK
# print(sqrt(9))
# print(sqrt(2))
# # ZeroDivisionError Error
# print(sqrt(-1))
# Normally we would nor raise ZeroDivisionError error
# But rather create ValueError as part of our API
# help(sqrt)
# try:
#     print(sqrt(-1))
# except ValueError as e:
#     print("Handled")

# Common exception types
# IndexError -> integer index is out of range
# print([1,2,3][4])
# ValueError -> object is correct type but has inappropriate value
# print(int("X"))
# KeyError
# print({'Alice': 32, 'John': 18}['Peter'])

# Avoid explicit type checks
# x = 1
# x = "X"
# if not isinstance(x, int):
#     raise TypeError("X must by type int")
# else:
#     print("OK")

# It is easier to ask for forgiveness than permission
# Is basically 2 approaches
# 1. LBYL (Look Before You Leap) -> Check all preconditions
# 2. EAFP ->  Run, hope for the best and prepar for consequences  -> Strongly preffered in Python
# EAFP is enabled by execptions
# using EAFP, it is very dificult to silently ignore errors

# LBYL
# import os
# p = 'my_file.txt'
# if os.path.exists(p):
#     print("Process file")
# else:
#     print("File does not exist")

# EAFP
# p = 'my_file.txt'
# p = 'roots.py'
# try:
#     f = open(p)
#     print("All good.")
# except OSError as e:
#     print(f"Error: {e!r}")
# f.close()

# clean up actions
# context managers - will cover later
# try:
# except: -> handle exception
# finally: -> executes allways, regardles how try block terminates

# import os

# def make_at(path, dir_name):
#     original_path = os.getcwd()
#     os.chdir(path)
#     os.mkdir(dir_name) # if this failes, we will not get back to our original directory
#     os.chdir(original_path)

# def make_at(path, dir_name):
#     original_path = os.getcwd()
#     os.chdir(path)
#     try:
#         os.mkdir(dir_name)
#     except OSError as e:
#         raise
#     finally:
#         os.chdir(original_path)


# -------------------------------------------------------
# Iteration and iterables
# -------------------------------------------------------

# ------------
# Comprehensions
# is concise syntax to discribe lists, sets and dictionaries
# readable and expressive
# close to natural language

# ------------
# list comprehension
# [expr(item) for item im iterable]

# l = [i for i in range(10)]
# print(l)

# words = "LKN qepj foefi fepoiejf Jqf HHHfjwpf Oofjowf oqfn oqfho qfpoqfofhN".split()
# l = [len(word) for word in words]
# print(l)
# l = []
# for word in words:
#     l.append(len(word))
# print(l)

# from math import factorial
# l = [len(str(factorial(x))) for x in range(20)]
# print(l)

# ------------
# set comprehension
# {expr(item) for item im iterable}

# from math import factorial

# f = {len(str(factorial(x))) for x in range(20)}
# print(f)

# ------------
# dictionary comprehension
# {
#  key_expr(item) : value_expr(item)
#  for item im iterable
# }

# country_to_capital = {
# 	'United Kingdom': 'London',
# 	'Italy': 'Rome',
# 	'Switzerland': 'Bern'
# }
# print(country_to_capital)
# capital_to_country = {country: capital for capital, country in country_to_capital.items()}
# print(capital_to_country)

# ------------
# filtering comprehensions

# create list of prime numbers in given range

# from pprint import pprint as pp
# from math import sqrt

# def is_prime(x):

# 	if x < 2:
# 		return False

# 	for i in range(2, int(sqrt(x))+1):
# 		if x % i == 0:
# 			return False

# 	return True

# prime_numbers = [x for x in range(20) if is_prime(x)]
# pp(prime_numbers)

# prime_square_divisors = {x*x: (1, x, x*x) for x in range(20) if is_prime(x)}
# pp(prime_square_divisors)


# ------------
# iteration protocol
# 2 types of onjects:
# Iterable - can be passed to build-in iter() function to obtain iterator
# Iterator - can be passed to build-in next() function to get next value in sequence

# iterable = ['My', 'List', 'As', 'Iterable']
# iterator = iter(iterable)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # -> raise StopIteration

# FOR Loops and comprehensions are build on top of above


# ------------
# Generator functions
# -> iterables defined by functions
# -> has lazy evaluations, can model infinite sequences
# -> composable into pipelines
# Generator functions must include yield() at least once
# may also include return with no arguments

# def gen123():
# 	yield 1
# 	yield 2
# 	yield 3

# print(type(gen123))

# g = gen123()

# print(type(g)) # Class Generator, Generator is iterator

# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g)) # -> raise StopIteration

# for x in gen123():
# 	print(x)

# def gen246():
# 	print('About to yield 2')
# 	yield(2)
# 	print('About to yield 4')
# 	yield(4)
# 	print('About to yield 6')
# 	yield(6)
# 	print('About to return')

# g = gen246()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# ------------
# maintaining state in Generators

# def take(count, iterable):
# 	counter = 0
# 	for item in iterable:
# 		if counter == count:
# 			# print('return')
# 			return # terminate stream of yielded values
# 		counter += 1
# 		# print(f"take = {counter}")
# 		yield item

# def distinct(iterable):
# 	seen = set()
# 	for item in iterable:
# 		if item in seen:
# 			# print('continue')
# 			continue # finish current loop iteration and begin next iteration immediately
# 		# print(f"distinct = {item}")
# 		yield item
# 		seen.add(item)

# def run_pipeline():
# 	items = [1, 2, 2, 3, 3, 4, 5, 6]
#     # lazy evaluation is used, generator only progress until yield
#     # it nested iterates in both generators
# 	for item in take(4, distinct(items)):
#     # list constructor makes the distinct() generator to fully complete before iterating take() generator
# 	# for item in take(4, list(distinct(items))):
# 		print(item)

# run_pipeline()

# ------------
# Laziness and Infinite
# Laziness enables to model infinite sequences
# examples: sensors readings, mathematical sequences, content of large files

# Lucas sequence
# def lucas():
# 	yield 2
# 	a = 2
# 	b = 1
# 	while True:
# 		yield b
# 		a, b = b, a + b

# x = lucas()
# for i in range(20):
# 	print(next(x))


# ------------
# Generator expression
# (expr(item) for item im iterable)
# similar to list comprehension

# milion_squares = (x*x for x in range(1,1000001)) # create generator object
# print(milion_squares)

# print(list(milion_squares)[-10:]) # pull whole generator into list = into memory
# print(list(milion_squares)) # generator already completed, will not produce any resuls

# print(sum(x*x for x in range(1,1000001))) # this does not consume much memory due to generators laziness
# print(sum((x*x for x in range(1,1000001)))) # the () can be included but are optional for better readability

# generator expresion can have if clause at the end
# print(sum(x*x for x in range(1,1000001) if x % 2 == 0))

# ------------
# Iteration tools
# bateries included
# we already had enumerate() and sum()
# Itertools includes much more

# ------------
# islice() -> slice iterator
# count() -> generate unbounded sequence of integers

# get a list of first 1000 prime numbers

# from math import sqrt

# def is_prime(x):
# 	if x < 2:
# 		return False
# 	for i in range(2, int(sqrt(x))+1):
# 		if x % i == 0:
# 			return False
# 	return True

# from itertools import islice, count

# thousands_primes = islice((x for x in count() if is_prime(x)),1000)
# print(thousands_primes)
# print(next(thousands_primes))
# print(next(thousands_primes))
# print(list(thousands_primes)[-10:])

# print(sum(islice((x for x in count() if is_prime(x)),1000)))

# ------------
# any() -> determines, if any element  in iterable object is  True
# all() -> determines, if all elements in iterable object are True

# print(any([True, False]))
# print(all([True, True]))

# are there prime numbers in given range
# print(any(is_prime(x) for x in range(127,130)))

# are all items in list starting with capital leter
# print(all(name == name.title() for name in ['Ab', 'Ac', 'Xx']))

# ------------
# zip() -> combines 2 or more iterables into list of tuples

# sunday = [11, 11, 12, 15, 17]
# monday = [10, 14, 17, 18, 22]

# x = zip(sunday, monday)
# print(type(x))
# print(x)
# print(list(x))

# for temps in zip(sunday, monday):
# 	print(f"min = {min(temps):4.1f} max = {max(temps):4.1f} average = {sum(temps) / len(temps):4.1f}")

# ------------
# chain() -> lazily concatenates iterables

# sunday = [11, 11, 12, 15, 17]
# monday = [10, 14, 17, 18, 22]
# tuesday = [15, 16, 19, 22, 24]

# from itertools import chain

# print(all(t > 0 for t in chain(sunday, monday, tuesday)))

# for temp in chain(sunday, monday, tuesday):
#     print(temp)


# lets print prime numbers in lucas sequence

# from math import sqrt

# def is_prime(x):
# 	if x < 2:
# 		return False
# 	for i in range(2, int(sqrt(x))+1):
# 		if x % i == 0:
# 			return False
# 	return True

# # Lucas sequence
# def lucas():
# 	yield 2
# 	a = 2
# 	b = 1
# 	while True:
# 		yield b
# 		a, b = b, a + b

# for x in (p for p in lucas() if is_prime(p)):
# 	print(x)

# from itertools import count
# import time

# cnt = 0
# for x in (p for p in count() if is_prime(p)):
#     if cnt % 100000 == 0:
#         print(f"Found : {x} at {time.ctime()}")
#         cnt = 0
#     cnt += 1

# -------------------------------------------------------
# Classes
# -------------------------------------------------------

# print(type(1))
# print(type("X"))
# print(type([1, 2, 3]))
# print(type(x for x in range(5)))

# Class defines structure and behaviour of a object at the time we crate it
# Class act as a template for creating new ojects
# Class controls an objects iitial state, attributes and methods
# In Python, you can do a lot without classes, just by using functions

# ------------
# define class
# define new class or define class based on another classes

# from airtravel import Flight, Aircraft
# from pprint import pprint as pp

# print(Flight)

# # we call a class constructor by ()
# f = Flight()
# print(f)
# # type() of an object is class of an object
# print(type(f))
# print(isinstance(f, Flight))


# ------------
# instance methods

# f = Flight()
# print(type(f.number))
# # calling instance, widely used syntax
# print(f.number())
# # another option, not used
# print(Flight.number(f))

# ------------
# instance initializer

# create Flight instance by passing flight number
# f = Flight("SN060")
# # accesss flight number by calling number() method
# print(f.number())
# # also _ details are accesible, not recommended, only for debugging
# print(f._number)

# there is no public, private and protected access modifiers in Python lie in Java, C#, etc
# Python has everything is public approach
# naming shold be sufficient as indicator

# ------------
# adding checks to class initializer

# f = Flight("060")
# f = Flight("sn060")
# f = Flight("SNabcd")
# f = Flight("SN12345")
# f = Flight("SN060")
# print(f.number())
# print(f.airline())


# ------------
# adding second Aircraft class

# a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
# print(a.model())
# print(a.registration())
# print(a.seating_plan())


# ------------
# collaborating classes
# Object Oriented design principle -> The Law of Demeter - principle of least knowledge
# You should never call methods on objects you received from other calls
# Only talk to your friends

# f = Flight("SN060", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
# # The Law of Demeter
# # this
# print(f.aircraft_model())
# # instead of
# print(f._aircraft.model())
# Zen of Python - Complex is better than complicated
# if you using Flight class, you dont need to know about Aircraft class


# ------------
# booking seats

# we will use list of dictionaries to keep track who is sitting where
# list will have 1 entry (dictionary) for each seat row
# each seats in 1 row will be moddeled as dictionary, where
# key = Seat letter, value = Passanger Name, None for empty seat

# f = Flight("SN060", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
# pp(f._seating)
# f.alocate_seat('12A', 'Julia')
# pp(f._seating)
# f.alocate_seat('12A', 'John')
# pp(f._seating)
# f.alocate_seat('12X', 'John')
# pp(f._seating)
# f.alocate_seat('DD', 'John')
# pp(f._seating)
# f.relocate_passenger('12A', '12F')
# pp(f._seating)
# print(f.num_avaiable_seats())
# f.alocate_seat('12E', 'John')
# print(f.num_avaiable_seats())

# from airtravel import make_flight, console_card_printer
# from pprint import pprint as pp

# f = make_flight()
# # we have access to Flight object, even we only imported function from module
# print(type(f))
# pp(f._seating)


# ------------
# print boarding cards
# requirement is to print boarding cards in alphabetical order
# for this we create separate card printer function first
# card printer
# function is sufficient, no need to create class
# also Fligt class is not right place for this generic function - separation of concerns principle
# Tell!! Dont ask.
# -> rather than function query all passangers detals from Flight object
# -> we tell the function what to do by passing the arguments
# -> this way is not related to the Flight object
# -> function doesnt know anything about flights or aircraft objects

# than we add methods into Flight class to print the make boarding cards

# f = make_flight()
# f.make_boarding_cards(console_card_printer)

# ------------
# Polymorphism
# using objects of different types through a uniform interface
# we already seen example with make_boarding_cards passing console_card_printer is printing function
# make_boarding_cards is interface
# accepts different printing functions, we could add html_card_printer and pass it to interface
# Polymorphism in Python is achieved through duck typing, we already covered
# Object fitness for particular use is determined at runtime
# rather than in statically typed languages, where it is determined by compiler
# Version 7
# Model and seating plan are related, so lets make 1 class per model

# before - > Aircraft(registration, model, num_rows, num_seats_per_row)
# after -> Aircraft(registration)


# from airtravel import make_flights, console_card_printer
# from pprint import pprint as pp

# f, g = make_flights()
# print(f.aircraft_model())
# print(g.aircraft_model())

# print(f.num_avaiable_seats())
# print(g.num_avaiable_seats())

# f.make_boarding_cards(console_card_printer)
# g.make_boarding_cards(console_card_printer)


# ------------
# Inheritance
# is a mechanism, where one class = subclass can be derived from another class = base class
# allowing us to make behaiviour more specific in derived class

# Nominaly typed languages like Java, uses inheritance for polymorphism
# Python uses late binding
# - no method calls or attribute lookups are bound to actual objects
# until the point at which they are called
# this means we can try any method on any object and it will suceed if the object fits
# Inheritance in Python is primarily used for sharing implementations between classes
# Version 8
# Example for above

# adding same method num_seats to both AirbusA319 and Boeing777 classes
# from airtravel import make_flights

# f, g = make_flights()
# # access _ only for demo
# print(f._aircraft.num_seats())
# print(g._aircraft.num_seats())

# from airtravel import *

# base = Aircraft("Airbus A319")
# # will fail
# print(base.num_seats())

# a = AirbusA319('G-EUPT')
# b = Boeing777('F-GSPS')
# print(a.num_seats())
# print(b.num_seats())


# Thanks to Duck typing, inheritance is used much less in ython than in other languages


# -------------------------------------------------------
# File IO and resource management
# -------------------------------------------------------

# Files are just one example of objects representing resources
# Resources are program elements that must be released or closed after use
# Python provides specific syntax for managing resources

# ------------
# Opening files = built in function open()
# arguments: file
# -> name of the file
# -> mode ->  read (r), write (w), append (a) + binary (b) or text (t)
# -> encoding -> if not specified, default will be used
# import sys
# print(sys.getdefaultencoding())

# f = open('wasteland.txt', mode='wt', encoding='utf-8')
# we can call help not only on Classes but also instances
# # help(f)
# f.close()

# ------------
# Writing text files

# f = open('__tmp__test_file.txt', mode='wt', encoding='utf-8')
# print(f.write("First line of the file.\n"))
# f.write("This should be second line of the file")
# f.write(" created using 2 write() calls.")
# f.close()

# ------------
# Reading text files
# read() method reads number of characters (not bytes)
# and advances the file pointer to the ed of what was read
# return type is str when we open the file in text mode

# f = open('__tmp__test_file.txt', mode='rt', encoding='utf-8')
# print(f.read(10))
# print(f.read(10))
# print(f.read(10))
# print(f.read())
# # futher call to read returns empty string
# print(f.read())

# # seek() - return to the start of the file
# # return value is the new file pointer position
# print(f.seek(0))
# print(f.read(10))
# print(f.read(10))
# f.close()

# reading with read is not much practical
# readline() -> reads whole line 

# f = open('__tmp__test_file.txt', mode='rt', encoding='utf-8')
# print(f.readline())
# # no newline character at the end of second line -> better to show in repl
# print(f.readline())
# f.close()

# readlines() -> read all lines into list -> hope we have enough memory :-)

# f = open('__tmp__test_file.txt', mode='rt', encoding='utf-8')
# print(f.readlines())
# f.close()


# ------------
# Appending to the text file
# open file in append (a) mode

# f = open('__tmp__test_file.txt', mode='at', encoding='utf-8')

# writelines() - write iterable serie of strings into file

# f.writelines(
#     [
#         ' Second line',
#         ' ends here.\n'
#         'Third line using',
#         ' using 2 list elements.\n'
#     ]
# )
# f.close()

# ------------
# Iterating over file lines

# import sys
# g = open('__tmp__test_file.txt', mode='rt', encoding='utf-8')
# my_lines = []
# for line in g:
# 	my_lines.append(line)
# 	# print(line) # print() adds newline at the end of each printed text
# 	sys.stdout.write(line) # this is standart output write, not adding newline
# g.close()
# print(my_lines)


# ------------
# Closing files with finally
# we will use recaman module

# from recaman import write_sequence
# from series import print_series

# write_sequence('recaman.dat', 1000)
# print_series('recaman.dat')

# modify file manually to create exception
# print_series('recaman.dat')
# causes error and f.close() was never executed

# ------------
# With-blocks
# until now we had following pattern
# open file
# ...work with file
# close file
# closing file is important and should allways happen
# it informs OS that you are done with file
# so every open() must be followed with close()
# with-block are supporting this
# with-block works with any object that supports context-manager protocol

# from recaman import write_sequence
# from series import print_series

# write_sequence('recaman.dat', 1000)
# print_series('recaman.dat')

