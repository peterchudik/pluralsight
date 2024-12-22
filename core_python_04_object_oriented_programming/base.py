class Base:
    def __init__(self):
        print('Base initializer')
    def f(self):
        print('Base.f()')


class Sub(Base):
    # if you define __init__ in the subclass, __init__ of base class will not be called
    # to call it, you need to do it explicitly
    def __init__(self):
        print('Sub initializer')
        super().__init__()
    def f(self):
        print('Sub.f()')
