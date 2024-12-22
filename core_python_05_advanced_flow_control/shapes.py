class Shape:

    def __init__(self, *, stroke_color=None, fill_color=None, stroke_width=None):
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.fill_color = fill_color

    # def attrs(self):
    #     return ' '.join(
    #         f'{key}="{value}"' for key, value in
    #         {
    #             "stroke": self.stroke_color,
    #             "stroke-width": self.stroke_width,
    #             "fill": self.fill_color
    #         }.items()
    #         if value is not None
    #     )


class Rectangle(Shape):

    def __init__(self, p, width, height, **kwargs):
        super().__init__(**kwargs)
        self.p = p
        self.width = width
        self.height = height

    # def draw(self):
    #     return (
    #         f'<rect '
    #         f'x="{self.p[0]}" '
    #         f'y="{self.p[1]}" '
    #         f'width="{self.width}" '
    #         f'height="{self.height}" '
    #         f'{self.attrs()} />'
    #     )


class Circle(Shape):

    def __init__(self, center, radius, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.radius = radius

    # def draw(self):
    #     return (
    #         f'<circle '
    #         f'cx="{self.center[0]}" '
    #         f'cy="{self.center[1]}" '
    #         f'r="{self.radius}" '
    #         f'{self.attrs()} />'
    #     )


class Polygon(Shape):

    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

    # def draw(self):
    #     return '<polygon points="{points}" {attrs} />'.format(
    #         points=" ".join(f"{p[0]} {p[1]}" for p in self.points),
    #         attrs=self.attrs()
    #     )


class Group:

    def __init__(self, shapes):
        self.shapes = shapes

    # def draw(self):
    #     return (
    #         '<g>\n{}\n</g>'.format(
    #             "\n".join(shape.draw() for shape in self.shapes)
    #         )
    #     )


# def make_svg_document(min_x, min_y, max_x, max_y, shapes):
#     """Make an SVG document from a collection of shapes."""
#     return (
#         '<svg viewBox="{min_x} {min_y} {width} {height}" xmlns="http://www.w3.org/2000/svg">'
#         '\n{shapes}\n'
#         '</svg>'.format(
#             min_x=min_x,
#             min_y=min_y,
#             width=max_x - min_x,
#             height=max_y - min_y,
#             shapes="\n".join(shape.draw() for shape in shapes)
#         )
#     )
