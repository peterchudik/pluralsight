# using metaclass

# class MyMeta(type):
#     def __new__(mcs, name, bases, namespace, **kwargs):
#         cls = super().__new__(mcs, name, bases, namespace)
#         cls._register(**kwargs)
#         return cls

# class MyBaseClass(metaclass=MyMeta):
#     _class_registry = {}

#     @classmethod
#     def _register(cls, register_as=None):
#         if register_as is None:
#             return
#         cls._class_registry[register_as] = cls


# class Child1(MyBaseClass, register_as="c1"):
#     pass


# class Child2(MyBaseClass, register_as="c2"):
#     pass

# print(MyBaseClass._class_registry)


# using __init_subclass__(cls)
# this method is called whenever the containing class is subclassed, cls is the new subclass


class MyBaseClass():
    _class_registry = {}

    @classmethod
    def __init_subclass__(cls, *, register_as, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._class_registry[register_as] = cls


class Child1(MyBaseClass, register_as="c1"):
    pass


class Child2(MyBaseClass, register_as="c2"):
    pass

print(MyBaseClass._class_registry)

