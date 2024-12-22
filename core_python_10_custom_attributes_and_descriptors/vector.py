# Version 1
# class Vector():
#     """A two dimensional vector."""

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"{type(self).__name__}({self.x}, {self.y})"


# Version 2
# added dynamic attributes
# class Vector():
#     """An n-dimensional vector."""

#     def __init__(self, **components):
#         # update() - updates a dictionary
#         self.__dict__.update(components)
    
#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k,
#                     v=v
#                 ) for k, v in self.__dict__.items()
#             )
#         )


# Version 3
# added private attributes
# added __getattr__() method - invoked AFTER failed attribute lookup
# class Vector():
#     """An n-dimensional vector."""

#     def __init__(self, **components):
#         private_components = {f"_{k}":v for k, v in components.items()}
#         self.__dict__.update(private_components)

#     def __getattr__(self, name):
#         private_name = f"_{name}"
#         return getattr(self, private_name)
    
#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k[1:],
#                     v=v
#                 ) for k, v in self.__dict__.items()
#             )
#         )


# Version 4
# added read only attributes by overriding __setattr__
# __setattr__() intercepts all attribute writes
# class Vector():
#     """An n-dimensional vector."""

#     def __init__(self, **components):
#         private_components = {f"_{k}":v for k, v in components.items()}
#         self.__dict__.update(private_components)

#     def __getattr__(self, name):
#         private_name = f"_{name}"
#         return getattr(self, private_name)

#     def __setattr__(self, name, value):
#         raise AttributeError(f"Can't set an attribute {name!r}")

#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k[1:],
#                     v=v
#                 ) for k, v in self.__dict__.items()
#             )
#         )

# Version 5
# preventing reccursion error if we ask for attribute which do not exist directly or as _ version

# class Vector():
#     """An n-dimensional vector."""

#     def __init__(self, **components):
#         private_components = {f"_{k}":v for k, v in components.items()}
#         self.__dict__.update(private_components)

#     def __getattr__(self, name):
#         private_name = f"_{name}"
#         try:
#             return self.__dict__[private_name]
#         except KeyError:
#             raise AttributeError(f"{self!r} object has no attribute {name!r}")

#     def __setattr__(self, name, value):
#         raise AttributeError(f"Can't set an attribute {name!r}")

#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k[1:],
#                     v=v
#                 ) for k, v in self.__dict__.items()
#             )
#         )

# ultimate version
# Version 6
# preventing attributes deletion
# This is the version, which allow us:
#  -> to initialize our class with any number of attributes
#  -> store attributes in _ versions
#  -> prevent creating new attributes by overriding __setattr__
#  -> prevent deleting     attributes by overriding __delattr__
#  -> raising an error on attribute lookup if attribute does not exist

# class Vector():
#     """An n-dimensional vector."""

#     def __init__(self, **components):
#         private_components = {f"_{k}":v for k, v in components.items()}
#         self.__dict__.update(private_components)

#     def __getattr__(self, name):
#         private_name = f"_{name}"
#         try:
#             return self.__dict__[private_name]
#         except KeyError:
#             raise AttributeError(f"{self!r} object has no attribute {name!r}")

#     def __setattr__(self, name, value):
#         raise AttributeError(f"Can't set an attribute {name!r}")

#     def __delattr__(self, name):
#         raise AttributeError(f"Can't delete an attribute {name!r}")

#     def __repr__(self):
#         return "{}({})".format(
#             type(self).__name__,
#             ", ".join(
#                 "{k}={v}".format(
#                     k=k[1:],
#                     v=v
#                 ) for k, v in self.__dict__.items()
#             )
#         )


# Version 7
# storring class attributes differently instead of directly in the __dict__
# stores mutable red, green, blue color as a list in __dict__ under key "_color"
# added ColoredVector class
# modified __repr__ of Vector
# added _args to be able to override it in child class in order the __repr__ in parent class to work fine
class Vector():
    """An n-dimensional vector."""

    def __init__(self, **components):
        private_components = {f"_{k}":v for k, v in components.items()}
        self.__dict__.update(private_components)

    def __getattr__(self, name):
        private_name = f"_{name}"
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError(f"{self!r} object has no attribute {name!r}")

    def __setattr__(self, name, value):
        raise AttributeError(f"Can't set an attribute {name!r}")

    def __delattr__(self, name):
        raise AttributeError(f"Can't delete an attribute {name!r}")

    def __repr__(self):
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                "{k}={v}".format(
                    k=k,
                    v=v
                ) for k, v in self._args().items()
            )
        )
    
    def _args(self):
        return {k[1:]: v for k, v in self.__dict__.items()}


# stores mutable red, green, blue color as a list in __dict__ under key "_color"
class ColoredVector(Vector):
    COLOR_INDEXES = ("red", "green", "blue")

    def __init__(self, red, green, blue, **components):
        super().__init__(**components)
        self.__dict__["_color"] = [red, green, blue]
    
    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__["_color"][channel]
    
    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__setattr__(name, value)
        else:
            self.__dict__["_color"][channel] = value

    def _args(self):
        args = {
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
        }
        args.update(super()._args())
        del args["color"]
        return args
