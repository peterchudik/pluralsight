class OneShotNamespace(dict):

    def __init__(self, name, existing=None):
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing.items():
                self[k] = v
    
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(
                f"Cannot reassign attribute {key!r}"
                f" of a class {self._name!r}"
            )
        super().__setitem__(key, value)

class ProhibitDuplicatesMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        return OneShotNamespace(name)

# class Dodgy:
class Dodgy(metaclass=ProhibitDuplicatesMeta):

    # def method(self):
    #     print("First definition")

    def method(self):
        print("Second definition")


if __name__ == "__main__":
    # d = OneShotNamespace("my_dict", {'A': 1, 'B': 2})
    # d['A'] = 1
    # d['B'] = 2
    # print(d)
    # d['B'] = 3
    d = Dodgy()
    d.method()

