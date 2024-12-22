# ##############################
# Abstract base classes
# ##############################

# serve 2 general purposes
# 1. provide mechanism for defining interfaces or protocols an ensure impementors of those protocols meet minimum requirements
# 2. provide a means to determine, whether class or instance meet the requirement of specific protocol

# from collections.abc import MutableSequence

# ms = MutableSequence()
# TypeError: Can't instantiate abstract class MyMS without an implementation for abstract methods '__delitem__', '__getitem__', '__len__', '__setitem__', 'insert'

# print(MutableSequence.__bases__)
# print(MutableSequence.__mro__)

# print(type(MutableSequence))

# print(type(type(MutableSequence)))

# print(issubclass(list, MutableSequence))
# why True
# issubclass checks on meta class of MutableSequence if it has __subclasscheck__ method, if yes, it uses it to check
# in other words, metaclass of class decides, if other class is subclass of it


# class MyInterfaceMeta(type):
#     def __subclasscheck__(cls, subclass):
#         # print(self)
#         # print(subclass)

#         if hasattr(subclass, "my_function") and callable(subclass.my_function):
#             return True
#         else:
#             return super().__subclasscheck__(subclass)
    
#     def __instancecheck__(cls, instance):
#         return issubclass(type(instance), cls)
    
#     def __call__(cls, *args, **kwargs):
#         if hasattr(cls, "my_function") and callable(cls.my_function):
#             super().__call__(*args, **kwargs)
#         else:
#             raise TypeError(f"Can't instantiate abstract class {cls.__name__} without implementing my_function")


# class MyInterface(metaclass=MyInterfaceMeta):
#     pass


# class MyInterfaceVariant1:
#     def my_function(self):
#         pass

# class MyInterfaceVariant2:
#     def my_function(self):
#         pass

# class NotMyInterfaceVariant():
#     pass

# print(issubclass(MyInterfaceVariant1, MyInterface))
# print(issubclass(MyInterfaceVariant2, MyInterface))
# print(issubclass(NotMyInterfaceVariant, MyInterface))

# i1 = MyInterfaceVariant1()

# print(isinstance(i1, MyInterfaceVariant1))
# print(isinstance(i1, MyInterface))
# print(isinstance(i1, object))

# i1 = MyInterface()

# class MyAbstractClass():
#     """My abstract base class"""

# ##############################
# Abstract base classes provided by Python as standart libraries
# ##############################

# Python standart library provides support for Abstract Base Classes in abc module
# abc module provides : 
# ABCMeta metaclass
# ABC base class
# @register class decorator
# @abstractmethod decorator


# ##############################
# ABCMeta metaclass
# implements reliable __subclasscheck__ and __instancecheck__ methods
# both of these methods calls __subclasshook__ method on class, which then can decide, if subclass is or is not its subclass
# all Python objects has __subclasshook__ method
# accepts subclass as its only argument
# should return True, False or NotImplemented
# if NotImplemented is return, then __subclasscheck__ is done on MRO

# print(dir(type))
# print(dir(object))

# print(object.__subclasshook__(int))

# from abc import ABCMeta

# class MyInterface(metaclass=ABCMeta):

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         # print(cls, subclass)
#         return (
#             hasattr(subclass, "my_function")
#             and
#             callable(subclass.my_function)
#         )

# class MyInterfaceVariant1:
#     def my_function(self):
#         pass

# class MyInterfaceVariant2:
#     def my_function(self):
#         pass

# class NotMyInterfaceVariant():
#     pass

# print(issubclass(MyInterfaceVariant1, MyInterface))
# print(issubclass(MyInterfaceVariant2, MyInterface))
# print(issubclass(NotMyInterfaceVariant, MyInterface))

# i1 = MyInterfaceVariant1()

# print(isinstance(i1, MyInterfaceVariant1))
# print(isinstance(i1, MyInterface))
# print(isinstance(i1, object))


# ##############################
# Virtual subclass registration
# @register class decorator from ABCMeta

# from abc import ABCMeta

# class Text(metaclass=ABCMeta):
#     pass

# print(dir(Text))
# print(issubclass(str, Text))
# print(isinstance("str", Text))
# print(Text.register(str))
# print(issubclass(str, Text))
# print(isinstance("str", Text))

# register returns class passed to it, so it can be used as decorator

# @Text.register
# class Prose:
#     pass

# print(issubclass(Prose, Text))


# my own register metaclass
# class MyMetaRegister(type):

#     _registry = {}

#     def my_register(cls, subclass):
#         # type(cls)._registry[cls] = subclass
#         print(cls._registry)
#         return subclass
    
#     def __subclasscheck__(cls, subclass):
#         if cls in type(cls)._registry:
#             return True
#         else:
#             return NotImplemented


# class MyParentClass(metaclass=MyMetaRegister):
#     pass


# @MyParentClass.my_register
# class MyVirtualSubclass:
#     pass

# print(issubclass(MyVirtualSubclass, MyParentClass))




# ##############################
# __subclasshook__ takes precedence over @register
# if you want @register to work, __subclasshook__ must return NotImplemented


# from abc import ABCMeta

# class MyInterface(metaclass=ABCMeta):

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         # print(cls, subclass)
#         return (
#             (
#             hasattr(subclass, "my_function")
#             and
#             callable(subclass.my_function)
#             )
#             or
#             NotImplemented
#         )

# class MyInterfaceVariant1:
#     def my_function(self):
#         pass

# @MyInterface.register
# class MyregisteredInterfaceVariant2:
#     pass

# class NotMyInterfaceVariant():
#     pass

# print(issubclass(MyInterfaceVariant1, MyInterface))
# print(issubclass(MyregisteredInterfaceVariant2, MyInterface))
# print(issubclass(NotMyInterfaceVariant, MyInterface))



# ##############################
# ABC class
# is dummy class with ABCMeta as its metaclass
# is preffered to inherit from ABC class instead of usint ABCMeta as metaclass

# from abc import ABC

# class MyInterface(ABC):

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         # print(cls, subclass)
#         return (
#             (
#             hasattr(subclass, "my_function")
#             and
#             callable(subclass.my_function)
#             )
#             or
#             NotImplemented
#         )

# class MyInterfaceVariant1:
#     def my_function(self):
#         pass

# @MyInterface.register
# class MyregisteredInterfaceVariant2:
#     pass

# class NotMyInterfaceVariant():
#     pass

# print(issubclass(MyInterfaceVariant1, MyInterface))
# print(issubclass(MyregisteredInterfaceVariant2, MyInterface))
# print(issubclass(NotMyInterfaceVariant, MyInterface))


# ##############################
# @abstractmethod decorator
# must be used only for classes with ABCMeta as metaclass (or classes which inherits from ABC)
# can be used in combination with other decorators
# @staticmethod
# @classmethod
# @property
# but it must be the innermost decorator
# @abstractmethod decorator sets __isabstractmethod__ = True attribute of decorated object
# any futher decorators must set this attribute __isabstractmethod__ accordingly and is responsibility of the decorator itself

# my own abstractmethod - very dummy implementation
# class MyMeta(type):

#     _registry = {}

#     @classmethod
#     def my_abstract_decorator(mcs, absract_method):
#         mcs._registry[absract_method.__name__] = id(absract_method)
#         print(mcs._registry)
#         return absract_method
    
#     def __call__(cls, *args, **kwargs):
#         print(cls)
#         for i in dir(cls):
#             if i in type(cls)._registry:
#                 # print(i)
#                 # print(id(getattr(cls, i)))
#                 if id(getattr(cls, i)) == type(cls)._registry[i]:
#                     print(f"Need to overide {i}")
#         super().__call__(*args, **kwargs)


# class MyAbstractBase(metaclass=MyMeta):

#     @MyMeta.my_abstract_decorator
#     def abstract_method_1(self):
#         return NotImplementedError

#     @MyMeta.my_abstract_decorator
#     def abstract_method_2(self):
#         return NotImplementedError

# class MyClass(MyAbstractBase):

#     def abstract_method_1(self):
#         pass

#     def abstract_method_2(self):
#         pass

# o = MyClass()

# from abc import ABC, abstractmethod


# class MyAbstractBase(ABC):

#     @abstractmethod
#     def my_abstract_mehod_1(self):
#         return NotImplementedError

#     @abstractmethod
#     def my_abstract_mehod_2(self):
#         return NotImplementedError


# class MyBase(MyAbstractBase):
#     pass

# print(MyAbstractBase.my_abstract_mehod_1.__isabstractmethod__)

# a = MyBase()


# ##############################
# applications
# flattening sequence with negatypes
# ##############################

# from abc import ABC

# class MyClass(ABC):
    
#     @classmethod
#     def __subclasshook__(cls, subclass):
#         print(cls)
#         print(subclass)

#         # only perform check on the class itself
#         # exclude checks on the subclasses
#         # but I do not know, why it is per also performed on subclasses
#         if cls is MyClass:
#             if issubclass(subclass, int):
#                 return False
#             else:
#                 return True

#         return NotImplemented

# class MySubClass(MyClass):
#     pass

# class MySubClass1(MyClass):
#     pass


# print(issubclass(int, MyClass))
# print(issubclass(str, MySubClass))

# print(MyClass.__mro__)

# from abc import ABC, abstractmethod
# from collections.abc import Iterable

# class NonStringIterable(ABC):

#     # this is to force pointless instantiations of this class
#     @abstractmethod
#     def __iter__(self):
#         raise NotImplementedError

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         if cls is NonStringIterable:
#             if issubclass(subclass, str):
#                 return False
#             if hasattr(subclass, "__iter__") and (subclass.__iter__ is not None):
#                 return True
#         return NotImplemented

# print(isinstance([1,2,3], NonStringIterable))
# print(isinstance("123", NonStringIterable))

# flatten list with any depth

# def flatten(items):

#     for item in items:
#         if isinstance(item, NonStringIterable):
#         # if isinstance(item, Iterable):
#             for inner_item in flatten(item):
#                 yield inner_item
#         else:
#             yield item

#         # try:
#         #     for inner_item in flatten(item):
#         #         yield inner_item
#         # except:
#         #     yield item

# my_list = [
#     1,
#     2,
#     [1, 2, 3],
#     4,
#     [1, 2, [
#         1, 2, 4, 2
#     ]
#     ],
#     "ssss"
# ]

# result = list(flatten(my_list))
# print(my_list)
# print(result)


# ##############################
# applications
# checking invariants
# ##############################

import functools
import inspect
from abc import ABC, abstractmethod

def postcondition(predicate):

    def function_decorator(f):

        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                r = object.__repr__(self)
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {r}"
                )
            return result
        
        return wrapper
    
    return function_decorator


class AbstractProperty(ABC):

    @abstractmethod
    def __get__(self, instance, owner=None):
        raise NotImplementedError

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError

    @abstractmethod
    def __delete__(self, instance):
        raise NotImplementedError

    @property
    @abstractmethod
    def __isabstractmethod__(self):
        raise NotImplementedError


AbstractProperty.register(property)


class InvariantProperty(AbstractProperty):
    
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def _check_predicate(self, instance):
        if not self._predicate(instance):
            r = object.__repr__(self)
            raise RuntimeError(
                f"Post-condition {self._predicate.__name__} not "
                f"maintained for {r}"
            )
    
    def __get__(self, instance, owner=None):
        result = self._referent.__get__(instance, owner)
        if instance is not None:
            self._check_predicate(instance)
        return result
    
    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        self._check_predicate(instance)
        return result
    
    def __delete__(self, instance):
        result = self._referent.__delete__(instance)
        self._check_predicate(instance)
        return result
    
    @property
    def __isabstractmethod__(self):
        return getattr(self._referent, "__isabstractmethod__", False)


def invariant(predicate):

    def class_decorator(cls):
        # print("decorating")
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                function_decorator = postcondition(predicate)
                decorated_member = function_decorator(member)
                # print("setting new class method")
                setattr(cls, name, decorated_member)
            # elif isinstance(member, property) or isinstance(member, InvariantProperty):
            elif isinstance(member, AbstractProperty):
                # print(member)
                proxy_property = InvariantProperty(member, predicate)
                # print(proxy_property)
                setattr(cls, name, proxy_property)
        return cls
    
    return class_decorator


def above_absolute_zero(temperature):
    # print("above_absolute_zero")
    return temperature._kelvin > 0


def below_absolute_hot(temperature):
    # print("below_absolute_hot")
    return temperature._kelvin <= 1.416785e32


@invariant(below_absolute_hot)
@invariant(above_absolute_zero)
class Temperature:

    # @postcondition(above_absolute_zero)
    def __init__(self, kelvin):
        self._kelvin = kelvin
    
    # @postcondition(above_absolute_zero)
    def get_kelvin(self):
        return self._kelvin
    
    # @postcondition(above_absolute_zero)
    def set_kelvin(self, value):
        self._kelvin = value
    
    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    # @postcondition(above_absolute_zero)
    def __repr__(self):
        return f"{type(self).__name__}(kelvin={self._kelvin})"

t = Temperature(500)
# print(t)

# t.set_kelvin(0)

t.celsius = -300
# print(t._kelvin)
# print("---")
# print(Temperature.get_kelvin)
# print(Temperature.celsius)
# print(Temperature.celsius._referent)
# print(Temperature.celsius._predicate)
