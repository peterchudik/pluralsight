import inspect
import reprlib
from pprint import pprint as pp
import itertools

def dump(obj):
    print("Type")
    print("====")
    print(type(obj))
    print()

    print("Documentation")
    print("=============")
    # Get the documentation string for an object.
    print(inspect.getdoc(obj))
    print()

    # dir() -> return list
    all_attr_names = set(dir(obj))
    # filter(function, iterable) -> return an iterator yielding those items of iterable for which function(item) is true.
    # lambda arguments : expression -> expression is executed and returned
    # callable() -> Return whether the object is callable
    # getattr(object, name) -> value -> get a named attribute from an object
    method_names = set(
        filter(lambda attr_name: callable(getattr(obj, attr_name)),
               all_attr_names)
               )
    # check if method_names is subset of all_attr_names
    # <= - relation operator on sets to test issubset
    assert method_names <= all_attr_names
    # get not callable attributes by substracting method_names from all_attr_names
    attr_names = all_attr_names - method_names


    print("Attributes")
    print("==========")
    # produce list of tuples
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name))) for name in attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    print()


    print("Methods")
    print("=======")
    methods = (getattr(obj, method_name) for method_name in method_names)
    # sorted(iterable) -> return a new list containing all items from the iterable in ascending order.
    # produce list of tuples
    method_names_and_doc = sorted((full_sig(method), brief_doc(method)) for method in methods)
    print_table(method_names_and_doc, "Name", "Description")
    print()

def full_sig(method):
    # EAFP
    try:
        # signature(method) -> get a signature object for the passed callable.
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + "(...)"

def brief_doc(obj):
    # LBYL
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        # len() -> Return the number of items in a container
        if len(lines) > 0:
            return lines[0]
    return ""

def print_table(rows_of_columns, *headers):

    # get number of columns from first row
    num_columns = len(rows_of_columns[0])

    # get number of headers from *args tuple
    num_headers = len(headers)

    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, "
                        "got {}".format(num_columns, num_headers))

    # add header tuple into first position of list
    # we get [("Name", "Value"), ("N1", "1"), ("N2", "2")]
    rows_of_columns_with_header = itertools.chain([headers], rows_of_columns)

    # zip -> list(zip('abcdefg', range(3), range(4))) == [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    # we get [("Name", "N1", "N2"), ("Value", "1", "2")]
    columns_of_rows = list(zip(*rows_of_columns_with_header))

    # map(func, *iterables) --> map object
    # Make an iterator that computes the function using arguments from each of the iterables.
    # we get max width of each column = [4, 5]
    column_widths = [max(map(len, column)) for column in columns_of_rows]

    # {{ -> escape
    # we get generator object which yields -> '{:4}' '{:5}'
    column_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)

    # we get string -> "'{:4}' '{:5}'"
    format_spec = ' '.join(column_specs)

    # print headers with max with
    print(format_spec.format(*headers))

    # get tuple = ("----", "-----")
    rules = ("-" * width for width in column_widths)

    # print it
    print(format_spec.format(*rules))

    # print row
    for row in rows_of_columns:
        print(format_spec.format(*row))


