# version 1

# By convention, class names use CamelCase
# class Flight:
# 	pass



# version 2 - adding instance methods

# class Flight:
# 	# instance methods are fuctions defined within class
# 	# instance methods must accept the actual instance on which method was called as first parameter
# 	def number(self):
# 		return "SN060"



# version 3 - adding class initializer

# class Flight:

# 	# name of initializer method is __init__
# 	# this method is called when we create new object
# 	# __init__ is not class constructor as in Java, C# or C++
# 	# __init__ is used to configure an object that already exists when it is called
# 	def __init__(self, number):
# 		# _number as object attribute does not need to be declared
# 		# it will be created as we start using it
# 		# one underscore is used
# 		# : to avoid name clash with method number
# 		# : by convention to indicate implementation details not intended for consumption or manipulation
# 		self._number = number

# 	def number(self):
# 		return self._number


# version 4 - adding checks ito class initializer

# class Flight:

# 	def __init__(self, number):

# 		if not number[:2].isalpha():
# 			raise ValueError(f"No airline code in '{number}'")

# 		if not number[:2].isupper():
# 			raise ValueError(f"Invalid airline code in '{number}'")

# 		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
# 			raise ValueError(f"Invalid route number '{number}'")

# 		self._number = number

# 	def number(self):
# 		return self._number
	
# 	# once we have chacks on flight number, we can get airline code
# 	def airline(self):
# 		return self._number[:2]


# # version 5
# # adding Aircraft class
# # adding Aircraft class to init of Flight class
# # adding docstring

# class Aircraft():

# 	def __init__(self, registration, model, num_rows, num_seats_per_row):
# 		self._registration = registration
# 		self._model = model
# 		self._num_rows = num_rows
# 		self._num_seats_per_row = num_seats_per_row

# 	def registration(self):
# 		return self._registration

# 	def model(self):
# 		return self._model

# 	# return tuple of 2 objects: 1. range object, 2. string object
# 	def seating_plan(self):
# 		return (range(1, self._num_rows + 1),"ABCDEFGHJK"[:self._num_seats_per_row])


# class Flight:
# 	"""A flight with particular passenger aircraft"""

# 	def __init__(self, number, aircraft):

# 		if not number[:2].isalpha():
# 			raise ValueError(f"No airline code in '{number}'")

# 		if not number[:2].isupper():
# 			raise ValueError(f"Invalid airline code in '{number}'")

# 		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
# 			raise ValueError(f"Invalid route number '{number}'")

# 		self._number = number
# 		self._aircraft = aircraft

# 	# following Law of Demeter
# 	def aircraft_model(self):
# 		return self._aircraft.model()

# 	def number(self):
# 		return self._number
	
# 	# once we have chacks on flight number, we can get airline code
# 	def airline(self):
# 		return self._number[:2]


# version 6 - adding booking seats
# __init__ - add _seating
# add alocate_seat and _parse_seat
# add relocate_passenger
# add make_flight function
# add console_card_printer function
# add _passenger_seats generator and make_boarding_cards method

# def console_card_printer(passenger, seat, flight_number, aircraft):
# 	# \ -> line continuation character, allowing us to split long line into multiple lies
# 	# implicit string concatenation to adjacent strings to produce string without line breaks
# 	output = f"| Name: {passenger}"            \
# 	         f"  Flight: {flight_number}"      \
# 	         f"  Seat: {seat}"                 \
# 	         f"  Aircraft: {aircraft}"         \
# 	         " |"
# 	banner = "+" + "-" * (len(output) - 2)  + "+"
# 	border = "|" + " " * (len(output) - 2)  + "|"
# 	# add strings into list
# 	lines = [banner, border, output, border, banner]
# 	# concaenate list elements using join() method using new line character
# 	card = "\n".join(lines)
# 	# print boardingcard
# 	print(card)
# 	# print empty line
# 	print()

# class Aircraft():

# 	def __init__(self, registration, model, num_rows, num_seats_per_row):
# 		self._registration = registration
# 		self._model = model
# 		self._num_rows = num_rows
# 		self._num_seats_per_row = num_seats_per_row

# 	def registration(self):
# 		return self._registration

# 	def model(self):
# 		return self._model

# 	# return tuple of 2 objects: 1. range object, 2. string object
# 	def seating_plan(self):
# 		return (range(1, self._num_rows + 1),"ABCDEFGHJK"[:self._num_seats_per_row])


# class Flight:
# 	"""A flight with particular passenger aircraft"""

# 	def __init__(self, number, aircraft):

# 		if not number[:2].isalpha():
# 			raise ValueError(f"No airline code in '{number}'")

# 		if not number[:2].isupper():
# 			raise ValueError(f"Invalid airline code in '{number}'")

# 		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
# 			raise ValueError(f"Invalid route number '{number}'")

# 		self._number = number
# 		self._aircraft = aircraft
# 		# initialize seating plann based on aircraft capacity
# 		rows, seats = self._aircraft.seating_plan()
# 		# Python list is Zero based, but Seating Rows are 1 based
# 		# so we assign 0 element to None, 1st element is row 1, 2nd is row 2, etc
# 		# _seating
# 		# is list of dictionaries
# 		# each element in list represents is 1 dictionary
# 		# each dictionary has keay for each seat letter and value with passanger name
# 		self._seating = [None] + [{ letter : None for letter in seats} for _ in rows]

# 	# following Law of Demeter
# 	def aircraft_model(self):
# 		return self._aircraft.model()

# 	def number(self):
# 		return self._number
	
# 	# once we have chacks on flight number, we can get airline code
# 	def airline(self):
# 		return self._number[:2]

# 	def _parse_seat(self, seat):

# 		rows, seat_letters = self._aircraft.seating_plan()

# 		letter = seat[-1]
# 		if letter not in seat_letters:
# 			raise ValueError(f"Invalid seat letter {letter}")

# 		row_text = seat[:-1]
# 		try:
# 			row = int(row_text)
# 		except:
# 			raise ValueError(f"Invalid seat row {row_text}")

# 		if row not in rows:
# 			raise ValueError(f"Invalid row number {row}")

# 		return row, letter

# 	def alocate_seat(self, seat, passenger):
# 		"""Allocate a seat to passenger

# 		Args:
# 			seat: A seat designator such as 12C or 21F
# 			passenger: passenger name

# 		Raises:
# 			ValueError: If the seat is unavailable.
# 		"""

# 		row, letter = self._parse_seat(seat)

# 		if self._seating[row][letter] is not None:
# 			raise ValueError(f"Seat {seat} already occupied")

# 		self._seating[row][letter] = passenger

# 	def relocate_passenger(self, from_seat, to_seat):
# 		"""Rellocate passenger to different seat

# 		Args:
# 			from_seat: The existing seat designator for the passenger to be moved
# 			to_seat: The new seat designator
# 		"""
# 		from_row, from_letter = self._parse_seat(from_seat)

# 		if self._seating[from_row][from_letter] is None:
# 			raise ValueError(f"No passenger to realocatein seat {from_seat}")

# 		to_row, to_letter = self._parse_seat(to_seat)

# 		if self._seating[to_row][to_letter] is not None:
# 			raise ValueError(f"Seat {to_seat} is occupied")

# 		self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
# 		self._seating[from_row][from_letter] = None

# 	def num_avaiable_seats(self):
# 		# 2 nested generator expressions
# 		return sum(sum(1 for s in row.values() if s is None)
# 			       for row in self._seating
# 			       if row is not None)

# 	# generator function
# 	# search all seats for ocupants
# 	# yield (pasanger, seat) as tuple
# 	def _passenger_seats(self):
# 		"""An iterable series of passenger seating locations."""
# 		row_numbers, seat_letters = self._aircraft.seating_plan()
# 		for row in row_numbers:
# 			for letter in seat_letters:
# 				passenger = self._seating[row][letter]
# 				if passenger is not None:
# 					yield (passenger, f"{row}{letter}")

# 	# this function accepts card printer function as argument
# 	# we can use any card printer variants here, like for HTML output, etc.
# 	# for loop iterates throught sorted list of tuples, uses tuples unpacking
# 	# sorted return sorted list from _passenger_seats() iterable (generator function)
# 	def make_boarding_cards(self, card_printer):
# 		for passenger, seat in sorted(self._passenger_seats()):
# 			card_printer(passenger, seat, self._number, self._aircraft.model())


# def make_flight():
# 	f = Flight('BA758', Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
# 	f.alocate_seat('12A', 'P1')
# 	f.alocate_seat('15F', 'P2')
# 	f.alocate_seat('15E', 'P3')
# 	f.alocate_seat('1C' , 'P4')
# 	f.alocate_seat('1D' , 'P5')
# 	return f


# # version 7 - adding booking seats
# # adding class for AirbusA319 and Boeing777
# # modify make_flight into make_flights

# def console_card_printer(passenger, seat, flight_number, aircraft):
# 	# \ -> line continuation character, allowing us to split long line into multiple lies
# 	# implicit string concatenation to adjacent strings to produce string without line breaks
# 	output = f"| Name: {passenger}"            \
# 	         f"  Flight: {flight_number}"      \
# 	         f"  Seat: {seat}"                 \
# 	         f"  Aircraft: {aircraft}"         \
# 	         " |"
# 	banner = "+" + "-" * (len(output) - 2)  + "+"
# 	border = "|" + " " * (len(output) - 2)  + "|"
# 	# add strings into list
# 	lines = [banner, border, output, border, banner]
# 	# concaenate list elements using join() method using new line character
# 	card = "\n".join(lines)
# 	# print boardingcard
# 	print(card)
# 	# print empty line
# 	print()

# class AirbusA319():

# 	def __init__(self, registration):
# 		self._registration = registration

# 	def registration(self):
# 		return self._registration

# 	def model(self):
# 		return "Airbus A319"

# 	def seating_plan(self):
# 		return range(1, 23), "ABCDEF"


# class Boeing777():

# 	def __init__(self, registration):
# 		self._registration = registration

# 	def registration(self):
# 		return self._registration

# 	def model(self):
# 		return "Boeing 777"

# 	def seating_plan(self):
# 		return range(1, 56), "ABCDEGHJK"


# class Flight:
# 	"""A flight with particular passenger aircraft"""

# 	def __init__(self, number, aircraft):

# 		if not number[:2].isalpha():
# 			raise ValueError(f"No airline code in '{number}'")

# 		if not number[:2].isupper():
# 			raise ValueError(f"Invalid airline code in '{number}'")

# 		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
# 			raise ValueError(f"Invalid route number '{number}'")

# 		self._number = number
# 		self._aircraft = aircraft
# 		# initialize seating plann based on aircraft capacity
# 		rows, seats = self._aircraft.seating_plan()
# 		# Python list is Zero based, but Seating Rows are 1 based
# 		# so we assign 0 element to None, 1st element is row 1, 2nd is row 2, etc
# 		# _seating
# 		# is list of dictionaries
# 		# each element in list represents is 1 dictionary
# 		# each dictionary has keay for each seat letter and value with passanger name
# 		self._seating = [None] + [{ letter : None for letter in seats} for _ in rows]

# 	# following Law of Demeter
# 	def aircraft_model(self):
# 		return self._aircraft.model()

# 	def number(self):
# 		return self._number
	
# 	# once we have chacks on flight number, we can get airline code
# 	def airline(self):
# 		return self._number[:2]

# 	def _parse_seat(self, seat):

# 		rows, seat_letters = self._aircraft.seating_plan()

# 		letter = seat[-1]
# 		if letter not in seat_letters:
# 			raise ValueError(f"Invalid seat letter {letter}")

# 		row_text = seat[:-1]
# 		try:
# 			row = int(row_text)
# 		except:
# 			raise ValueError(f"Invalid seat row {row_text}")

# 		if row not in rows:
# 			raise ValueError(f"Invalid row number {row}")

# 		return row, letter

# 	def alocate_seat(self, seat, passenger):
# 		"""Allocate a seat to passenger

# 		Args:
# 			seat: A seat designator such as 12C or 21F
# 			passenger: passenger name

# 		Raises:
# 			ValueError: If the seat is unavailable.
# 		"""

# 		row, letter = self._parse_seat(seat)

# 		if self._seating[row][letter] is not None:
# 			raise ValueError(f"Seat {seat} already occupied")

# 		self._seating[row][letter] = passenger

# 	def relocate_passenger(self, from_seat, to_seat):
# 		"""Rellocate passenger to different seat

# 		Args:
# 			from_seat: The existing seat designator for the passenger to be moved
# 			to_seat: The new seat designator
# 		"""
# 		from_row, from_letter = self._parse_seat(from_seat)

# 		if self._seating[from_row][from_letter] is None:
# 			raise ValueError(f"No passenger to realocatein seat {from_seat}")

# 		to_row, to_letter = self._parse_seat(to_seat)

# 		if self._seating[to_row][to_letter] is not None:
# 			raise ValueError(f"Seat {to_seat} is occupied")

# 		self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
# 		self._seating[from_row][from_letter] = None

# 	def num_avaiable_seats(self):
# 		# 2 nested generator expressions
# 		return sum(sum(1 for s in row.values() if s is None)
# 			       for row in self._seating
# 			       if row is not None)

# 	# generator function
# 	# search all seats for ocupants
# 	# yield (pasanger, seat) as tuple
# 	def _passenger_seats(self):
# 		"""An iterable series of passenger seating locations."""
# 		row_numbers, seat_letters = self._aircraft.seating_plan()
# 		for row in row_numbers:
# 			for letter in seat_letters:
# 				passenger = self._seating[row][letter]
# 				if passenger is not None:
# 					yield (passenger, f"{row}{letter}")

# 	# this function accepts card printer function as argument
# 	# we can use any card printer variants here, like for HTML output, etc.
# 	# for loop iterates throught sorted list of tuples, uses tuples unpacking
# 	# sorted return sorted list from _passenger_seats() iterable (generator function)
# 	def make_boarding_cards(self, card_printer):
# 		for passenger, seat in sorted(self._passenger_seats()):
# 			card_printer(passenger, seat, self._number, self._aircraft.model())


# def make_flights():
# 	f = Flight('BA758', AirbusA319('G-EUPT'))
# 	f.alocate_seat('12A', 'P1')
# 	f.alocate_seat('15F', 'P2')
# 	f.alocate_seat('15E', 'P3')
# 	f.alocate_seat('1C' , 'P4')
# 	f.alocate_seat('1D' , 'P5')

# 	g = Flight('AF72', Boeing777('F-GSPS'))
# 	g.alocate_seat('55K', 'P1')
# 	g.alocate_seat('33G', 'P2')
# 	g.alocate_seat('4B' , 'P4')
# 	g.alocate_seat('4A' , 'P5')

# 	return f, g


# version 8 - adding inheritance
# add method num_seats() to AirbusA319 and Boeing777
# num_seats() is redundant code, will get worse more Arcraft types we add
# we extract common elements from AirbusA319 and Boeing777 into new base class Aircraft
# from which AirbusA319 and Boeing777 will be derived by inheritance

def console_card_printer(passenger, seat, flight_number, aircraft):
	# \ -> line continuation character, allowing us to split long line into multiple lies
	# implicit string concatenation to adjacent strings to produce string without line breaks
	output = f"| Name: {passenger}"            \
	         f"  Flight: {flight_number}"      \
	         f"  Seat: {seat}"                 \
	         f"  Aircraft: {aircraft}"         \
	         " |"
	banner = "+" + "-" * (len(output) - 2)  + "+"
	border = "|" + " " * (len(output) - 2)  + "|"
	# add strings into list
	lines = [banner, border, output, border, banner]
	# concaenate list elements using join() method using new line character
	card = "\n".join(lines)
	# print boardingcard
	print(card)
	# print empty line
	print()

# Aircraft class is not usable on its own, because it depends on method 
# seating_plan(), which does not exist in Aircraft class
# this class is abstract, is not usefull to meka instances using it
class Aircraft():

	def __init__(self, registration):
		self._registration = registration

	def registration(self):
		return self._registration

	def num_seats(self):
		rows, row_seats = self.seating_plan()
		return len(rows) * len(row_seats)

# Inheritance is specified in the class definition
# where base classes are listed inside ()
class AirbusA319(Aircraft):

	# def __init__(self, registration):
	# 	self._registration = registration

	# def registration(self):
	# 	return self._registration

	def model(self):
		return "Airbus A319"

	def seating_plan(self):
		return range(1, 23), "ABCDEF"

	# def num_seats(self):
	# 	rows, row_seats = self.seating_plan()
	# 	return len(rows) * len(row_seats)


class Boeing777(Aircraft):

	# def __init__(self, registration):
	# 	self._registration = registration

	# def registration(self):
	# 	return self._registration

	def model(self):
		return "Boeing 777"

	def seating_plan(self):
		return range(1, 56), "ABCDEGHJK"

	# def num_seats(self):
	# 	rows, row_seats = self.seating_plan()
	# 	return len(rows) * len(row_seats)


class Flight:
	"""A flight with particular passenger aircraft"""

	def __init__(self, number, aircraft):

		if not number[:2].isalpha():
			raise ValueError(f"No airline code in '{number}'")

		if not number[:2].isupper():
			raise ValueError(f"Invalid airline code in '{number}'")

		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
			raise ValueError(f"Invalid route number '{number}'")

		self._number = number
		self._aircraft = aircraft
		# initialize seating plann based on aircraft capacity
		rows, seats = self._aircraft.seating_plan()
		# Python list is Zero based, but Seating Rows are 1 based
		# so we assign 0 element to None, 1st element is row 1, 2nd is row 2, etc
		# _seating
		# is list of dictionaries
		# each element in list represents is 1 dictionary
		# each dictionary has keay for each seat letter and value with passanger name
		self._seating = [None] + [{ letter : None for letter in seats} for _ in rows]

	# following Law of Demeter
	def aircraft_model(self):
		return self._aircraft.model()

	def number(self):
		return self._number
	
	# once we have chacks on flight number, we can get airline code
	def airline(self):
		return self._number[:2]

	def _parse_seat(self, seat):

		rows, seat_letters = self._aircraft.seating_plan()

		letter = seat[-1]
		if letter not in seat_letters:
			raise ValueError(f"Invalid seat letter {letter}")

		row_text = seat[:-1]
		try:
			row = int(row_text)
		except:
			raise ValueError(f"Invalid seat row {row_text}")

		if row not in rows:
			raise ValueError(f"Invalid row number {row}")

		return row, letter

	def alocate_seat(self, seat, passenger):
		"""Allocate a seat to passenger

		Args:
			seat: A seat designator such as 12C or 21F
			passenger: passenger name

		Raises:
			ValueError: If the seat is unavailable.
		"""

		row, letter = self._parse_seat(seat)

		if self._seating[row][letter] is not None:
			raise ValueError(f"Seat {seat} already occupied")

		self._seating[row][letter] = passenger

	def relocate_passenger(self, from_seat, to_seat):
		"""Rellocate passenger to different seat

		Args:
			from_seat: The existing seat designator for the passenger to be moved
			to_seat: The new seat designator
		"""
		from_row, from_letter = self._parse_seat(from_seat)

		if self._seating[from_row][from_letter] is None:
			raise ValueError(f"No passenger to realocatein seat {from_seat}")

		to_row, to_letter = self._parse_seat(to_seat)

		if self._seating[to_row][to_letter] is not None:
			raise ValueError(f"Seat {to_seat} is occupied")

		self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
		self._seating[from_row][from_letter] = None

	def num_avaiable_seats(self):
		# 2 nested generator expressions
		return sum(sum(1 for s in row.values() if s is None)
			       for row in self._seating
			       if row is not None)

	# generator function
	# search all seats for ocupants
	# yield (pasanger, seat) as tuple
	def _passenger_seats(self):
		"""An iterable series of passenger seating locations."""
		row_numbers, seat_letters = self._aircraft.seating_plan()
		for row in row_numbers:
			for letter in seat_letters:
				passenger = self._seating[row][letter]
				if passenger is not None:
					yield (passenger, f"{row}{letter}")

	# this function accepts card printer function as argument
	# we can use any card printer variants here, like for HTML output, etc.
	# for loop iterates throught sorted list of tuples, uses tuples unpacking
	# sorted return sorted list from _passenger_seats() iterable (generator function)
	def make_boarding_cards(self, card_printer):
		for passenger, seat in sorted(self._passenger_seats()):
			card_printer(passenger, seat, self._number, self._aircraft.model())


def make_flights():
	f = Flight('BA758', AirbusA319('G-EUPT'))
	f.alocate_seat('12A', 'P1')
	f.alocate_seat('15F', 'P2')
	f.alocate_seat('15E', 'P3')
	f.alocate_seat('1C' , 'P4')
	f.alocate_seat('1D' , 'P5')

	g = Flight('AF72', Boeing777('F-GSPS'))
	g.alocate_seat('55K', 'P1')
	g.alocate_seat('33G', 'P2')
	g.alocate_seat('4B' , 'P4')
	g.alocate_seat('4A' , 'P5')

	return f, g



# """Model for aircraft flights."""

# def console_card_printer(passenger, seat, flight_number, aircraft):
# 	output = f"| Name: {passenger}"            \
# 	         f"  Flight: {flight_number}"      \
# 	         f"  Seat: {seat}"                 \
# 	         f"  Aircraft: {aircraft}"         \
# 	         " |"
# 	banner = "+" + "-" * (len(output) - 2)  + "+"
# 	border = "|" + " " * (len(output) - 2)  + "|"
# 	lines = [banner, border, output, border, banner]
# 	card = "\n".join(lines)
# 	print(card)
# 	print()


# class Aircraft():

# 	def __init__(self, registration):
# 		self._registration = registration

# 	def registration(self):
# 		return self._registration

# 	def num_seats(self):
# 		rows, row_seats = self.seating_plan()
# 		return len(rows) * len(row_seats)


# class AirbusA319(Aircraft):

# 	def model(self):
# 		return "Airbus A319"

# 	def seating_plan(self):
# 		return range(1, 23), "ABCDEF"


# class Boeing777(Aircraft):

# 	def model(self):
# 		return "Boeing 777"

# 	def seating_plan(self):
# 		return range(1, 56), "ABCDEGHJK"


# class Flight:
# 	"""A flight with particular passenger aircraft"""

# 	def __init__(self, number, aircraft):

# 		if not number[:2].isalpha():
# 			raise ValueError(f"No airline code in '{number}'")

# 		if not number[:2].isupper():
# 			raise ValueError(f"Invalid airline code in '{number}'")

# 		if not (number[2:].isdigit() and int(number[2:]) <= 9999): 
# 			raise ValueError(f"Invalid route number '{number}'")

# 		self._number = number
# 		self._aircraft = aircraft
# 		rows, seats = self._aircraft.seating_plan()
# 		self._seating = [None] + [{ letter : None for letter in seats} for _ in rows]

# 	def number(self):
# 		return self._number

# 	def airline(self):
# 		return self._number[:2]

# 	def aircraft_model(self):
# 		return self._aircraft.model()

# 	def _parse_seat(self, seat):

# 		rows, seat_letters = self._aircraft.seating_plan()

# 		letter = seat[-1]
# 		if letter not in seat_letters:
# 			raise ValueError(f"Invalid seat letter {letter}")

# 		row_text = seat[:-1]
# 		try:
# 			row = int(row_text)
# 		except:
# 			raise ValueError(f"Invalid seat row {row_text}")

# 		if row not in rows:
# 			raise ValueError(f"Invalid row number {row}")

# 		return row, letter


# 	def alocate_seat(self, seat, passenger):
# 		"""Allocate a seat to passenger

# 		Args:
# 			seat: A seat designator such as 12C
# 			passenger: passenger name

# 		Raises:
# 			ValueError: If the seat is unavailable.
# 		"""

# 		row, letter = self._parse_seat(seat)

# 		if self._seating[row][letter] is not None:
# 			raise ValueError(f"Seat {seat} already occupied")

# 		self._seating[row][letter] = passenger

# 	def relocate_passenger(self, from_seat, to_seat):
# 		"""Rellocate passenger to different seat

# 		Args:
# 			from_seat: The existing seat designator for the passenger to be moved
# 			to_seat: The new seat designator
# 		"""
# 		from_row, from_letter = self._parse_seat(from_seat)

# 		if self._seating[from_row][from_letter] is None:
# 			raise ValueError(f"No passenger to realocatein seat {from_seat}")

# 		to_row, to_letter = self._parse_seat(to_seat)

# 		if self._seating[to_row][to_letter] is not None:
# 			raise ValueError(f"Seat {to_seat} is occupied")

# 		self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
# 		self._seating[from_row][from_letter] = None

# 	def num_avaiable_seats(self):
# 		return sum(sum(1 for s in row.values() if s is None)
# 			       for row in self._seating
# 			       if row is not None)

# 	def make_boarding_cards(self, card_printer):
# 		for passenger, seat in sorted(self._passenger_seats()):
# 			card_printer(passenger, seat, self._number, self._aircraft.model())

# 	def _passenger_seats(self):
# 		"""An iterable series of passenger seating locations."""
# 		row_numbers, seat_letters = self._aircraft.seating_plan()
# 		for row in row_numbers:
# 			for letter in seat_letters:
# 				passenger = self._seating[row][letter]
# 				if passenger is not None:
# 					yield (passenger, f"{row}{letter}")


# def make_flights():
# 	f = Flight('BA758', AirbusA319('G-EUPT'))
# 	f.alocate_seat('12A', 'P1')
# 	f.alocate_seat('15F', 'P2')
# 	f.alocate_seat('15E', 'P3')
# 	f.alocate_seat('1C' , 'P4')
# 	f.alocate_seat('1D' , 'P5')

# 	g = Flight('AF72', Boeing777('F-GSPS'))
# 	g.alocate_seat('55K', 'P1')
# 	g.alocate_seat('33G', 'P2')
# 	g.alocate_seat('4B' , 'P4')
# 	g.alocate_seat('4A' , 'P5')

# 	return f, g
