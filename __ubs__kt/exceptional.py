# # Version 1 - initial

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	number = ''
# 	for token in s:
# 		number += DIGIT_MAP[token]
# 	x = int(number)
# 	return x


# # Version 2 - catch KeyError

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	try:
# 		number = ''
# 		for token in s:
# 			number += DIGIT_MAP[token]
# 		x = int(number)
# 		print("Conversion OK")
# 	except KeyError:
# 		print("Conversion Error")
# 		x = -1
# 	return x

# Version 3 - catch TypeError

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	try:
# 		number = ''
# 		for token in s:
# 			number += DIGIT_MAP[token]
# 		x = int(number)
# 		print("Conversion OK")
# 	except KeyError:
# 		print("Conversion Error")
# 		x = -1
# 	except TypeError:
# 		print("Conversion Error")
# 		x = -1
# 	return x

# # Version 4 - remove duplicate code and print

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	"""Convert a string to an integer"""
# 	x = -1
# 	try:
# 		number = ''
# 		for token in s:
# 			number += DIGIT_MAP[token]
# 		x = int(number)
# 	except (KeyError, TypeError):
# 		# add pass in order to not have empty block
# 		pass
# 	return x

# # Version 5 - remove x

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	"""Convert a string to an integer"""
# 	try:
# 		number = ''
# 		for token in s:
# 			number += DIGIT_MAP[token]
# 		return int(number)
# 	except (KeyError, TypeError):
# 		return -1

# Version 6 - get a details about error object

DIGIT_MAP = {
	'zero': '0',
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

def convert(s):
	"""Convert a string to an integer"""
	try:
		number = ''
		for token in s:
			number += DIGIT_MAP[token]
		return int(number)
	except (KeyError, TypeError) as e: # get a named reference to exception object
		print(f"Conversion error: {e!r}") # print repr of a object (call __repr__)
		return -1

# Version 7 - adding log an raising exception

from math import log

DIGIT_MAP = {
	'zero': '0',
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

def convert(s):
	"""Convert a string to an integer"""
	try:
		number = ''
		for token in s:
			number += DIGIT_MAP[token]
		return int(number)
	except (KeyError, TypeError) as e: # get a named reference to exception object
		print(f"Conversion error: {e!r}") # print repr of a object (call __repr__)
		# raise exception
		raise


def string_log(s):
	v = convert(s)
	return(log(v))

# import sys

# from math import log

# DIGIT_MAP = {
# 	'zero': '0',
# 	'one': '1',
# 	'two': '2',
# 	'three': '3',
# 	'four': '4',
# 	'five': '5',
# 	'six': '6',
# 	'seven': '7',
# 	'eight': '8',
# 	'nine': '9'
# }

# def convert(s):
# 	"""Convert a string to an integer"""

# 	try:
# 		number = ''
# 		for token in s:
# 			number += DIGIT_MAP[token]
# 		# print(f'Conversion succeeded! x = {x}')
# 		return int(number)

# 	except (KeyError, TypeError) as e:
# 		print(f'Conversion error: {e!r}', file=sys.stderr)
# 		raise

# def string_log(s):

# 	v = convert(s)

# 	return(log(v))
