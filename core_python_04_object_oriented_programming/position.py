import inspect
import functools
from dataclasses import dataclass

def typename(obj):
	return type(obj).__name__

class Position:

	def __init__(self, latitude, longitude):

		if not (-90 <= latitude <= +90):
			raise ValueError(f"Latitude {latitude} out of range")

		if not (-180 <= longitude <= +180):
			raise ValueError(f"Longitude {longitude} out of range")

		self._latitude = latitude
		self._longitude = longitude

	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude
	
	@property
	def latitude_hemisphere(self):
		return "N" if self.latitude >= 0 else "S"

	@property
	def longitude_hemisphere(self):
		return "E" if self.longitude >= 0 else "W"

	# ------------------------------
	# customizing repr()
	# repr() is intended for developers
	# guidlines for __repr__:
	# 1. incude all necessery states of objects
	# 2. format as constructor invocation code
	# ------------------------------
	def __repr__(self):
		# basic
		# return f"Position(latitude={self.latitude}, longitude={self.longitude})"
		
		# fit for inheritance
		# return f"{self.__class__.__name__}(latitude={self.latitude}, longitude={self.longitude})"
		# fit for inheritance using type
		# return f"{type(self).__name__}(latitude={self.latitude}, longitude={self.longitude})"
		# fit for inheritance using help function typename
		return f"{typename(self)}(latitude = {self.latitude}, longitude = {self.longitude})"
	
	def __str__(self):
		# return (
		# 	f"{abs(self.latitude)} Degree {self.latitude_hemisphere}, "
		# 	f"{abs(self.longitude)} Degree {self.longitude_hemisphere}"
		# )

		# __str__ should return the same result as __format__ with empty format spec
		# so we call __format__ inderictly using build in format function without second argument
		# rather then calling __str__ from __format__ and duplicating our code
		return(format(self))

	def __format__(self, format_spec):
		component_format_spec = ".2f"

		prefix, dot, suffix = format_spec.partition(".")
		if dot:
			num_decimal_places = int(suffix)
			component_format_spec = f".{num_decimal_places}f"

		latitude = format(abs(self.latitude),component_format_spec)
		longitude = format(abs(self.longitude),component_format_spec)

		return (
			f"{latitude} Degree {self.latitude_hemisphere}, "
			f"{longitude} Degree {self.longitude_hemisphere}"
		)

class EarthPosition(Position):
	pass		

class MarsPosition(Position):
	pass

def auto_repr(cls):
	
	# print(f"Decorating {cls.__name__} with auto repr")
	
	# get all variables of class as dictionary
	members = vars(cls)
	# for name, member in members.items():
	# 	print(name, member)
	
	# check if __repr__ is defined in class
	if "__repr__" in members:
		raise TypeError(f"{cls.__name__} already defines __repr__")
	
	# check if __init__ is not defned in class
	if "__init__" not in members:
		raise TypeError(f"{cls.__name__} does not override __init__")
	
	# get the parameters of __init__ function, except self
	sig = inspect.signature(cls.__init__)
	parameter_names = list(sig.parameters)[1:]
	# print("__init__ parameter names: ", parameter_names)

	# check, if all parameters of __init__ are also properties (instances of property class)

	# using for loop
	# for parameter_name in parameter_names:
	# 	if not isinstance(members.get(parameter_name, None), property):
	# 		raise TypeError(
	# 			f"Cannot apply auto_repr to {cls.__name__} because not all "
	# 			"__init__ parameters have matching properties")

	# using generator comprehension
	if not all(
		isinstance(members.get(parameter_name, None), property)
		for parameter_name in parameter_names
		):
			raise TypeError(
				f"Cannot apply auto_repr to {cls.__name__} because not all "
				"__init__ parameters have matching properties")

	def synthesized_repr(self):

		return "{typename}({args})".format(
			typename = typename(self),
			args = ", ".join(
				"{name} = {value!r}".format(
					name = name,
					value = getattr(self, name)
				)  for name in parameter_names
			)
		)
	
	setattr(cls, "__repr__", synthesized_repr)

	return cls

# Class Location defined using dataclass decorator
# optional arguments
# def dataclass(
#     *,
#     init: bool = True,
#     repr: bool = True,
#     eq: bool = True,
#     order: bool = False,
#     unsafe_hash: bool = False,
#     frozen: bool = False,
#     match_args: bool = True,
#     kw_only: bool = False,
#     slots: bool = False,
#     weakref_slot: bool = False)

@dataclass
class Location:
	# This is type annotation, which is normally optional, but here is needed
	name: str
	position: Position

# Handwritten class Location
# @auto_repr
# class Location:

# 	def __init__(self, name, position):
# 		self._name = name
# 		self._position = position

# 	@property
# 	def name(self):
# 		return self._name

# 	@property
# 	def position(self):
# 		return self._position

# 	# def __repr__(self):
# 	# 	return f"{typename(self)}(name = {self.name}, position = {self.position!r})"

# 	def __str__(self):
# 		return self.name

def postcondition(predicate):

	def function_decorator(f):
		
		@functools.wraps(f)
		def wrapper(self, *args, **kwargs):
			result = f(self, *args, **kwargs)
			# print("Checking condition")
			if not predicate(self):
				raise RuntimeError(
					f"Post-condition {predicate.__name__} not "
					f"maintained for {self!r}"
				)
			return result
		
		return wrapper

	return function_decorator

def invariant(predicate):
	function_decorator = postcondition(predicate)

	def class_decorator(cls):
		members = list(vars(cls).items())
		for name, member in members:
			if inspect.isfunction(member):
				decorated_member = function_decorator(member)
				setattr(cls, name, decorated_member)
				# print(f"Function {name} decorated")

		return cls

	return class_decorator

def at_least_two_locations(itinerary):
	return len(itinerary._locations) >= 2

def no_duplicates(itinerary):
	already_seen = set()
	for location in itinerary._locations:
		if location in already_seen:
			return False
		already_seen.add(location)
	return True

@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:

	@classmethod
	def from_locations(cls, *locations):
		return cls(locations)
	
	# @postcondition(at_least_two_locations)
	def __init__(self, locations):
		self._locations = list(locations)

	def __str__(self):
		return "\n".join(location.name for location in self._locations)

	@property
	def locations(self):
		return(self._locations)
	
	@property
	def origin(self):
		return self._locations[0]
	
	@property
	def destination(self):
		return self._locations[-1]

	# @postcondition(at_least_two_locations)
	def add(self, location):
		self._locations.append(location)

	# @postcondition(at_least_two_locations)
	def remove(self, name):
		removal_indexes = [
			index for index, location in enumerate(self._locations)
			if location.name == name
		]
		for index in reversed(removal_indexes):
			del self._locations[index]

	# @postcondition(at_least_two_locations)
	def truncate_at(self, name):
		stop = None
		for index, location in enumerate(self._locations):
			if location.name == name:
				stop = index + 1

		self._locations = self._locations[:stop]

