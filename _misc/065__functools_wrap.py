import functools

def my_decorator(f):

    @functools.wraps(f)
    def wrapper():
        return f()

    # wrapper.__name__ = f.__name__
    # wrapper.__doc__ = f.__doc__

    return wrapper

@my_decorator
def my_function():

    "My function doc"
    print("My function return")


print(my_function.__name__)
print(my_function.__doc__)

my_function()

