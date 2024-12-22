import inspect

def decorate_with_repr(cls):
    
    # members = vars(cls)

    # for name, member in members.items():
    #     print(name, " : ", member)
    
    # if '__repr__' in members:
    #     raise TypeError(f"{cls.__name__} already has __repr__")

    # if '__init__' not in members:
    #     raise TypeError(f"{cls.__name__} does not have __init__")
    
    # parameter_names = list(inspect.signature(cls.__init__).parameters)[1:]

    # if not all(
    #     isinstance(members.get(name, None), property)
    #     for name in parameter_names
    # ):
    #     raise TypeError(f"{cls.__name__} does not have all __init__ parameters as properties")
    
    def new_repr(self):
        return "I am newly added by decorator"

    setattr(cls, '__repr__', new_repr)

    return cls

@decorate_with_repr
class ToBeDcorated:

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    # def __repr__(self):
    #     pass

print(vars(ToBeDcorated))

print(ToBeDcorated(1, 2))

