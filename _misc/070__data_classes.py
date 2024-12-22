from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class MyDataClass:
    x: int
    y: int

    def __post_init__(self):
        if self.x < 0:
            raise ValueError("x must be bigger than 0")

md = MyDataClass(1, 2)
print(md.x)
print(md.y)

my_list = []
my_list.append(md)

print(my_list[0])

md1 = MyDataClass(1, 2)
my_list.append(md)

print(my_list[1])

print(md==md1)

md2 = MyDataClass(-1, 2)
