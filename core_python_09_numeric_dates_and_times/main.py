# ---------------------------------------
# Review of int and float
# ---------------------------------------

# ------------------
# int
# represents whole numbers
# no size limitation


# ------------------
# float
# 64 bit floating pont number -> binary64 format
# 1 bit sign, 11 bits exponent, 52 bits mantissa (fraction)
# in terms of decimal, float has between 15 decimal places precission

# import sys
# print(sys.float_info)
# # sys.float_info(
# # max=1.7976931348623157e+308,
# # max_exp=1024,
# # max_10_exp=308,
# # min=2.2250738585072014e-308,
# # min_exp=-1021,
# # min_10_exp=-307,
# # dig=15,
# # mant_dig=53,
# # epsilon=2.220446049250313e-16,
# # radix=2,
# # rounds=1)

# smallest_negative_float = -sys.float_info.max
# print(smallest_negative_float)
# greatest_negative_float = -sys.float_info.min
# print(greatest_negative_float)

# decimal precission is not given for float
# print(0.8-0.7)
# alternative is decimal

# ---------------------------------------
# The Decimal module
# ---------------------------------------

# ------------------
# decimal.Decimal
# fast, correctly rounded number type for base-10 arithmetic
# floating point type with finite, configurable precision
# usefull in financial applications

# import decimal

# print(decimal.getcontext())
# Context(
# prec=28, # default 28 points of decimal precision
# rounding=ROUND_HALF_EVEN,
# Emin=-999999,
# Emax=999999,
# capitals=1,
# clamp=0,
# flags=[],
# traps=[InvalidOperation, DivisionByZero, Overflow])

# decimal constructor
# decimal.Decimal(5)

# import decimal
# from decimal import Decimal

# print(Decimal(5))
# print(type(Decimal(5)))
# print(type(Decimal(5)).__mro__)

# Decimal accepts strings as arg
# print(Decimal('0.8') - Decimal('0.7'))
# not the same as when we pass float
# print(Decimal(0.8) - Decimal(0.7))
# always pass decimal numbers as str to the Decimal constructor

# we can set to raise error if float is passed
# decimal.getcontext().traps[decimal.FloatOperation] = True
# print(Decimal(0.8) - Decimal(0.7))
# print(Decimal('0.8') > 0.7)

# Decimal preserve trailing zeros precision
# a = Decimal('7.0')
# b = Decimal('7.00')
# c = Decimal('7.000')

# print(a)
# print(b)
# print(c)
# print(a*2)
# print(b*2)
# print(c*2)

# preserves precision on constructed objects
# but limits presision while computing, based on setting
# decimal.getcontext().prec = 6
# d = Decimal('1.234567')
# print(d)
# print(d + Decimal('1'))

# print(Decimal('Infinity'))
# print(Decimal('-Infinity'))
# print(Decimal('NaN'))
# print(Decimal('NaN') - Decimal('1'))

# ------------------
# combining Decimal with other types

# Decimal and float not supported
# print(Decimal('1.4') + 1.4)

# Decimal cannot be used with the functions from math module
# Decimal provides some alternatives
# print(Decimal(9).sqrt())

# ---------------------------------------
# The Fraction module
# ---------------------------------------

# ------------------
# fraction.Fraction
# used to represent rational numbers, like 1/2, 2/3, ... = numerator / denominator
# denominator must not be 0

# from fractions import Fraction
# from decimal import Decimal

# two_thirds = Fraction(2, 3)
# print(two_thirds)
# four_fifths = Fraction(4, 5)
# print(four_fifths)
# print(Fraction(4, 0)) # ZeroDivisionError

# # construct Fraction from float
# print(Fraction(0.5))
# print(Fraction(0.1))
# # construct Fraction from Decimal
# print(Fraction(Decimal('0.1')))
# # construct Fraction from str
# print(Fraction('22/7'))

# Fraction arithmetics
# print(Fraction(2, 3) + Fraction(4, 5))
# print(Fraction(2, 3) - Fraction(4, 5))
# print(Fraction(2, 3) * Fraction(4, 5))
# print(Fraction(2, 3) / Fraction(4, 5))
# print(Fraction(2, 3) // Fraction(4, 5)) # floor
# print(Fraction(2, 3) % Fraction(4, 5)) # modulo


# ---------------------------------------
# Complex numbers
# ---------------------------------------

# Complex - built-in type for working with numbers with an imaginary component
# a = 3 + 5j
# print(a)
# print(type(a))
# print(a.real)
# print(a.imag)

# complex numbers spported by cmath library
# import cmath
# print(cmath.sqrt(-1))


# ---------------------------------------
# Built-in functions related to numbers
# ---------------------------------------

# from fractions import Fraction
# from decimal import Decimal

# ------------------
# abs() - Return the absolute value of the argument

# print(repr(abs(-5)))
# print(repr(abs(-5.0)))
# print(repr(abs(Decimal('-5'))))
# print(repr(abs(Fraction(-5, 1))))


# ------------------
# round() - Round a number to a given precision in decimal digits.

# print(round(1.1234, 3))
# print(round(1.5678, 3))
# # round toward even numbers
# print(round(1.5))
# print(round(2.5))

# print(round(5))
# print(round(5.0))
# print(round(Decimal('5.6')))
# print(round(Fraction(5, 2)))

# ------------------
# base conversions

# print(0b101010)
# print(0o52)
# print(0x2a)

# print(bin(42))
# print(oct(42))
# print(hex(42))

# ---------------------------------------
# Dates and Times in datetime module
# ---------------------------------------

# objects -> date, time, datetime, tzinfo, timedelta
# all are immutable

# ------------------
# date

# import datetime
# # construct date by passing year, month, day
# print(datetime.date(2014, 1, 6))
# print(datetime.date(year=2014, month=1, day=6))
# # Date of Today
# print(datetime.date.today())
# # Construct a date from a POSIX timestamp
# print(datetime.date.fromtimestamp(1000000000)) # 1 bilion seconds
# # Construct a date from a proleptic Gregorian ordinal.
# print(datetime.date.fromordinal(700000))
# print(datetime.date.fromordinal(700001))

# d = datetime.date.today()
# # Properties
# print(d.year)
# print(d.month)
# print(d.day)
# # Methods
# print(d.weekday())
# print(d.isoweekday())
# print(d.isoformat())
# # format
# # are platform dependent
# print(d.strftime('%A %d %B %Y'))
# print("Today is {:%A %d %B %Y}".format(d))

# # min, max, delta
# print(datetime.date.min)
# print(datetime.date.max)
# print(datetime.date.resolution)
# print(repr(datetime.date.resolution))

# ------------------
# time

# import datetime

# # constructors
# print(datetime.time(3, 1, 3, 232))
# print(datetime.time(hour=3, minute=1, second=3, microsecond=232))

# # min max
# print(datetime.time.min)
# print(datetime.time.max)

# # Attributes
# t = datetime.time(hour=3, minute=1, second=3, microsecond=232)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# # Methods
# print(t.isoformat())
# print(t.strftime('%Hh%Mm%Ss')) # platform specific
# print("{t.hour}h{t.minute}m{t.second}s".format(t=t)) # preffered


# ------------------
# datetime

# import datetime

# # constructors
# print(datetime.datetime(2023, 11, 11, 12, 24, 36, 123456))
# print(datetime.datetime(year=2023, month=11, day=11, hour=12, minute=24, second=36, microsecond=123456))
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
# print(datetime.datetime.fromordinal(5))
# print(datetime.datetime.fromtimestamp(1000000))
# print(datetime.datetime.utcfromtimestamp(2000000))
# # combine date and time into datetime
# d = datetime.date.today()
# t = datetime.time(hour=8, second=15)
# dt = datetime.datetime.combine(date=d, time=t)
# print(d)
# print(t)
# print(dt)
# dt = datetime.datetime.strptime('Monday 6 November 2023, 12:50:14','%A %d %B %Y, %H:%M:%S')
# print(dt)
# # construct date and time trom datetime
# d = dt.date()
# t = dt.time()
# print(d)
# print(t)


# ------------------
# timedelta
# represents a duration of time

# import datetime

# constructors

# print(datetime.timedelta(milliseconds=1, microseconds=1000))

# # Attributes
# # internally stores only 3 attributes

# td = datetime.timedelta(weeks=7, minutes=10, milliseconds=24)
# print(repr(td))
# # datetime.timedelta(days=49, seconds=600, microseconds=24000)
# print(td.days)
# print(td.seconds)
# print(td.microseconds)
# print(td)

# date and time arthhmetics results in timedelta
# a = datetime.datetime(year=2023, month=11, day=11, hour=12, minute=24, second=36, microsecond=123456)
# b = datetime.datetime(year=2023, month=10, day=11, hour=12, minute=24, second=36, microsecond=123456)
# c = a - b
# print(repr(c))
# print(c)

# print(datetime.datetime.today() + datetime.timedelta(weeks=1) * 3)

# ------------------
# timezones
# Python 3 only has rudimentary support for timezones
# for more rich timezones support, use third party modules like pytz or dateutil

# timezones are represented by abstract class tzinfo, which cannot be instanciated directly
# we have timezone concrete class, which can be used to represent timezones as fixed offset from UTC

# import datetime

# # In CH, we are in CET, which is UTC + 1
# cet = datetime.timezone(datetime.timedelta(hours=1), "CET")

# departure = datetime.datetime(year=2023, month=12, day=1, hour=12, tzinfo=cet)
# arrival = datetime.datetime(year=2023, month=12, day=1, hour=13, tzinfo=datetime.timezone.utc)

# time_lost = arrival - departure
# print(time_lost)


