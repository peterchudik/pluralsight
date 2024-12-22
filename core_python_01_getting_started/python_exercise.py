# ------------------------------
# scalar types
# ------------------------------

# ------------------------------
# # int
# ------------------------------
# print(10)

# ------------------------------
# binary
# ------------------------------
# print(0b10)

# ------------------------------
# octo
# ------------------------------
# print(0o10)

# ------------------------------
# hex
# ------------------------------
# print(0x10)
# print(int(3.5))
# print(int(-3.5))
# print(int("456"))
# print(int("10000", 3))

# ------------------------------
# float
# ------------------------------
# print(3.125)
# print(3e8)
# print(1.656e-65)
# print(3.0 + 1)

# print(float(7))
# print(float("nan")) # nan = not a number
# print(float("inf")) # positive infinity
# print(float("-inf")) # negative infinity

# ------------------------------
# Null value = None
# ------------------------------
# print(None)
# a = None
# if a is None:
# 	print("Is None")

# ------------------------------
# Boolean
# ------------------------------
# print(True)
# print(False)

# print(bool(0))
# print(bool(42))
# print(bool(-1))
# print(bool(0.0))
# print(bool(42.1))
# print(bool(-1.1))
# print(bool([]))
# print(bool([1, 2, 3]))
# print(bool(""))
# print(bool("Spam"))


# ------------------------------
# Relational operators
# ------------------------------

# ------------------------------
# ==, !=, <, >, <=, >=
# ------------------------------

# if 2 == 2.0:
# 	print("True")

# ------------------------------
# Control flow
# ------------------------------

# if True:
# 	print("Yes")
# elif False:
# 	print("No")
# else:
# 	print("Panic")

# ------------------------------
# While loops
# ------------------------------

# c = 5
# while c != 0:
# 	print(c)
# 	c -= 1

# while True:
# 	response = input()
# 	if int(response) % 7 == 0:
# 		break

# ------------------------------
# Colection types
# ------------------------------

# ------------------------------
# str, bytes, list, dict
# ------------------------------

# ------------------------------
# strings have datatype str
# str is immutable
# str is sequence of unicode code points
# ------------------------------

# print('This is string')
# print("This is string")
# print('This "is" string')
# print("This 'is' string")
# a = "first" "second"
# print(a)
# print("Line1\n	Line2\nLine3")

# ------------------------------
# \n -> universal newline (Windows, Unix, etc.)
# ------------------------------

# print("This \"is\" string")

# ------------------------------
# raw string 
# ------------------------------

# path = r'c:\nxxx\nddd'
# print(path)

# s = 'string'
# print(s[2])

# print(type(s))
# print(type(s[2]))

# c = 'oslo'
# print(c.capitalize())
# print(c.count('o'))

# ------------------------------
# bytes
# ------------------------------

# print(b'data data')

# a = b'data data'
# print(a)
# print(a[0])
# print(a.split())

# ------------------------------
# to convert between str and bytes
# use
# encode str -> byte
# decode byte -> str
# ------------------------------

# name = 'olafhladj'
# data = name.encode('utf8')
# print(name)
# print(data)
# name_back = data.decode('utf8')
# print(name_back)
# if name == name_back:
# 	print('Yes')

# ------------------------------
# list
# sequence of objects
# mutable
# ------------------------------

# print(list('characters'))

# ------------------------------
# dict
# key value pairs
# {k1 : v1, k2: v2}
# ------------------------------


# ------------------------------
# for loops
# for item in iterable:
#	... body...
# ------------------------------

# for c in list('characters'):
# 	print(c)

# from urllib.request import urlopen

# a = 496
# print(id(a))

# b = 1729
# print(id(b))

# b = a

# print(id(a))
# print(id(b))

# print(a == b)
# print(a is b)

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)
# print(a is b)

# a = [1, 2, 3]
# b = a

# a[1] = 2

# print(a is b)

# f = [1, 2, 3]
# def replace(g):
# 	g = [4, 5, 6]
# 	print(g)

# replace(f)
# print(f)

# a = [1, 2, 3]
# def f(x):
# 	return(x)

# b = f(a)
# print(b is a)

# import time

# print(time.ctime())
# time.sleep(1)

# def ctime(arg=time.ctime()):
# 	print(arg)

# def ctime(arg=None):
# 	arg = time.ctime()
# 	print(arg)

# time.sleep(2)
# ctime()
# time.sleep(2)
# ctime()
# time.sleep(2)
# ctime()

# ------------------------------
# Dynamic type system
# ------------------------------

# def add(a, b):
# 	print(a + b)

# add(1,2)
# add(1.1,2.2)
# add('x','y')
# add([1,2],[3,4])

# ------------------------------
# scopes
# ------------------------------

# count = 0

# def get_count():
# 	print(count)

# def set_count(c):
# 	global count
# 	count = c

# get_count()
# set_count(5)
# get_count()

# ------------------------------
# tuple
# ------------------------------

# a = (1,2,3)
# print(type(a))
# a += ('3',4)
# print(a)
# a*=3
# print(a)
# h = (3)
# print(type(h)) # not a single element tuple
# h = (3,)
# print(type(h)) #     a single element tuple
# print(h)
# t = 1, 2, 3, 4 # also a tuple, no brackets
# print(type(t))

# def minmax(items):
# 	return min(items), max(items) # tuple, no brackets

# print(minmax([1,2,3,4,5]))
# print(type(minmax([1,2,3,4,5])))

# ------------------------------
# tuple unpacking
# ------------------------------

# (lower, upper) = minmax([1,2,3,4,5])

# print(lower)
# print(type(lower))
# print(upper)
# print(type(upper))

# (a, (b , (c, d))) = (1, (2, (3,4)))
# print(type(d))

# a = 'jelly'
# b = 'bean'

# a, b = b, a # first, on right side, packs a and b into tuple, then unpacks tuple to the a and b on the left side

# print(a)
# print(b)

# ------------------------------
# tuple constructor
# ------------------------------

# a = tuple('String')
# print(a)
# print(type(a))

# ------------------------------
# in, not in
# ------------------------------

# print(t in a)
# print(t not in a)


# ------------------------------
# string also a collection
# ------------------------------

# a = 'a' + 'b' + 'c' + 'b'
# print(a)
# print(type(a))

# ------------------------------
# better to use str.join method instead of + = more efficient
# ------------------------------

# a = ''.join(('a', 'b', 'c', 'd'))
# print(a)

# a = ';'.join(('a', 'b', 'c', 'd'))
# print(a)
# a = a.split(';')
# print(a)


# a = "unforgetable".partition('forget')
# print(a)
# print(type(a))

# departure, separator, arrival = 'London:Zurich'.partition(':')
# print(departure)
# print(separator)
# print(arrival)

# departure, _, arrival = 'London:Zurich'.partition(':') # convenntion tu use _ for dummy/unused values
# print(departure)
# print(_)
# print(arrival)

# ------------------------------
# format method
# ------------------------------

# a = 'Then age of {0} is {1}'.format('Jim', '32')
# print(a)
# a = 'Then age of {name} is {age}'.format(name='Jim', age='32')
# print(a)
# a = 'Then age of {pos[0]} is {pos[1]}'.format(pos=('Jim', '32'))
# print(a)

# import math
# print(type(math))
# a = 'Math constants {m.pi} is {m.e}'.format(m=math)
# print(a)
# a = 'Math constants {m.pi:.3f} is {m.e:.3f}'.format(m=math)
# print(a)

# a = f'Math constants {math.pi:.3f} is {math.e:.3f}'
# print(a)

# help(str)


# ------------------------------
# range
# ------------------------------

# print(range(5))
# print(list(range(5)))
# print(list(range(10,20,2)))

# a,b,c,d,e = range(5)
# print(a)
# print(b)

# ------------------------------
# enumerate - returns pair of tuples from list item, where first value is index, second value is the value
# ------------------------------

# a = enumerate(range(5))
# print(a)

# for i, v in enumerate(range(5)):
# 	print(f'i = {i}, v = {v}')

# ------------------------------
# list - indexing
# ------------------------------
# a = [1,2,3,4,5]
# print(a)
# print(a[-1])
# print(a[0])
# print(a[-0])
# print(a[1:3])
# print(a[1:-1])
# print(a[:2])
# print(a[2:])

# ------------------------------
# copy list = shallow copies, we have 2 list objects, but they both reference same objects in the lists
# ------------------------------
# b = a
# print(a is b)
# print(a == b)
# print(id(a))
# print(id(b))
# c = a[:]
# print(c is a)
# print(c == a)
# print(id(a))
# print(id(c))
# d = list(a) # preffered
# print(d is a)
# print(d == a)
# e = a.copy()
# print(e is a)
# print(e == a)

# a = [ [1, 2], [3, 4]]
# print(a)

# b = a
# print(b)

# a[1].append(5)
# print(a)
# print(b)


# a = [0] * 9
# print(a)

# a = [ [0, 1] ] * 9
# print(a)

# a[0].append(5)
# print(a)

# a = 'some random text for testing the split of text'.split()
# print(a)
# b = a.index('random')
# print(b)
# print(a[b])

# b = a.count('text')
# print(b)

# print('text' in a)
# print('x' not in a)

# del a[8]
# print(a)

# a.remove('of')
# print(a)

# a.insert(len(a), 'of')
# a.insert(len(a), 'text')
# print(a)
# print(' '.join(a))

# ------------------------------
# sort and reverse methods of list object
# ------------------------------
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.sort(key=len, reverse=True)
# print(a)


# ------------------------------
# sorted and reversed as callable objects, in this case both are functions
# ------------------------------

# b = sorted(a)
# print(b)

# c = reversed(b)
# print(list(c))


# ------------------------------
# Dictionaries
# ------------------------------

# my_list_of_tuples = [(1, 'X'), (2, 'Y'), (3, 'Z')]
# print(my_list_of_tuples)
# my_dict = dict(my_list_of_tuples)
# print(my_dict)

# d = dict(a='alfa', b='bravo', c='charlie')
# d = dict(a=['alfa'], b=['bravo'], c=['charlie'])
# print(d)

# e = dict(d)
# print(e)

# print(d is e)

# d['a'] = 'x'
# print(d)
# e['d'] = ['delta']
# print(e)

# d.update(e)
# print(d)

# ------------------------------
# Set
# ------------------------------

# a = {}
# print(type(a))

# a = set()
# print(type(a))

# a = set([1,1,2,3,4,4,5,5,5,6,7,8,9])
# print(a)

# for x in a:
# 	print(x)


# print(1 in a)
# print(10 in a)

# a.add(10)
# print(a)

# a.update([7, 11, 13])
# print(a)

# a.remove(11)
# a.discard(17)

# print(a)

# ------------------------------
# set operators = union, difference, intersection, subset, superset, disjoint
# ------------------------------

# a = {1,2,3}
# b = {2,3,4}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.isdisjoint(b))


# ------------------------------
# Comprehensions
# ------------------------------

# words = "LKN qepj foefi fepoiejf Jqf HHHfjwpf Oofjowf oqfn oqfho qfpoqfofhN".split()
# print(words)

# ------------------------------
# list comprehension
# [expr(item) for item im iterable]
# ------------------------------

# a = [len(word) for word in words]
# print(a)

# from math import factorial

# f = [len(str(factorial(x))) for x in range(20)]
# print(f)

# ------------------------------
# set comprehension
# {expr(item) for item im iterable}
# ------------------------------

# from math import factorial

# f = {len(str(factorial(x))) for x in range(20)}
# print(f)

# ------------------------------
# dictionary comprehension
# {
#  key_expr(item) : value_expr(item)
#  for item im iterable
# }
# ------------------------------

# country_to_capital = {
# 	'SK': 'BA',
# 	'CZ': 'PH',
# 	'CH': 'ZH'
# }
# print(country_to_capital)

# capital_to_country = {capital: country for country, capital in country_to_capital.items()}
# print(capital_to_country)

# import glob
# import os

# print(glob.glob('**', recursive=True, include_hidden=True))

# file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py', recursive=False)}
# print(file_sizes)

# ------------------------------
# filtering comprehension
# ------------------------------

# from math import sqrt

# def is_prime(x):

# 	if x < 2:
# 		return False

# 	for i in range(2, int(sqrt(x))+1):
# 		if x % i == 0:
# 			return False

# 	return True

# prime_numbers = [x for x in range(101) if is_prime(x)]
# print(prime_numbers)

# prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
# print(prime_square_divisors)

# ------------------------------
# Iterables and Iterators
# ------------------------------

# def first(iterable):
# 	iterator = iter(iterable)
# 	try:
# 		return next(iterator)
# 	except StopIteration:
# 		raise ValueError('iterable is empty')

# my_iterable = ['1', '2', '3', 'x']
# print(my_iterable)

# print(first(my_iterable))
# print(first([]))

# ------------------------------
# Generators -> function contains yield -> is Iterator -> generators are lazy
# ------------------------------

# def gen123():
# 	yield 1
# 	yield 2
# 	yield 3

# print(type(gen123))

# g = gen123()

# print(type(g)) # Class generator, generators are Iterable

# print(next(g))
# print(next(g))
# print(next(g))

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


# def take(count, iterable):
# 	counter = 0
# 	for item in iterable:
# 		if counter == count:
# 			print('return')
# 			return
# 		counter += 1
# 		print(f"take = {counter}")
# 		yield item

# def distinct(iterable):
# 	seen = set()
# 	for item in iterable:
# 		if item in seen:
# 			print('continue')
# 			continue
# 		print(f"distinct = {item}")
# 		yield item
# 		seen.add(item)

# def run_pipeline():
# 	items = [1, 2, 2, 3, 3, 4, 5, 6]
# 	# for item in take(4, distinct(items)): # it nested iterates in both generators
# 	for item in take(4, list(distinct(items))): # list constructor makes the distinct generator to fully complete before iterating take generator
# 		print(item)

# run_pipeline()

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

# ------------------------------
# generator expresions
# (expr(item) for item im iterable)
# ------------------------------

# milion_squares = (x*x for x in range(1,1000001)) # create generator object
# print(milion_squares)

# print(list(milion_squares)[-10:]) # pull whole generator into list = into memory
# print(list(milion_squares)) # generator already completed, will not produce any resuls

# print(sum((1,2,3)))

# print(sum(x*x for x in range(1,1000001))) # this does not consume much memory due to generators laziness
# print(sum((x*x for x in range(1,1000001)))) # the () can be included bu are optional for better readability

# print(sum(x*x for x in range(1,1000001) if x % 2 == 0))

# my_generator = (x for x in range(10))
# a = 0
# for i in my_generator:
# 	a += i
# print(a)


# ------------------------------
# Iteration tools
# islice() -> slice iterator
# count() -> generate unbounded sequence of integers
# ------------------------------

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
# print(list(thousands_primes)[-10:])

# print(sum(islice((x for x in count() if is_prime(x)),1000)))

# ------------------------------
# any() -> any element  in iterable object is  True
# all() -> all elements in iterable object are True
# ------------------------------

# print(any([True, False]))
# print(all([True, False]))

# print(any(is_prime(x) for x in range(127,130)))
# print(all(name == name.title() for name in ['Ab', 'Ac', 'Xx']))

# ------------------------------
# zip() -> combines 2 or more iterables into list of tuples
# ------------------------------

# sunday = [11, 23, 14,  15, 20]
# monday = [10, 20, 23,  19, 18]

# x = zip(sunday, monday)
# print(type(x))
# print(x)

# for x in zip(sunday, monday):
# 	print(x)

# ------------------------------
# chain() -> lazily concatenates iterables
# ------------------------------

# from itertools import chain

# print(all(t > 0 for t in chain(sunday, monday)))


# ------------------------------
# Files
# ------------------------------

# import sys
# print(sys.getdefaultencoding())

# ------------------------------
# create new file -> w (write) t (text)
# ------------------------------


# f = open('wasteland.txt', mode='wt', encoding='utf-8')
# help(f)
# print(f.write('What are the roots that clutch,  '))
# print(f.write('what branches grow\n'))
# print(f.write('Out of this stony rubbish? '))
# f.close()

# ------------------------------
# read existing file -> r (write) t (text)
# ------------------------------

# g = open('wasteland.txt', mode='rt', encoding='utf-8')
# print(g.read(32))
# print(g.read())
# print(g.read())

# g.seek(0) # for text files, only 0 and any other returned by tell is supported
# print(g.readline())
# print(g.readline())
# print(g.readline())

# g.seek(0)

# print(g.readlines()) # only if you have enough memory :-)

# f.close()

# ------------------------------
# append existing file -> a (append) t (text)
# ------------------------------

# h = open('wasteland.txt', mode='at', encoding='utf-8')

# h.writelines(['\nLine1','Line1\n','Line2\n','Line3'])

# h.close()

# ------------------------------
# files support iterator protocol, iterates line by line
# ------------------------------

# g = open('wasteland.txt', mode='rt', encoding='utf-8')

# for line in g:
# 	# print(line) # adds newline at the end of each printed text
# 	sys.stdout.write(line) # this is standart output write, not adding newline

# g.close()


# import sys
# from itertools import count, islice


# def sequence():
# 	"""Generate Recaman's sequence"""
# 	seen = set()
# 	a = 0
# 	for n in count(1):
# 		yield a
# 		seen.add(a)
# 		c = a - n
# 		if c < 0 or c in seen:
# 			c = a + n
# 		a = c

# ------------------------------
# with block -> can be used with any object which uses context-manager protocol
# ------------------------------

# def write_sequence(filename, num):
# 	"""Write Recaman's sequence to text file"""
# 	with open(filename, mode='wt', encoding='utf-8') as f:
# 		f.writelines(f'{r}\n' for r in islice(sequence(), num + 1))

# def read_series(filename):
# 	with open(filename, mode='rt', encoding='utf-8') as f:
# 		return [int(line.strip()) for line in f]


# write_sequence('recaman.dat', 1000)
# print(read_series('recaman.dat'))


# def words_per_line(flo):
# 	return [len(line.split()) for line in flo.readlines()]

# with open('wasteland.txt', mode='rt', encoding='utf-8') as real_file:
# 	wpl = words_per_line(real_file)

# print(wpl)

# from urllib.request import urlopen

# with urlopen('http://sixty-north.com/c/t.txt') as web_file:
# 	wpl = words_per_line(web_file)

# print(wpl)


# ------------------------------------------------------------------------------------------------------------
# Python - Organizing Larger Programs
# ------------------------------------------------------------------------------------------------------------


# ------------------------------
# sys.path - directories to search when importing module
# sys.path - can be modified by .append(), as it is normal list
# ------------------------------

# import sys

# print(sys.path)
# print(type(sys))

# ------------------------------
# PYTHONPATH - env variable, it is assignet to sys.path on import sys module
# ------------------------------

# import urllib # is package, as it is directory
# import urllib.request # is module, as it is file

# print(type(urllib))
# print(urllib.__path__) 
# print(type(urllib.request))

# ------------------------------
# Python package - is a directory containing __init__.py file
# ------------------------------

# import demo_reader

# print(type(demo_reader))
# print(demo_reader.__path__)
# print(demo_reader.__file__)

# import demo_reader.multireader

# r = demo_reader.multireader.MultiReader('demo_reader/__init__.py')
# print(r.read())
# print(type(r.read()))
# r.close()

# import demo_reader.compressed

# print(type(demo_reader.compressed))
# print(demo_reader.compressed.__path__)
# print(demo_reader.compressed.__file__)

# import demo_reader
# import demo_reader.multireader
# import demo_reader.compressed
# import demo_reader.compressed.gzipped
# import demo_reader.compressed.bzipped

# import os

# print(type(os.path.splitext('abc.txt')))
# print(os.path.splitext('abc.txt'))
# print(os.path.splitext('abc.txt')[1])

# from demo_reader.multireader import MultiReader

# r = MultiReader('test.bz2')
# print(r.read())
# r.close()

# r = MultiReader('test.gz')
# print(r.read())
# r.close()

# r = MultiReader('demo_reader/__init__.py')
# print(r.read())
# r.close()

# ------------------------------
# __all__
# module level attribute
# controls what is imported using import *
# ------------------------------


# from pprint import pprint
# pprint(locals())
# from demo_reader.compressed import *
# pprint(locals())

# ------------------------------
# namespace package
# single logical package split across multiple directories
# cannot have __init__.py file
# ------------------------------

# import demo_reader
# print(demo_reader.__path__)
# import demo_reader.compressed
# print(demo_reader.compressed.__path__)
# import demo_reader.util
# print(demo_reader.util.__path__)

# ------------------------------
# executable directories
# contails __main__,py file, which gets executed
# ------------------------------



