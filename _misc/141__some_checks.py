# multiple class decorators

def my_new_func_1(f):

    def wrapper(self):
        f(self)
        print("1")
        # return 1

    return wrapper


def my_new_func_2(f):

    def wrapper(self):
        f(self)
        print("2")
        # return 2

    return wrapper


def my_class_decorator_1(cls):
    # print("decorating 1")
    # print(vars(cls))
    decorated = my_new_func_1(cls.my_function)
    setattr(cls, "my_function", decorated)
    # print(vars(cls))
    return cls

def my_class_decorator_2(cls):
    # print("decorating 2")
    # print(vars(cls))
    decorated = my_new_func_2(cls.my_function)
    setattr(cls, "my_function", decorated)
    # print(vars(cls))
    return cls


@my_class_decorator_2
@my_class_decorator_1
class MyTestClass:
    
    def my_function(self):
        print("0")

# print(vars(MyTestClass))

t = MyTestClass()
t.my_function()