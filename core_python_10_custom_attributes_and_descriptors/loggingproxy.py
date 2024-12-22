class LoggingProxy():
    """Intercepts and logs all attributes access to an object."""

    def __init__(self, target):
        # self.target = target -> would invoke __getattribute__, which we dont want
        # that is why we invoke __setattr__ from superclass (base python object)
        super().__setattr__("target", target)

    # is invoked for all attribute access, basically anytime we use . 
    def __getattribute__(self, name):
        target = super().__getattribute__("target")
        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError(
                "{} could not forward request {} to {}".format(
                    super().__getattribute__("__class__").__name__,
                    name,
                    target,
                )
            ) from e
        print(f"Retrieved attribute {name} == {value!r} from {target!r}")
        return value

    def __setattr__(self, name, value):
        target = super().__getattribute__("target")
        try:
            value = setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError(
                "{} could not forward request {} to {}".format(
                    super().__getattribute__("__class__").__name__,
                    name,
                    target,
                )
            ) from e
        print(f"Set attribute {name} == {value!r} on {target!r}")

    def __repr__(self):
        target = super().__getattribute__("target")
        repr_callable = getattr(target, "__repr__")
        return repr_callable()

