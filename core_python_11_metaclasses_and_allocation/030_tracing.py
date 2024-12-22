# what is Python doing on class definition
# this
# class Widget:
#     pass
# same as this
# class Widget(object, metaclass=type):
#     pass

# name = 'Widget'
# metaclass = type
# bases = () # this is for base classes other than imlicit object
# kwargs = {} # ena keyword arguments following metaclass= in the class definition
# namespace = metaclass.__prepare__(name, bases, **kwargs)
# Widget = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
# metaclass.__init__(Widget, name, bases, namespace, **kwargs)

class TracingMeta(type):

    # __prepare__ used to create the namespace object for the class, usually empty dictionary
    # __prepare__ is explicit class method of metaclass
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print(f"   {mcs=}")
        print(f"   {name=}")
        print(f"   {bases=}")
        print(f"   {kwargs=}")
        namespace = super().__prepare__(name, bases)
        print(f"-> {namespace=}")
        print()
        return namespace

    # __new__ used to create new class object
    # __new__ is inplicit class method of metaclass
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("TracingMeta.__new__(mcs, name, bases, namespace)")
        print(f"   {mcs=}")
        print(f"   {name=}")
        print(f"   {bases=}")
        print(f"   {namespace=}")
        print(f"   {kwargs=}")
        cls = super().__new__(mcs, name, bases, namespace)
        print(f"-> {cls=}")
        print()
        return cls

    # __init__ used to configure newly created class object
    # __init__ is instance method of metaclass
    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__(cls, name, bases, namespace)")
        print(f"   {cls=}")
        print(f"   {name=}")
        # we could modify sequence of base classes
        print(f"   {bases=}")
        # we could modify namespace before call to super() and this for example add new method, etc
        print(f"   {namespace=}")
        print(f"   {kwargs=}")
        # we could allocate completelly new class, but it is rarely needed
        cls = super().__init__(name, bases, namespace)
        print()

    # regular method of metaclass can be access as class method of the class 
    def metamethod(cls):
        print("TracingMeta.metamethod(cls)")
        print(f"   {cls=}")

    def __call__(cls, *args, **kwargs):
        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print(f"   {cls=}")
        print(f"   {args=}")
        print(f"   {kwargs=}")
        print("About to call type.__call__")
        obj = super().__call__(*args, **kwargs)
        print("Returned from type.__call__")
        print(f"   {obj=}")
        print()
        return obj


# what are the use cases to override each of the metaclass methods __prepare__, __new__ and __init__
# __prepare__ => if we want to customize the type or initial value of namespace mapping type (could be any mapping type, not only dict)
# __new__     => if we want to configure class object before it gets created
# __init__    => if we want to configure class object after  it gets created

# class Widget(metaclass=TracingMeta):
#     the_answer = 42
#     def action(self, message):
#         print(message)


# Output when running code for the class definition

# TracingMeta.__prepare__(name, bases, **kwargs)
#    mcs=<class '__main__.TracingMeta'>
#    name='Widget'
#    bases=()
#    kwargs={}
# -> namespace={}

# TracingMeta.__new__(mcs, name, bases, namespace)
#    mcs=<class '__main__.TracingMeta'>
#    name='Widget'
#    bases=()
#    namespace={'__module__': '__main__', '__qualname__': 'Widget', 'the_answer': 42, 'action': <function Widget.action at 0x0000022E35A99E40>}
#    kwargs={}
# -> cls=<class '__main__.Widget'>

# TracingMeta.__init__(cls, name, bases, namespace)
#    cls=<class '__main__.Widget'>
#    name='Widget'
#    bases=()
#    namespace={'__module__': '__main__', '__qualname__': 'Widget', 'the_answer': 42, 'action': <function Widget.action at 0x0000022E35A99E40>}
#    kwargs={}

# metaclass keyword arguments

# class EntriesMeta(type):

#     def __new__(mcs, name, bases, namespace, num_entries):
#         print("EntriesMeta.__new__(mcs, name, bases, namespace, num_entries)")
#         print(f"   {kwargs=}")
#         namespace.update({chr(i): i for i in range(ord("a"), ord("a")+num_entries)})
#         cls = super().__new__(mcs, name, bases, namespace)
#         return cls

# class AtoZ(metaclass=EntriesMeta, num_entries=26):
#     pass

# class AtoZ():
#     f = 100

# print(dir(AtoZ))
# print(AtoZ.f)

# metamethod
# class Widget(metaclass=TracingMeta, ):
#     pass

# Widget.metamethod()
# # metamethod is not accesible from class instance
# w = Widget()
# w.metamethod()

# metaclass __call__
# when creating new instance from class, then __call__ method of metaclass is called
# __call__ method of metaclass is then calling __new__ and __init__ methods of class

class TracingClass(metaclass=TracingMeta):

    def __new__(cls, *args, **kwargs):
        print("TracingClass.__new__(cls, *args, **kwargs)")
        print(f"   {cls=}")
        print(f"   {args=}")
        print(f"   {kwargs=}")
        obj = super().__new__(cls)
        print(f"   {obj=}")
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print("TracingClass.__init__(self, *args, **kwargs)")
        print(f"   {self=}")
        print(f"   {args=}")
        print(f"   {kwargs=}")
        print()

pass

# just by runnning class definition of TracingClass, metaclass __prepare__, __new__ and __init__ are invoked
# output
# TracingMeta.__prepare__(name, bases, **kwargs)
#    mcs=<class '__main__.TracingMeta'>
#    name='TracingClass'
#    bases=()
#    kwargs={}
# -> namespace={}

# TracingMeta.__new__(mcs, name, bases, namespace)
#    mcs=<class '__main__.TracingMeta'>
#    name='TracingClass'
#    bases=()
#    namespace={'__module__': '__main__', '__qualname__': 'TracingClass', '__new__': <function TracingClass.__new__ at 0x00000141ED669EE0>, '__init__': <function TracingClass.__init__ at 0x00000141ED669F80>, '__classcell__': <cell at 0x00000141ED673C70: empty>}
#    kwargs={}
# -> cls=<class '__main__.TracingClass'>

# TracingMeta.__init__(cls, name, bases, namespace)
#    cls=<class '__main__.TracingClass'>
#    name='TracingClass'
#    bases=()
#    namespace={'__module__': '__main__', '__qualname__': 'TracingClass', '__new__': <function TracingClass.__new__ at 0x00000141ED669EE0>, '__init__': <function TracingClass.__init__ at 0x00000141ED669F80>, '__classcell__': <cell at 0x00000141ED673C70: TracingMeta object at 0x00000141ED56AF40>}
#    kwargs={}

t = TracingClass(42, keyword="clef")

# TracingMeta.__call__(cls, *args, **kwargs)
#    cls=<class '__main__.TracingClass'>
#    args=(42,)
#    kwargs={'keyword': 'clef'}
# About to call type.__call__
# TracingClass.__new__(cls, *args, **kwargs)
#    cls=<class '__main__.TracingClass'>
#    args=(42,)
#    kwargs={'keyword': 'clef'}
#    obj=<__main__.TracingClass object at 0x0000021E41C9EF10>

# TracingClass.__init__(cls, *args, **kwargs)
#    self=<__main__.TracingClass object at 0x0000021E41C9EF10>
#    args=(42,)
#    kwargs={'keyword': 'clef'}

# Returned from type.__call__
#    obj=<__main__.TracingClass object at 0x0000021E41C9EF10>


# what is the usecase of overriding __call__ on metaclass
# phased initialization
# if we have 3 phazed initialization, pre_init, init, post_init
# it is better to place it into __call__ methof of metaclass instead of into __init__ of class
# this way we can better override __init__ only method in subclasses without impacting pre_init and post_init
# compared to if these would be in the __init__ of class
# see phased.py

# custom namespace distionaries
# see dodgy.py

