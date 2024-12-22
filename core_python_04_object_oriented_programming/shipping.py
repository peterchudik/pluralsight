import iso6346

class ShippingContainer:

	# Define class attributes inside class block
	# same for all class instances
	# class block has no scope

	my_class_attribute = 'class attribute go here'
	MY_CONSTANT = 'they are often class specific constants'

	HEIGHT_FT = 8.5
	WIDTH_FT = 8.0
	next_serial = 1337

	# static method operates on class attributes, not on instance attributes
	# self parameter is not required

	# @staticmethod
	# def _generate_serial():
	# 	# when refferencing to class attributes, must qualify with class name
	# 	# class body is has no scope only exists at global/module scope
	# 	result = ShippingContainer.next_serial
	# 	ShippingContainer.next_serial += 1
	# 	return result

	@staticmethod
	def _make_bic_code(owner_code, serial):
		return iso6346.create(
			owner_code = owner_code,
			serial = str(serial).zfill(6)
			)

	# class method requires access to the class object (not instance)
	# class object is passed as first atribute

	@classmethod
	def _generate_serial(cls):
		# when refferencing to class attributes, must qualify with class name
		# class body has no scope only exists at global/module scope
		result = cls.next_serial
		cls.next_serial += 1
		return result

	# class method can also provide factory initializer for the class instance
	@classmethod
	def create_empty(cls, owner_code, length_ft, **kwargs):
		return cls(owner_code, length_ft, contents = [], **kwargs)

	# class method can also provide factory initializer for the class instance
	@classmethod
	def create_with_items(cls, owner_code, length_ft, items, **kwargs):
		return cls(owner_code, length_ft, contents = list(items), **kwargs)

	def __init__(self, owner_code, length_ft, contents, **kwargs):
		self.owner_code = owner_code
		self.length_ft = length_ft
		self.contents = contents
		# self.bic = ShippingContainer._make_bic_code(
		# call _make_bic_code using object instance self. to allow override in the classes that inherits this class
		# like below class RefrigeratedShippingContainer
		self.bic = self._make_bic_code(
			owner_code = owner_code,
			serial = ShippingContainer._generate_serial()
			)

	# we do not want to override properties getter and setter
	# instead we create new method called by setter or getter
	# and override this instead in child classes
	@property
	def volume_ft3(self):
		return self._calc_volume()

	def _calc_volume(self):
		return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
	

class RefrigeratedShippingContainer(ShippingContainer):

	MAX_CELSIUS = 4.0
	FRIDGE_VOLUME = 100

	# we provide an override version of _make_bic_code
	# the problem is, that the __init__method is calling _make_bic_code using class object, not instance
	# so it will not call _make_bic_code from here, but from parent class always
	# solution is to call _make_bic_code using object instance = self.
	@staticmethod
	def _make_bic_code(owner_code, serial):
		return iso6346.create(
			owner_code = owner_code,
			serial = str(serial).zfill(6),
			category = 'R'
			)
	# to prevent changing celsius higher than MAX_CELSIUS
	# we create class properties which behave like attributes
	# instead of creating getter and setter methods

	# getter - can be also used to create read only attributes
	@property
	def celsius(self):
		return self._celsius

	# setter
	@celsius.setter
	def celsius(self, value):
		# we delegate the logic to another class method
		# as it is easier to overide the class method in the child classes
		# instead of overiding property itself in child classes
		self._set_celsius(value)

	def _set_celsius(self, value):
		if value > RefrigeratedShippingContainer.MAX_CELSIUS:
			raise ValueError('Temperature too hot!')
		self._celsius = value

	@staticmethod
	def _c_to_f(celsius):
		return celsius * 9/5 + 32

	@staticmethod
	def _f_to_c(fahrenheit):
		return (fahrenheit - 32) * 5/9

	@property
	def fahrenheit(self):
		return RefrigeratedShippingContainer._c_to_f(self.celsius)

	@fahrenheit.setter
	def fahrenheit(self, value):
		self.celsius = RefrigeratedShippingContainer._f_to_c(value)

	def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
		# __init__ of parent class is not called automatically
		# explicit is better than implicit
		super().__init__(owner_code, length_ft, contents, **kwargs)
		# validation can be removed after moving it to setter
		self.celsius = celsius

	# do not overide property, instead overide the method call by property
	# @property
	# def volume_ft3(self):
	# 	return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME

	def _calc_volume(self):
		return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

	MIN_CELSIUS = -20

	# Override property setter from parent class
	# This works but is quite ugly, as we call parent class directly
	# This can get messy, for example if parent is n levels above

	# @RefrigeratedShippingContainer.celsius.setter
	# def celsius(self, value):
	# 	if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
	# 		raise ValueError('Temperature too cold!')
	# 	# calling directly as super().celsius = value does not work
	# 	RefrigeratedShippingContainer.celsius.fset(self, value)

	# Instead of overriding setter we override the method called by setter in parent class
	def _set_celsius(self, value):
		if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
			raise ValueError('Temperature too cold!')
		super()._set_celsius(value)

