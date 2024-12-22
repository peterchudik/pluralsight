#---------------------------------------------
# __call__ -> object becomes callable
#---------------------------------------------

# from resolver import Resolver

# resolve = Resolver()
# print(resolve('google.com'))
# print(resolve('ubs.com'))
# print(resolve._cache)
# print(resolve.resolve('nitra.sk'))
# print(resolve.resolve('golem.de'))
# print(resolve._cache)


# x = tuple
# print(type(x))
# y = x()
# print(type(y))

# x = tuple('test')
# print(x)
# x = list('test')
# print(x)
# x = set('test')
# print(x)


#---------------------------------------------
# conditional expresion
# result = true_value if condition else false_value
#---------------------------------------------

# x = 1
# print('1') if x == 1 else print('not 1')
# x = 2
# print('1') if x == 1 else print('not 1')

#---------------------------------------------
# lambda = anonymous callable object
#---------------------------------------------

# names = ['a x', 'b y', 'c a', 'd b']
# sorted_names = sorted(names, key = lambda name: name.split()[-1])
# print(sorted_names)

# last_name = lambda name: name.split()[-1]
# print(type(last_name))
# print(last_name('a x'))

#---------------------------------------------
# arbitrary number of positional arguments = *args
#---------------------------------------------

# def hypervolume(*args):
# 	print(args)
# 	print(type(args))

# hypervolume()
# hypervolume(1)
# hypervolume(1,2,3)

# def hypervolume(length, *lengths):
# 	v = length
# 	for item in lengths:
# 		v *= item
# 	return v

# print(hypervolume(2,3,4))
# print(hypervolume(2,3))
# print(hypervolume(2))

#---------------------------------------------
# arbitrary number of keyword arguments = **kwargs
#---------------------------------------------

# def tag(name, **kwargs):
# 	print(name)
# 	print(kwargs)
# 	print(type(kwargs))

# print(tag('img', src='Monet.jpg', alt='Sunrise', border=1))


# def tag(name, **attributes):
# 	result = '<' + name
# 	for key, value in attributes.items():
# 		result += ' {k}="{v}"'.format(k=key, v=str(value))
# 	result += '>'
# 	return result

# print(tag('img', src='Monet.jpg', alt='Sunrise', border=1))

#---------------------------------------------
# positional only arguments -> cannot be passed with keyword
#---------------------------------------------

# def numner_length(x, /):
# 	return len(str(x))

# print(numner_length(x = 10)) # error
# print(numner_length(10))

#---------------------------------------------
# extended call syntax
#---------------------------------------------

# def print_args(arg1, arg2, *args):
# 	print(arg1)
# 	print(arg2)
# 	print(args)

# t = (1,2,3)
# print(print_args(*t)) # * call syntax

# def color(red, green, blue, **kwargs):
# 	print('r = ', red)
# 	print('g = ', green)
# 	print('b = ', blue)
# 	print(kwargs)

# k = {'red':21, 'green':68, 'blue':120, 'alpha':52}
# print(color(**k))

#---------------------------------------------
# argument forwarding
#---------------------------------------------

# def trace(f, *args, **kwargs):
# 	print(args)
# 	print(kwargs)
# 	result = f(*args, **kwargs)
# 	print('result=', result)
# 	return result

# print(trace(int, 'ff', base=16))

#---------------------------------------------
# local function is function defined inside other function
# scope is local to the function outer function
#---------------------------------------------

# def sort_by_last_leter(strings):
# 	def last_letter(s):
# 		return s[-1]
# 	return(sorted(strings, key=last_letter))

# print(sort_by_last_leter(['hello', 'from', 'a', 'local', 'function']))

#---------------------------------------------
# scopes = L (Local) E (Enclosing) G (Global) B (Built-in)
#---------------------------------------------

# g = 'global'
# def outer(p='param'):
# 	l = 'local'
# 	def inner():
# 		print(g, p, l)
# 	inner()

# outer()

# def enclosing():
# 	def local_func():
# 		print('local func')
# 	return local_func

# lf = enclosing()
# lf()

#---------------------------------------------
# how does local function retain access to its enclosing scope?
# answer is __closure__ attribute of local function keeps the references to the needed atributes from enclosing scope
#---------------------------------------------

# def enclosing():
# 	x = 'closed over'
# 	def local_func():
# 		print('local func')
# 	return local_func

# lf = enclosing()
# lf()

#---------------------------------------------
# example of closure usage are function factories
#---------------------------------------------

def raise_to(exp):
	def raise_to_exp(x):
		return pow(x, exp)
	return raise_to_exp

square = raise_to(2)
print(square(5))
print(square(6))

cube = raise_to(3)
print(cube(5))
print(cube(6))

#---------------------------------------------
# global = insert a name binding from global to local scope
# nonlocal = insert a name binding from enclosing to local scope, searches all enclosing scopes from innermost to outermost
#---------------------------------------------

# import time

# def make_timer():
# 	last_called = None # Never
# 	def elapsed():
# 		nonlocal last_called
# 		now = time.time()
# 		if last_called is None:
# 			last_called = now
# 			return None
# 		result = now - last_called
# 		last_called = now
# 		return result
# 	return elapsed

#---------------------------------------------
# __closure__ can associate state with function between function invocations
#---------------------------------------------

# t = make_timer() # as long as t exists it keeps __closure__ which references value of last_called
# print(t())
# time.sleep(1)
# print(t())
# time.sleep(1)
# print(t())
# time.sleep(1)
# print(t())

#---------------------------------------------
# function decorations
# decorator takes callable object as only argument and returns callable object
# syntax:
# @my_deorator
# def my_function():
# execution:
# 1. compile my_function
# 2. pass my_function to my_deorator
# 3. return value from my_deorator and bind it to my_function
# result is my_function bound to resut of calling my_decorator with my_function as parameter
#---------------------------------------------

# this is my decorator
# def excape_unicode(f):
# 	def wrap(*args, **kwargs):
# 		x = f(*args, **kwargs)
# 		return ascii(x)
# 	return wrap

# def northern_city():
# 	return 'Tromsø'

# print(northern_city())

# # this would be how to use decorator but without decorator syntax
# my_wrap = excape_unicode(northern_city)
# print(my_wrap())

# # this is decorator syntax
# @excape_unicode
# def northern_city():
# 	return 'Tromsø'
# # still calling decorated function as it would not be decorated
# print(northern_city())


#---------------------------------------------
# using class objects as decotators
# class is callable object as calling them produce new instance of the class
# when using class as decorator, decorated function is replace by new instance of class which mus be callable (have __call__)
#---------------------------------------------

# class CallCount():
# 	def __init__(self, f):
# 		self.f = f
# 		self.count = 0
# 	def __call__(self, *args, **kwargs):
# 		self.count += 1
# 		return self.f(*args, **kwargs)

# def hello(name):
# 	print('Hello, {}!'.format(name))

# my_call = CallCount(hello)
# print(my_call.count)
# my_call('1')
# my_call('2')
# print(my_call.count)

# @CallCount
# def hello(name):
# 	print('Hello, {}!'.format(name))
# hello('1')
# hello('2')
# print(hello.count)


#---------------------------------------------
# using class instances as decotators
#---------------------------------------------

# class Trace:
# 	def __init__(self):
# 		self.enabled = True
# 	def __call__(self, f):
# 		def wrap(*args, **kwargs):
# 			if self.enabled:
# 				print('Calling {}'.format(f))
# 			return f(*args, **kwargs)
# 		return wrap

# tracer = Trace()

# @tracer
# def rotate_list(l):
# 	return l[1:] + [l[0]]

# l = [1, 2, 3]

# l = rotate_list(l)
# print(l)
# l = rotate_list(l)
# print(l)
# l = rotate_list(l)
# print(l)

# tracer.enabled = False
# l = rotate_list(l)
# print(l)
# l = rotate_list(l)
# print(l)
# l = rotate_list(l)
# print(l)

#---------------------------------------------
# using multiple decorators
#---------------------------------------------

# def excape_unicode(f):
# 	def wrap(*args, **kwargs):
# 		x = f(*args, **kwargs)
# 		return ascii(x)
# 	return wrap

# class Trace:
# 	def __init__(self):
# 		self.enabled = True
# 	def __call__(self, f):
# 		def wrap(*args, **kwargs):
# 			if self.enabled:
# 				print('Calling {}'.format(f))
# 			return f(*args, **kwargs)
# 		return wrap

# tracer = Trace()

# @tracer
# @excape_unicode
# def northern_city():
# 	return 'Tromsø'

# print(northern_city())
# tracer.enabled = False
# print(northern_city())


#---------------------------------------------
# decorating methods of classes
#---------------------------------------------

# class Trace:
# 	def __init__(self):
# 		self.enabled = True
# 	def __call__(self, f):
# 		def wrap(*args, **kwargs):
# 			if self.enabled:
# 				print('Calling {}'.format(f))
# 			return f(*args, **kwargs)
# 		return wrap

# tracer = Trace()

# class IslandMaker:
# 	def __init__(self, suffix):
# 		self.suffix = suffix
# 	@tracer
# 	def make_island(self,name):
# 		return name + self.suffix

# im = IslandMaker(' Island')
# print(im.make_island('Python'))

#---------------------------------------------
# loosing fuction metadata when dcorating function
#---------------------------------------------

# def noop(f):
# 	def noop_wrapper():
# 		return f()
# 	return noop_wrapper
# def hello():
# 	"Print well known message"
# 	print('Hello, world!')
# print(hello.__name__)
# print(hello.__doc__)

# # Function metadata lost
# def noop(f):
# 	def noop_wrapper():
# 		return f()
# 	return noop_wrapper
# @noop
# def hello():
# 	"Print well known message"
# 	print('Hello, world!')
# print(hello.__name__)
# print(hello.__doc__)

# # To preserve function metadata, use functools.wrap
# import functools
# def noop(f):
# 	@functools.wraps(f)
# 	def noop_wrapper():
# 		return f()
# 	return noop_wrapper
# @noop
# def hello():
# 	"Print well known message"
# 	print('Hello, world!')
# print(hello.__name__)
# print(hello.__doc__)

#---------------------------------------------
# parametrized decorators
#---------------------------------------------

# def check_non_negative_index(index):
# 	def validator(f):
# 		def wrap(*args):
# 			if args[index] < 0:
# 				raise ValueError('Argument {} must be non-negative'.format(index))
# 			return f(*args)
# 		return wrap
# 	return validator

# # this is executing function which returns actual decorator
# # index variable is preserved as __closure__ in the decorator
# @check_non_negative_index(1)
# def create_list(value, size):
# 	return [value] * size

# print(create_list('a', 3))
# print(create_list('a', -1))

#---------------------------------------------
# functional style programming
#---------------------------------------------

#---------------------------------------------
# map(function, sequence) function
# map elements in sequence using function into result sequence
# is iterator = lazy evaluation
#---------------------------------------------

# print(ord('a'))

# print(type(map(ord,'a')))

# for i in map(ord,'abc'):
# 	print(i)

# class Trace:
# 	def __init__(self):
# 		self.enabled = True
# 		print('Init')
# 	def __call__(self, f):
# 		def wrap(*args, **kwargs):
# 			if self.enabled:
# 				print('Calling {}'.format(f))
# 			return f(*args, **kwargs)
# 		return wrap

# result = map(Trace()(ord),'abcd')
# for item in result:
# 	print(item)

# result = list(map(Trace()(ord),'abcd'))
# print(result)

# def combine(size, colour, animal):
# 	return '{} {} {}'.format(size, colour, animal)

# sizes = ['small', 'medium', 'large']
# colours = ['red', 'green', 'blue', 'yellow']
# animals = ['god', 'cat', 'chicken']

# # if input sequences are not same size, map will stop after shottest sequence is processed
# combined_list = list(map(combine, sizes, colours, animals))
# print(combined_list)

# # list comprehension
# my_list = [str(i) for i in range(5)]
# print(my_list)

# # list constructor
# my_list = list(map(str,range(5)))
# print(my_list)

# # generator expresion
# i = (str(i) for i in range(5))
# # list constructor
# print(list(i))

# i = map(str, range(5))
# # list constructor
# print(list(i))

#---------------------------------------------
# filter(function, sequence) function
# function - must accept only 1 argument and return True or False
#---------------------------------------------

# positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
# print(list(positives))

# trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'Hello'])
# print(list(trues))

#---------------------------------------------
# itertools.reduce(function, sequence)
# function - must accept 2 arguments
# reduce calls the function repeatedly for 2 arguments
# first argument is result of previous function call
# second argument is next element in the sequence
#---------------------------------------------

# from functools import reduce
# import operator

# print(operator.add(1,2))
# print(reduce(operator.add, range(1,10)))
# print(reduce(operator.mul, range(1,10)))


#---------------------------------------------
# map, reduce
#---------------------------------------------

# def count_words(doc):
# 	# below is generator expresion with if else
# 	normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
# 	frequencies = {}
# 	for word in normalized_doc.split():
# 		frequencies[word] = frequencies.get(word, 0) + 1
# 	return frequencies

# documents=['a b c d e', 'a b c e f g', 'c d g h k']
# # print(list(map(count_words,documents)))
# counts = map(count_words,documents)

# def combine_counts(d1, d2):
# 	d = d1.copy()
# 	for word, count in d2.items():
# 		d[word] = d.get(word, 0) + count
# 	return d

# from functools import reduce
# total_counts = reduce(combine_counts, counts)
# print(total_counts)


#---------------------------------------------
# multi input comprehensions
#---------------------------------------------

# l = [(x, y) for x in range(5) for y in range(5)]
# print(l)

# l = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
# print(l)

#---------------------------------------------
# nested comprehensions
#---------------------------------------------

# list of lists

# vals = [[y * 3 for y in range(x)] for x in range(10)]
# print(vals)
