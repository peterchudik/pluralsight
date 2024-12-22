# -----------------------------------------------------------------------------------
# class attributes, methods and properties
# -----------------------------------------------------------------------------------


# from shipping import *

# c1 = ShippingContainer('YML', ['books'], 20)
# print(c1.owner_code)
# print(c1.contents)
# print(c1.my_class_attribute)
# print(c1.MY_CONSTANT)
# print(c1.bic)
# print(c1.next_serial)



# c2 = ShippingContainer('MAE', ['clothes'], 20)
# print(c2.owner_code)
# print(c2.contents)
# print(c2.my_class_attribute)
# print(c2.bic)
# print(c2.next_serial)


# # no need to create instanc of a class to see class attributes
# print(ShippingContainer.my_class_attribute)
# print(ShippingContainer.MY_CONSTANT)
# print(ShippingContainer.next_serial)
# # class attributes change also for existing class instances
# print(c1.next_serial)
# print(c2.next_serial)


# # using factory initializers
# c3 = ShippingContainer.create_empty('YML', 20)
# print(c3.owner_code)
# print(c3.contents)
# print(c3.bic)
# c4 = ShippingContainer.create_with_items('MAE', 40, {'books', 'clothes'})
# print(c4.owner_code)
# print(c4.contents)
# print(c4.bic)

# c5 = RefrigeratedShippingContainer.create_empty('MAE', 20, celsius = 3)
# print(c5.owner_code)
# print(c5.contents)
# print(c5.bic)
# print(c5.celsius)

# c6 = RefrigeratedShippingContainer.create_with_items('ESC', 40, {'onions'}, celsius = 4)
# print(c6.owner_code)
# print(c6.contents)
# print(c6.bic)
# print(c6.celsius)

# c7 = RefrigeratedShippingContainer('YML', 20, {'ice cream'}, celsius = 4)
# print(c7.owner_code)
# print(c7.contents)
# print(c7.bic)
# print(c7.celsius)
# c7.celsius = 3
# print(c7.celsius)
# print(c7.fahrenheit)
# c7.fahrenheit = 20
# print(c7.celsius)
# print(c7.volume_ft3)


# c8 = HeatedRefrigeratedShippingContainer('YML', 20, {'ice cream'}, celsius = 4)
# print(c8.celsius)
# c8.celsius = 3
# print(c8.celsius)
# # c8.celsius = -21
# # c8.celsius = 10


# from position import *

# -----------------------------------------------------------------------------------
# string representation of a class
# repr()
# str()
# format()
# -----------------------------------------------------------------------------------


# oslo = Position(60.0, 10.7)

# print(repr(oslo))
# # <position.Position object at 0x0000028AE2497C50>
# print(str(oslo))
# # <position.Position object at 0x0000028AE2497C50>
# print(format(oslo))
# # <position.Position object at 0x0000028AE2497C50>
# print(dir(object))
# # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
# # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
# # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# ------------------------------
# repr()
# ------------------------------
# print(oslo)
# r = repr(oslo)
# print(r)
# # eval() can run string as python code
# p = eval(r)
# print(p)
# print(p is r)

# print(oslo)
# print(dir(oslo))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# # '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
# # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# # '_latitude', '_longitude', 'latitude', 'longitude']

# # gets class object of object instance
# print(oslo.__class__)
# print(type(oslo))
# print(dir(oslo.__class__))
# print(oslo.__class__.__name__)
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# # '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
# # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# # 'latitude', 'longitude']

# # creates new type class from Position
# # this class has __name__
# print(type(Position))
# print(type(Position.__name__))
# print(dir(type(Position)))
# print(Position.__name__)


# mauna_kea = EarthPosition(19.82, -155.47)
# print(mauna_kea)
# print(repr(mauna_kea))
# print(mauna_kea)


# olympus_mons = MarsPosition(18.65, -133.80)
# print(olympus_mons)
# print(repr(olympus_mons))

# print(type(str))
# print(str)
# print(dir(type(str)))
# print(dir(str))

# ------------------------------
# str()
# ------------------------------
# olympus_mons = MarsPosition(18.65, -133.80)
# print(str(olympus_mons))

# ------------------------------
# format()
# __format__ is per defult called by f"" strings and .format() methods
# ------------------------------
# olympus_mons = MarsPosition(18.65, -133.80)
# print("{}".format(olympus_mons))
# print(f"{olympus_mons}")

# print(format(olympus_mons))
# print(format(olympus_mons,".1"))
# print(format(olympus_mons,".5"))

# invokation of __repr__ or __str__ can be forced from f"" string using !r or !s
# print(f"{olympus_mons!r}") # invokes __repr__
# print(f"{olympus_mons!s}") # invokes __str__
# print(f"{olympus_mons:.1}") # invokes __fomat__

# = displays variable name followed by __repr__ representation
# print(f"{olympus_mons=}")


# -----------------------------------------------------------------------------------
# multiple inheritance and method resolution order
# -----------------------------------------------------------------------------------

# from base import Base, Sub

# b = Base()
# b.f()

# s = Sub()
# s.f()

# print(dir(s))

# from simple_list import *

# sl = SortedList([3, 8, 1, 2, 9])
# print(sl)
# sl.add(-5)
# print(sl)

# il = IntList([1, 2, 3, 4])
# print(il)
# il.add(5)
# print(il)
# il.add('xxx')

# sil = SortedIntList([3, 8, 1, 2, 9])
# print(sil)
# print(dir(sil))

# list all base classs in the order of as defined
# print(SortedIntList.__bases__)

# list method resolution order mro
# print(SortedIntList.__mro__)

# super() can be called explicitelly
# super(class_object, instance_or_class)

# sil = SortedIntList()
# mro = (<class 'simple_list.SortedIntList'>, <class 'simple_list.IntList'>, <class 'simple_list.SortedList'>, <class 'simple_list.SimpleList'>, <class 'object'>)
# for our SortedIntList instance sil invokes add method from SortedList class
# we skip the add method from IntList class -> int validation is skipped
# super(IntList, sil).add("not a int")

# print(sil)


# -----------------------------------------------------------------------------------
# class decorators
# -----------------------------------------------------------------------------------

# from position import *
# import inspect

# hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
# stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
# cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
# rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
# maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# print(f"{hong_kong!r}")
# print(vars(hong_kong))

# sig = inspect.signature(Location.__init__)
# print(list(sig.parameters))

# print(isinstance(Location.name, property))

# auto_repr(Location)

# print(f"{getattr(hong_kong,'name')!r}")

# trip = Itinerary.from_locations(hong_kong, stockholm, cape_town)
# print(trip)
# trip.add(rotterdam)
# trip.add(rotterdam)
# print(trip)
# trip.remove("Rotterdam")
#trip.truncate_at("Hong Kong")
# print(trip)
# trip.add(hong_kong)

# trip = Itinerary.from_locations(hong_kong)
# print(trip)

# print(trip.__str__())


# -----------------------------------------------------------------------------------
# data classes
# -----------------------------------------------------------------------------------
# from position import *

# hong_kong = Location("Hong Kong", Position(22.29, 114.16))
# stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
# cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
# rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
# maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# print(hong_kong)
