########################################
# buld in numeric types
########################################

# # integer
# print(type(1))

# # float
# print(type(1.2))

# # complex numbers
# print(type((2-1j)))


########################################
# standart library, not build in
# decimal
########################################

# from decimal import Decimal
# import decimal
# import math

# print(Decimal('0.1')*10)

# print(Decimal('0.1') == Decimal(0.1))

# print(decimal.getcontext())

# print(Decimal("0.1") == Decimal(0.1))
# print(math.isclose(Decimal("0.1"), Decimal(0.1)))

########################################
# standart library, not build in
# fraction
########################################

# from decimal import Decimal
# from fractions import Fraction

# print(Fraction(2,5))
# print(Fraction(1,3))
# print(type(Fraction(1,3)+0.5))

# print(dir(Fraction))

# print(Fraction.from_decimal(Decimal('0.1')))
# print(Fraction.from_float(0.1))
# print(Fraction.from_float(0.1).limit_denominator(10))

########################################
# operations with numbers
########################################

# Python rounds to nearest integer
# in case of 0.5, it rounds to nearest even integer
print(round(0.4))
print(round(1.4))
print(round(2.4))

