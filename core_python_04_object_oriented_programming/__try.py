# class Addition:

#     def __call__(self, *args, **kwargs):
#         return self.run(*args, **kwargs)
    
#     def run(self, *args, **kwargs):
#         return NotImplementedError('Subclass must implement run')

# def addition(decorated):

#     class AdditionSubclass(Addition):

#         def run(self, *args, **kwargs):

#             if args:
#                 add = 0
#                 for arg in args:
#                     add += arg
#                 return add
#             else:
#                 return 0

#     return AdditionSubclass()

# @addition
# def my_adding_function(*args):
#     pass

# print(type(my_adding_function).run(my_adding_function,1,2,3,4))

# print(my_adding_function.run(1,2,3,4))

# def decorator_func(f):

#     class Decorator():

#         def __init__(self):
#             self._lf = []

#         def __call__(self, seq):
#             print("Decorator")
#             print(seq)
#             self._lf[seq]()
        
#         def register(self, f):

#             print("register")
#             self._lf.append(f)
#             print(self._lf)

#             # def wrapper(self, f):
#             #     print("wrapper")
#             #     f()
#             # return wrapper

#     return Decorator()


# @decorator_func
# def my_func():
#     print("my_func")
#     return 1


# @my_func.register
# def _():
#     print("func1")

# @my_func.register
# def _():
#     print("func2")

# @my_func.register
# def _():
#     print("func3")

# my_func(2)


# def my_decorator(f):
#     print("decorator")
#     return(f)

# @my_decorator
# def my_func():
#     print("func")

# my_func()

class My_class:
    # def __bool__(self):
    #     return False
    pass


mc = My_class()

print(bool(mc))
