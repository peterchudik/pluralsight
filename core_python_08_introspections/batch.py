from itertools import chain

class Batch():
    def __init__(self, iterable=()):
        self._iterables = []
        self._iterables.append(iterable)
    
    def append(self, iterable):
        self._iterables.append(iterable)
    
    def __iter__(self):
        return chain(*self._iterables)
