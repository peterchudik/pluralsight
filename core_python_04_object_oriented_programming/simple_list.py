class SimpleList:
    def __init__(self, items):
        self._items = list(items)
    
    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"

class SortedList(SimpleList):
    def __init__(self, items=()):
        s = super()
        print(f"SortedList {s}")
        s.__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        s = super()
        print(f"IntList {s}")
        s.__init__(items)
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values')
    
    def add(self, item):
        self._validate(item)
        super().add(item)

class SortedIntList(IntList, SortedList):
    pass
    # if class has no __init__ then only the __init__ of first base class is called automatically
