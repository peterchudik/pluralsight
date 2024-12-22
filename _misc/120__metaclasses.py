# class Test(object, metaclass=type):
#     pass

# steps which happens when class is created

# name = 'Test'
# metaclass = type
# bases = ()
# kwargs = {}
# namespace = metaclass.__prepare__(name, bases, **kwargs)
# here Python runtime populates namespace dictionary based on class definition
# Test = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
# metaclass.__init__(Test, name, bases, namespace, **kwargs)


# what are the use cases to override metaclass methods
# __prepare__ => if we want to customize the type or initial value of namespace mapping type (could be any mapping type, not only dict)
# __new__     => if we want to configure class object before it gets created
# __init__    => if we want to configure class object after  it gets created

class MyMeta(type):

    # regular methods of metaclass accepts class as first argument
    # these methods can be accessed through class, but not through instance of the class
    def new_repr(cls):
        print(type(cls))
        return "__repr__ added by metaclass"
    
    # class method of metaclass
    @classmethod
    def meta_class_method(mcs):
        print(type(mcs))
        return "meta class classmethod"

    def __new__(mcs, name, bases, namespace, **kwargs):
        namespace.update({"added_by_meta":10})
        namespace.update({"__repr__":MyMeta.new_repr})
        namespace.update(**kwargs)
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

def my_func(self, x):
    return x * x

class Dummy(metaclass=MyMeta, my_func=my_func):
    pass

print(dir(Dummy))
print(Dummy.new_repr())
print(Dummy.meta_class_method())
d1=Dummy()
# methods of metaclass are not accesible via class instance
# d1.meta_class_method
# d1.new_repr

# print(d1.added_by_meta)
# Dummy.added_by_meta = 20
# d2=Dummy()
# print(d2.added_by_meta)
# print(d1)

# print(d1.my_func(10))


# metaclass __call__
# when creating new instance from class (or calling the class using  Class()), then __call__ method of metaclass is called
# __call__ method of metaclass is then calling __new__ and __init__ methods of class

# class MyMeta(type):

#     def __call__(cls, *args, **kwargs):
#         print(f"You are about to create object from {cls.__name__}")
#         super().__call__(*args, **kwargs)
#         print(f"Object from {cls.__name__} has been created")

# class Dummy(metaclass=MyMeta):
#     pass

# d = Dummy()
