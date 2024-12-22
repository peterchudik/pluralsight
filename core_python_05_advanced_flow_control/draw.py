from functools import singledispatch

from shapes import Rectangle, Circle, Polygon, Group

def attrs(shape):
    return ' '.join(
        f'{key}="{value}"' for key, value in
        {
            "stroke": shape.stroke_color,
            "stroke-width": shape.stroke_width,
            "fill": shape.fill_color
        }.items()
        if value is not None
    )

# this is version of draw function using generic funtion as decorator
# generic functions is Python answer for overloading function
# by type of its arguments
# generic function = @singledispatch decorator from functools standart library

@singledispatch
def draw(shape):
    raise TypeError(f"Can't draw shane {shape!r}")


# def draw(shape):
#     """Draw generic shape."""
    # This is not really nice code using if..elif..else

    # if isinstance(shape, Rectangle):
    #     return draw_rectangle(shape)
    # elif isinstance(shape, Circle):
    #     return draw_circle(shape)
    # elif isinstance(shape, Polygon):
    #     return draw_polygon(shape)
    # elif isinstance(shape, Group):
    #     return draw_group(shape)
    # else:
    #     raise TypeError(f"Can't draw shane {shape!r}")
    
    # This is nice code, but it relies on exact object type
    # So a subclass of circle would not draw circle

    # drawers = {
    #     Rectangle: draw_rectangle,
    #     Circle: draw_circle,
    #     Polygon: draw_polygon,
    #     Group: draw_group
    # }

    # try:
    #     drawer = drawers[type(shape)]
    # except KeyError:
    #     raise TypeError(f"Can't draw shane {shape!r}")
    # else:
    #     return drawer(shape)

    # This is another version based on globals() lookup
    # It relly on name convention of draw functions and class names
    
    # suffix = type(shape).__name__.lower()
    # drawer_name = f"draw_{suffix}"

    # try:
    #     drawer = globals()[drawer_name]
    # except KeyError:
    #     raise TypeError(f"Can't draw shane {shape!r}")
    # else:
    #     return drawer(shape)
@draw.register(Rectangle)
def _(rect):
# def draw_rectangle(rect):
    return (
        f'<rect '
        f'x="{rect.p[0]}" '
        f'y="{rect.p[1]}" '
        f'width="{rect.width}" '
        f'height="{rect.height}" '
        f'{attrs(rect)} />'
    )

@draw.register(Circle)
def _(circle):
# def draw_circle(circle):
    return (
        f'<circle '
        f'cx="{circle.center[0]}" '
        f'cy="{circle.center[1]}" '
        f'r="{circle.radius}" '
        f'{attrs(circle)} />'
    )

@draw.register(Polygon)
def _(polygon):
# def draw_polygon(polygon):
    return '<polygon points="{points}" {attrs} />'.format(
        points=" ".join(f"{p[0]} {p[1]}" for p in polygon.points),
        attrs=attrs(polygon)
    )

@draw.register(Group)
def _(group):
# def draw_group(group):
    return (
        '<g>\n{}\n</g>'.format(
            "\n".join(draw(shape) for shape in group.shapes)
        )
    )

def make_svg_document(min_x, min_y, max_x, max_y, shapes):
    """Make an SVG document from a collection of shapes."""
    return (
        '<svg viewBox="{min_x} {min_y} {width} {height}" xmlns="http://www.w3.org/2000/svg">'
        '\n{shapes}\n'
        '</svg>'.format(
            min_x=min_x,
            min_y=min_y,
            width=max_x - min_x,
            height=max_y - min_y,
            shapes="\n".join(draw(shape) for shape in shapes)
        )
    )

