# import words

# print(type(words))

# print(dir(words))

# print(type(words.fetch_words))

# print(dir(words.fetch_words))

# print(words.fetch_words.__name__)

# print(words.fetch_words.__doc__)


# from exceptional import convert

# print(convert('one three three seven'.split()))
# print(convert('around one million'.split()))
# print(convert(512))


# from exceptional import string_log

# print(string_log('ouch'.split()))


# from airtravel import Flight

# f = Flight('060')
# f = Flight('sn060')
# f = Flight('SN06A')
# f = Flight('SN60000')


# f = Flight('SN0600')
# print(f.number())
# print(f.airline())
# print(f._number) # not recommended but good for debuging and testing

# from airtravel import Aircraft

# a = Aircraft(registration = 'XXX', model = 'XXX', num_rows = 20, num_seats_per_row = 6)
# print(a.seating_plan())

# #letters = [i for i in a.seating_plan()[1]]
# letters = list(a.seating_plan()[1])
# print(letters)

# from airtravel import *
# from pprint import pprint as pp

# f = Flight('BA758', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# print(f.aircraft_model())
# pp(f._seating)
# pp(f._seating[1]['A'])
# f.alocate_seat('12A', 'Peter')
# f.alocate_seat('12A', 'Someone')
# f.alocate_seat('10A', 'Someone')
# f.alocate_seat('XAA', 'Someone')
# pp(f._seating)

# from airtravel import make_flight, console_card_printer
# from pprint import pprint as pp

# f = make_flight()
# pp(f._seating)
# f.relocate_passenger('12A','15D')
# pp(f._seating)
# pp(f.num_avaiable_seats())

# f.make_boarding_cards(console_card_printer)

# from airtravel import *
# from pprint import pprint as pp

# f, g = make_flights()

# pp(f.aircraft_model())
# pp(g.aircraft_model())
# pp(f.num_avaiable_seats())
# pp(g.num_avaiable_seats())

# f.make_boarding_cards(console_card_printer)
# g.make_boarding_cards(console_card_printer)

# a = AirbusA319('G-EUPT')
# b = Boeing777('F-GSPS')

# pp(a.num_seats())
# pp(b.num_seats())
