#-------------------------------------------
# Review
#-------------------------------------------

# from guess import main

# main()


#-------------------------------------------
# Exceptions hierarchies
#-------------------------------------------

# Python has many exception classes
# exception classes are organized into hierarchies using inheritance
# this inheritance facilitates catching exceptions by the base classes
# means any class that is a subclass of a class specified in except will be catched by the exception

# IndexError
# s = [1, 2, 3]
# print(s[4])

# KeyError
# d = dict(a=1, b=2, c=3)
# print(d['d'])

# lets check the inheritance graphs of IndexError and KeyError
# by investigating their __mro__ -> method resolution order

# print(IndexError.__mro__)
# print(KeyError.__mro__)

# we can catch both IndexError and KeyError by catching theit common parent class LookupError

# def lookups():

#     s = [1, 2, 3]
#     try:
#         print(s[4])
#     # except IndexError:
#     except LookupError:
#         print("Handled IndexError")

#     d = dict(a=1, b=2, c=3)
#     try:
#         print(d['d'])
#     # except KeyError:
#     except LookupError:
#         print("Handled KeyError")

# lookups()

# Python exceptions hierarchy: https://docs.python.org/3/library/exceptions.html


#-------------------------------------------
# Exception Payloads
#-------------------------------------------

# Most exceptions contains smple payload
# which contains dagnostic information about what caused an exception
# Most exceptions accepts a single string in their constructor

# def median(iterable):
#     items = sorted(iterable)
#     median_index = (len(items)-1) // 2
#     if len(items) % 2 != 0:
#         return items[median_index]
#     return (items[median_index] + items[median_index+1]) / 2

# m = median([1,2,3,4])
# print(m)
# m = median([1,2,3,4,5])
# print(m)
# m = median([])
# print(m)

# IndexError: list index out of range
# Payload: list index out of range

# lets add guard clause and raise ValueError
# def median(iterable):
#     items = sorted(iterable)
#     if len(items) == 0:
#         raise ValueError("median() arg is an empty serie")
#     median_index = (len(items)-1) // 2
#     if len(items) % 2 != 0:
#         return items[median_index]
#     return (items[median_index] + items[median_index+1]) / 2

# m = median([])
# print(m)

# ValueError: median() arg is an empty serie
# Payload: median() arg is an empty serie

# Retrieve payload informations
# def main():
#     try:
#         _ = median([])
#     except ValueError as e:
#         print("Payload: ", e.args)
#         print("Payload repr: ", repr(e))
#         print("Payload str: ", str(e))

# main()

# Payload:  ('median() arg is an empty serie',)
# Payload repr:  ValueError('median() arg is an empty serie')
# Payload str:  median() arg is an empty serie

# PEP 352 -> only single string argument should be passed as payload information

# some exceptions provide more informations as named attributes (not as payload)
# def main():
#     try:
#         b'\x81'.decode('utf-8')
#     except UnicodeError as e:
#         print(e)
#         print(e.encoding)
#         print(e.reason)
#         print(e.object)
#         print(e.start)
#         print(e.end)

# main()


#-------------------------------------------
# User defined exceptions
#-------------------------------------------

# import math

# def triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     a = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return(a)

# print(triangle_area(3, 4, 5))
# print(triangle_area(3, 4, 10))

# ValueError: math domain error
# We would like to raise our own TraingleError exception
# We should subclass Exception, not BaseException

# class TriangleError(Exception):
#     pass

# import math

# def triangle_area(a, b, c):
#     sides = sorted((a, b, c))
#     if sides[2] > sides[0] + sides[1]:
#         raise TriangleError("Illegal triangle")
#     p = (a + b + c) / 2
#     a = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return(a)

# print(triangle_area(3, 4, 10))


# lets modify our exception to accept more data about the "exceptional" triangle

# class TriangleError(Exception):
    
#     # Override __init__, which now accepts payload and collection of side lenghts
#     def __init__(self, text, sides):
#         # Payload is forwarded to base class for storage
#         super().__init__(text)
#         # side lenghts are storred in instance attribute of on the derived class
#         # stored as tuple to prevent modification
#         self._sides = tuple(sides)

#     # provide read only attribute to access sides tuple
#     @property
#     def sides(self):
#         return self._sides
    
#     def __str__(self):
#         return "'{}' for sides {}".format(self.args[0], self._sides)

#     def __repr__(self):
#         return "TriangleError({!r}, {!r})".format(self.args[0], self._sides)

# import math

# def triangle_area(a, b, c):
#     sides = sorted((a, b, c))
#     if sides[2] > sides[0] + sides[1]:
#         raise TriangleError("Illegal triangle", sides)
#     p = (a + b + c) / 2
#     a = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return(a)

# # print(triangle_area(3, 4, 10))
# try:
#     print(triangle_area(3, 4, 10))
# except TriangleError as e:
#     print(e.sides)
#     print("repr: ", repr(e))
#     print("str: ", str(e))


#-------------------------------------------
# Exception chaining
#-------------------------------------------

# Python only supports 1 exception beeing raised at the time
# But it provides a way to chain exceptions, so the full context can be communicated

#----------------------
# Implicit chaining
# occurs, when exception is raised incidentally during processing of another
# original exception is storred in the __context__ attribute of the second

# class TriangleError(Exception):
    
#     def __init__(self, text, sides):
#         super().__init__(text)
#         self._sides = tuple(sides)

#     @property
#     def sides(self):
#         return self._sides
    
#     def __str__(self):
#         return "'{}' for sides {}".format(self.args[0], self._sides)

#     def __repr__(self):
#         return "TriangleError({!r}, {!r})".format(self.args[0], self._sides)

# import math
# import sys
# import io

# def triangle_area(a, b, c):
#     sides = sorted((a, b, c))
#     if sides[2] > sides[0] + sides[1]:
#         raise TriangleError("Illegal triangle", sides)
#     p = (a + b + c) / 2
#     a = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return(a)

# def main():
#     try:
#         # first exception
#         print(triangle_area(3, 4, 10))
#     except TriangleError as e:
#         # second exception
#         print(e, file=sys.stdin)

# main()

# During handling of the above exception, another exception occurred:

# TriangleError was attached to the __context__ attribute of io.UnsupportedOperation object

# def main():
#     try:
#         # first exception
#         print(triangle_area(3, 4, 10))
#     except TriangleError as e:
#         # second exception
#         try:
#             print(e, file=sys.stdin)
#         except io.UnsupportedOperation as f:
#             print(e)
#             print(f)
#             print(f.__context__ is e)
#             print(type(f.__context__))
#             print(f.__context__)
#             print(f.__context__.sides)

# main()

#----------------------
# Explicit chaining
# we explicitely associate an exception with a new exception at the point of raising the latter
# this is done in the process of translating one exception to another

# import math

# class InclinationError(Exception):
#     pass

# def inclination(dx, dy):
#     try:
#         return math.degrees(math.atan(dy / dx))
#     except ZeroDivisionError as e:
#         # from e -> syntax for explicit chaining
#         # associates new exception with original exception using __cause__ attribute
#         # unlike implicit chaining, which is using __context__
#         raise InclinationError("Slope can not be vertical") from e

# # print(inclination(2,2))
# # fails with ZeroDivisionError
# # print(inclination(0,2))

# try:
#     inclination(0,2)
# except InclinationError as e:
#     print(e)
#     print(e.__context__)



#-------------------------------------------
# Tracebacks
#-------------------------------------------

# Every exception object has __traceback__ attribute, which holds reference to the traceback object

# import math
# from traceback import print_tb, format_tb

# class InclinationError(Exception):
#     pass

# def inclination(dx, dy):
#     try:
#         return math.degrees(math.atan(dy / dx))
#     except ZeroDivisionError as e:
#         # from e -> syntax for explicit chaining
#         # associates new exception with original exception using __cause__ attribute
#         # unlike implicit chaining, which is using __context__
#         raise InclinationError("Slope can not be vertical") from e

# def main():
#     try:
#         inclination(0,2)
#     except InclinationError as e:
#         # prints traceback object
#         # to do anything usefull with traceback object
#         # we need to use python standart library traceback
#         print(e.__traceback__)
#         print_tb(e.__traceback__)
#         print(format_tb(e.__traceback__))

#     print("Finished")

# main()

# <traceback object at 0x000001EC59AEFF40>
#   File "d:\python_work\pluralsight\robust_resource_and_error_handling\main.py", line 331, in main
#     inclination(0,2)
#   File "d:\python_work\pluralsight\robust_resource_and_error_handling\main.py", line 327, in inclination
#     raise InclinationError("Slope can not be vertical") from e
# Finished

# to be able to get hold of traceback informations
# is important for example for logging of handled exceptions
# many more functions are available in traceback module
# avoid keeping references to the traceback ojects, as it can quicky consume lot of memory

#-------------------------------------------
# Assertions
#-------------------------------------------

# syntax:
# assert condition [, message]
# condition = boolean expression
# -> if is False, AssertionError is raised causing program to terminate
# message =optional error message
# -> is used as AssertionError exception payload

# assert False, "The condition was false."

# Purpoe of assertions:
# document conditions your programm expects
# they should only be used to verify that your implementation is correct
# so only to check, if programmer made a mistake
# should not be used to validata arguments, as they are under control of caller, not the one who implemented function
# wrong argument should raaise ValueError

# Example
# from bisect import bisect_left

# class SortedSet:
#     def __init__(self, xs):
#         self._set = []
#         for x in xs:
#             self.add(x)
    
#     def add(self, x):
#         self._set.append(x)
#         self._set = sorted(set(self._set))
#         assert self._is_unique_and_sorted()

#     def contains(self, x):
#         assert self._is_unique_and_sorted()
#         index = bisect_left(self._set, x)
#         return index != len(self._set) and self._set[index] == x

#     def _is_unique_and_sorted(self):
#         return all(self._set[i] < self._set[i + 1] for i in range(len(self._set) - 1))

# s = SortedSet([1, 2, 3, 5, 6, 7, 7, 0, 0])
# print(s._set)
# s.add(10)
# print(s._set)
# s.add(10)
# print(s._set)


# Disabling assertions
# python -O (O as Optimized mode)

# from timeit import timeit
# from random import randrange

# print(timeit(
#     setup="from __main__ import SortedSet; from random import randrange",
#     stmt="s = SortedSet(randrange(1000) for _ in (range(2000)))",
#     number=100
# ))

# python main.py -> 6sec
# python -O main.py -> 1sec

# def wrap(text, line_length):

#     # do not use assert for validating args, just use ValueError
#     if line_length < 1:
#         raise ValueError("line length {} is not positive".format(line_length))

#     words = text.split()

#     # validate too long words, again, do not use assert
#     if max(map(len, words)) > line_length:
#         raise ValueError("line length must be at least as long as longest word")

#     lines_of_words = []
#     current_line_length = line_length
#     for word in words:
#         if current_line_length + len(word) > line_length:
#             lines_of_words.append([]) # new line
#             current_line_length = 0
#         lines_of_words[-1].append(word)
#         # current_line_length += len(word)
#         # fix assert
#         current_line_length += len(word) + len(' ')
#     lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
#     result = '\n'.join(lines)
#     # assert result before returning
#     assert all(len(line) <= line_length for line in result.splitlines())
#     return result

# text = 'ewfwf flonew fnwof wfnwofnwe fbneof iwfbnewiof ibffb ifbif ibfbf kfbwfb bfkbf ifbwifbwi wfbwifbwf wfibw fwibfwif wf iwfbwfib bf f f f fkifb fbiqfb'
# print(wrap(text,20))
# print(wrap(text,0))
# print(wrap(text,2))
# print(wrap(text,10))


#-------------------------------------------
# Context managers
#-------------------------------------------

# context manager is object designed to be used in with statement
# syntax
# with expresion:
#     with-block
# expresion must evaluate to a context manager
# context manager implements 2 methods, which are used by a with statement
# 1st method is called before with-block executes
# 2nd method is called after with-block executes, even is it ends with exception
# 1st method   - 2nd method
# construction - destruction
# setup        - teardown
# allocation   - deallocation
# enter        - exit

# context manager is object that ensures are properly and automatically handled
# "enter" method ensures that the resuorce is ready to be used in with-block
# "exit" method ensures that the resuorce is properly cleaned up after with-block ends

# as example, file is context manager
# file object returned by open() is contex manager
# with open('__tmp.txt', 'wt') as f:
#     f.write("Context manager example.")

# context manager protocol
# for an objec to be a context manager it needs to support context manager protocol
# context manager protocol consists of 2 methods
# __enter__() and __exit__()

# Context manager algorithm
# 1. expresion is executed and must return context manager object
# 2. __enter__() method of object from step 1 is called with no arguments
# 3. if __enter__() method ends with exception, then with-block is not executed and with statement is done
# 3. if with statement has "as x" clause, than return value of __enter__() method is bound to the name "x", otherwise is discarded
# 4. with-block itself is executed
# 5. after with-block either finish succesfully or ends with exception, __exit__() is executed
# 6. if __exit__() ends sucessfully, then no information is passed as arguments
# 7. if __exit__() ends with exception, then exception information is passed as arguments

# from traceback import print_tb

# class LoggingContextManager:

#     def __enter__(self):
#         # return self
#         # print('LoggingContextManager.__enter__()')
#         return "You are in with-block"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('LoggingContextManager.__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
#         # print_tb(exc_tb)
#         return

# # with LoggingContextManager() as x:
# #     print("x = ", x)

# with LoggingContextManager() as x:
#     raise ValueError("Something is wrong")

# normally, __exit__() reacts differently when exception is thrown

# class LoggingContextManager:

#     def __enter__(self):
#         print('LoggingContextManager.__enter__()')
#         return "You are in with-block"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             print('LoggingContextManager.__exit__: Normal exit')
#         else:
#             print('LoggingContextManager.__exit__: '
#                   'Exception detected. '
#                   'type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))

# with LoggingContextManager() as x:
#     pass

# with LoggingContextManager() as x:
#     raise ValueError("Something is wrong")

# by default, __exit__() will propagate exceptions from the with-block to the enclosing context
# __exit__() return a Falsy value, exception will be propagated
# this means, __exit__() should not re-raise the exception it receives from with-block, it should just simply return Falsy value (like None)
# __exit__() should only raise exceptions if something goes wrong in the dunction itself

# try:
#     with LoggingContextManager() as x:
#         raise ValueError("Something is wrong")
# except ValueError:
#     print('***Value error escaped the with-block***')

# with statement was originally defined in PEP 343


#-------------------------------------------
# Context manager decorators
#-------------------------------------------

# contextlib - standart Python library, that "provide utilities for common tasks involving the with statement"
# contextmanager from contextlib is decorator for creating new context managers

# abstract example from web
# from contextlib import contextmanager

# @contextmanager
# def managed_resource(*args, **kwds):
#     # Code to acquire resource, e.g.:
#     resource = acquire_resource(*args, **kwds)
#     try:
#         yield resource
#     finally:
#         # Code to release resource, e.g.:
#         release_resource(resource)


# my own try to simulate contextmanager decorator
# class GenericContextManager:

#     def __init__(self, f):
#         print("2. Init")
#         print(f)
#         self._f = f

#     def __enter__(self):
#         print("3. Enter class")
#         print(self._f)
#         self._g = self._f()
#         return next(self._g)

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             next(self._g)
#         except StopIteration:
#             pass

# def context_manager_decorator(f):
#     def wrap():
#         print("1. Decorator")
#         print(f)
#         g = GenericContextManager(f)
#         return g
#     return wrap

# @context_manager_decorator
# def my_context_manager():
#     print('Open my resource for the processing of with block')
#     try:
#         yield 'My resource'
#         print('Normal exit')
#     except Exception:
#         print('Exception exit')
#     finally:
#         print("Release resource")

# with my_context_manager() as x:
#     print("Printing x")
#     print(x)
#     print("My with block")


# in order to use contextmanager decorator
# we need to have generator function with excatly 1 yield
# adantage:
# no need to have class with 2 methods
# sice generators remember its state, you dont need to define new class just to create statefull context manager
# exceptions needs to be raised explicitelly

# from contextlib import contextmanager
# import sys

# @contextmanager
# def LoggingContextManager():
# # __enter__ start

#     print('LoggingContextManager: enter')
#     try:
#         print('LoggingContextManager: yield my resource to assign it to name reference in with block')
#         yield 1
# # __enter__ end

# # __exit__ normal exit start
#         print('LoggingContextManager: normal exit')
# # __exit__ normal exit end

# # __exit__ with exception start
#     except Exception:
#         print('LoggingContextManager: exceptional exit', sys.exc_info())
#         # raise
# # __exit__ with exception end

# # __exit__ finally start
#     finally:
#         # Code to release resource, e.g.:
#         print('LoggingContextManager: finally exit')
#         print('LoggingContextManager: release my resource to assign it to name reference in with block')
# # __exit__ finally end

# # with LoggingContextManager() as x:
# #     print(x)

# with LoggingContextManager() as x:
#     print(x)
#     # nor propagated if nor re-reised in except block when we catched it in our generator
#     raise ValueError("Something is wrong")


#-------------------------------------------
# Multiple Context managers in single WITH
#-------------------------------------------
# syntax:
# WITH cm1 as a, cm2 as b:
#....body...
# equivalent to:
# WITH cm1 as a:
#     WITH cm2 as b:
#........body.......

# from contextlib import contextmanager

# @contextmanager
# def nest_test(name):
#     print('Entering', name)
#     yield name
#     print('Exiting', name)

# with nest_test('outer'), nest_test('inner'):
#     print('BODY')
# same as
# with nest_test('outer'):
#     with nest_test('inner'):
#         print('BODY')

# we can use yielded object from outer context managers in inner context managers

# from contextlib import contextmanager

# @contextmanager
# def nest_test(name):
#     print('Entering', name)
#     yield name
#     print('Exiting', name)

# with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
#     print('BODY')

# exceptions (if raised) from inner context manager are propagated to outer context manager

# from contextlib import contextmanager

# @contextmanager
# def propagater(name, propagate):
#     try:
#         yield
#         print(name, 'exited normally')
#     except Exception:
#         print(name, 'received an exception')
#         if propagate:
#             raise

# with propagater('outer', True) as n1, propagater('inner', False) as n2:
#     print('BODY')
#     raise TypeError()

# with propagater('outer', False) as n1, propagater('inner', True) as n2:
#     print('BODY')
#     raise TypeError()

# line continuation can be used to split nested context managers to multiple lines for netter code formating
# or you can alse use with nestting
# with propagater('cm1', True) as n1, \
#      propagater('cm2', True) as n2, \
#      propagater('cm3', True) as n3:
#     print('BODY')


#-------------------------------------------
# Mdelling DB transactions with context managers
#-------------------------------------------

# class Connection:
#     def __init__(self):
#         self.xid = 0
    
#     def _start_transaction(self):
#         print('starting transaction', self.xid)
#         rslt = self.xid
#         self.xid += 1
#         return rslt
    
#     def _commit_transaction(self, xid):
#         print('committing transaction', xid)

#     def _rollback_transaction(self, xid):
#         print('rolling back transaction', xid)


# class Transaction:
#     def __init__(self, conn):
#         self.conn = conn
#         self.xid = conn._start_transaction()
    
#     def commit(self):
#         self.conn._commit_transaction(self.xid)

#     def rollback(self):
#         self.conn._rollback_transaction(self.xid)


# conn = Connection()
# trx = Transaction(conn)
# trx.commit()

# from contextlib import contextmanager

# @contextmanager
# def start_transaction(connection):
#     tx = Transaction(connection)
#     try:
#         yield
#     except:
#         tx.rollback()
#         raise
#     tx.commit()

# conn = Connection()

# try:
#     with start_transaction(conn):
#         x = 1 + 1
#         raise ValueError()
#         y = x + 2
#         print(f"transaction => {x} {y}")
# except ValueError:
#     print('Operation failed')

# try:
#     with start_transaction(conn):
#         x = 1 + 1
#         y = x + 2
#         print(f"transaction => {x} {y}")
# except ValueError:
#     assert False

