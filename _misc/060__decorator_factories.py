def my_condition(condition):
    # print("my_condition", condition)

    def funtion_decorator(f):
        # print("funtion_decorator", condition, f)
        def wrapper(self, x):
            if condition(x):
                raise RuntimeError("Parameter is not within range")
            f(self, x)
    
        return wrapper
    
    return funtion_decorator


def check_min_2(x):
    # print("check_min_2")
    return x < 2

def check_max_10(x):
    # print("check_max_10")
    return x > 10

class A:

    @my_condition(check_min_2)
    @my_condition(check_max_10)
    def __init__(self, x):
        # print("init")
        self._x = x

A(10)

