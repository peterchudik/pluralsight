# ------------------------------------------------------------------------
# while - else
# ------------------------------------------------------------------------

# import operator

# def is_comment(item):
#     return isinstance(item, str) and item.startswith("#")

# def execute(program):

#     # Skip leading comments
#     while program:
#         item = program.pop()
#         if not is_comment(item):
#             program.append(item)
#             break
#     else: # nobreak
#         print("Empty program")
#         return
    
#     # Evaluate the program
#     pending = []
#     while program:
#         item = program.pop()
#         if callable(item):
#             try:
#                 result = item(*pending)
#             except Exception as e:
#                 print("Error: ", e)
#             program.append(result)
#             pending.clear()
#         else:
#             pending.append(item)
#     else: # nobreak
#         print("Program succesfull")
#         print("Result: ", pending)

#     print("Finished")

# program = list(reversed((
#     "# A short stak program",
#     "# to add and multiply",
#     5,
#     2,
#     operator.add,
#     3,
#     operator.sub,
# )))

# execute(program)


# ------------------------------------------------------------------------
# for - else
# ------------------------------------------------------------------------

# items = [123, 41, 525, 6436543, 24, 2525, 525, 5252, 45252]
# divisor = 13

# for item in items:
#     if item % divisor == 0:
#         found_item = item
#         break
# else: # nobreak
#     items.append(divisor)
#     found_item = divisor

# print (f"{items} contains {found_item} which is multiple of {divisor}")

# ------------------------------------------------------------------------
# for - else -> to avoid it you can use named function
# ------------------------------------------------------------------------

# def ensure_has_divisible(items, divisor):
#     for item in items:
#         if item % divisor == 0:
#             return item
#     items.append(divisor)
#     return divisor

# items = [123, 41, 525, 6436543, 24, 2525, 525, 5252, 45252]
# divisor = 13

# dividend = ensure_has_divisible(items, divisor)

# print (f"{items} contains {dividend} which is multiple of {divisor}")

# ------------------------------------------------------------------------
# try - else
# ------------------------------------------------------------------------

# try:
#     f = open("little_women.txt", "rt")
# except OSError:
#     print("No file found.")
# else:
#     num_lines = sum(1 for _ in f)
#     print("Number of lines:", num_lines)
#     f.close()

# ------------------------------------------------------------------------
# switch statement - NO switch exists
# ------------------------------------------------------------------------

# Option 1 -> if..elif..elif..else


# Option 2 -> A mapping of callables

# """Kafka - the adventure game you cannot win."""


# def go_north(position):
#     i, j = position
#     new_position = (i, j + 1)
#     return new_position


# def go_east(position):
#     i, j = position
#     new_position = (i + 1, j)
#     return new_position


# def go_south(position):
#     i, j = position
#     new_position = (i, j - 1)
#     return new_position


# def go_west(position):
#     i, j = position
#     new_position = (i - 1, j)
#     return new_position


# def look(position):
#     return position


# def quit_game(position):
#     return None


# def labyrinth(position, alive):
#     print("You are in a maze of twisty passages, all alike.")
#     return position, alive


# def dark_forest_road(position, alive):
#     print("You are on a road in a dark forest. To the north you can see a tower.")
#     return position, alive


# def tall_tower(position, alive):
#     print("There is a tall tower here, with no obvious door. A path leads east.")
#     return position, alive


# def rabbit_hole(position, alive):
#     print("You fall down a rabbit hole into a labyrinth.")
#     return (0, 0), alive


# def lava_pit(position, alive):
#     print("You fall into a lava pit.")
#     return position, False


# def play():

#     position = (0, 0)
#     alive = True

#     while position:

#         locations = {
#             (0, 0): labyrinth,
#             (1, 0): dark_forest_road,
#             (1, 1): tall_tower,
#             (2, 1): rabbit_hole,
#             (1, 2): lava_pit,
#         }

#         try:
#             location_action = locations[position]
#         except KeyError:
#             print("There is nothing here.", position)
#         else:
#             position, alive = location_action(position, alive)

#         if not alive:
#             print("You're dead!")
#             break

#         command = input("? ")

#         actions = {
#             "N": go_north,
#             "E": go_east,
#             "W": go_west,
#             "S": go_south,
#             "L": look,
#             "Q": quit_game,
#         }

#         try:
#             command_action = actions[command]
#         except KeyError:
#             print("I don't understand")
#         else:
#             position = command_action(position)

#     else:  # nobreak
#         print("You have chosen to leave the game.")

#     print("Game over")

# play()

# ------------------------------------------------------------------------
# dispatching on type
# ------------------------------------------------------------------------

# from shapes import Rectangle, Circle, Polygon, Group
# from draw import make_svg_document

# s = Shape(stroke_color = "#2a9fbc", fill_color = "#ffffff", stroke_width = 8)
# print(s.attrs())

# r = Rectangle((0,0), 100, 100, stroke_color = "#2a9fbc", fill_color = "#ffffff", stroke_width = 8)
# print(r.draw())

# c = Circle((600, 90), 30, fill_color = "#ffffff")
# print(c.draw())

# p = Polygon([
#             (300, 425), (580, 425), (560, 155), (510, 155),
#             (500, 285), (450, 250), (450, 285), (400, 250),
#             (400, 285), (350, 250), (350, 285), (300, 250),
#             ],
#             stroke_width=8,
#             stroke_color="#2a9fbc",
#             fill_color="#addbea")
# print(p.draw())

# points = [
#         (300, 425), (580, 425), (560, 155), (510, 155),
#         (500, 285), (450, 250), (450, 285), (400, 250),
#         (400, 285), (350, 250), (350, 285), (300, 250),
# ]
# print(points)
# pt = '<polygon points="{points}"/>'.format(points = " ".join(f"{point[0]} {point[1]}" for point in points))
# print(pt)

# g = Group([
#     Circle(center=(550, 120), radius=30, fill_color="#d8d8d8"),
#     Circle(center=(600, 90), radius=40, fill_color="#d8d8d8"),
#     Circle(center=(650, 60), radius=50, fill_color="#d8d8d8"),
# ])

# print(g.draw())

# d = make_svg_document(300, 10, 700, 425, [r, c, p, g])
# print(d)


# outline = Polygon(points=[
#         (300, 425), (580, 425), (560, 155), (510, 155),
#         (500, 285), (450, 250), (450, 285), (400, 250),
#         (400, 285), (350, 250), (350, 285), (300, 250),
#     ],
#     stroke_width=8,
#     stroke_color="#2a9fbc",
#     fill_color="#addbea",
# )
# left_window = Rectangle(
#     p=(350, 330),
#     width=50, height=40,
#     stroke_width=6,
#     stroke_color="#2a9fbc",
#     fill_color="#ffffff",
# )
# right_window = Rectangle(
#     p=(430, 330),
#     width=50, height=40,
#     stroke_width=6,
#     stroke_color="#2a9fbc",
#     fill_color="#ffffff",
# )
# smoke = Group(
#     [
#         Circle(center=(550, 120), radius=30, fill_color="#d8d8d8"),
#         Circle(center=(600, 90), radius=40, fill_color="#d8d8d8"),
#         Circle(center=(650, 60), radius=50, fill_color="#d8d8d8"),
#     ]
# )
# d = make_svg_document(300, 10, 700, 425, [outline, right_window, left_window, smoke])
# print(d)

# with open("my_svg.svg", "wt", encoding="utf=8") as svg_file:
#     print(d, file=svg_file)

# print("Done")
# print("\n".join(f"{item}: {name}" for item, name in globals().items()))
# print(Group.__name__)

# ------------------------------------------------------------------------
# Short circuit evaluator
# ------------------------------------------------------------------------

# simulating coalesce
# def image_width(num_pixels=None):
#     return num_pixels or 1280

# print(image_width(10))
# print(image_width())

# avoiding division by zero error
# def divide(num1, num2):
#     return num2 and num1 // num2

# print(divide(10,2))
# print(divide(10,0))

