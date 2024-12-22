from collections.abc import Sequence, Set
from itertools import chain
from bisect import bisect_left

class SortedFrozenSet(Sequence, Set):
    
    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items) if items is not None
            else set()
        ))

    def __contains__(self, item):
        # O(n) version
        # return item in self._items
        # O(log n) version
        index = bisect_left(self._items, item)
        return (index != len(self._items) and self._items[index] == item)
        

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        
        return iter(self._items)
        
        # alternative, but probably slower
        # for item in self._items:
        #     yield item

    def __getitem__(self, index):
        # return self._items[index]
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )

    def __repr__(self):
        return "{type}({arg})".format(
            type = type(self).__name__,
            arg = (
                "[{}]".format(
                    ", ".join(
                        map(repr, self._items)
                    )
                )
                if self._items else ""
            )
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items

    def __hash__(self):
        return hash(
            (type(self), self._items)
        )

    def __add__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return SortedFrozenSet(
            chain(self._items, rhs._items)
        )

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedFrozenSet()

    def __rmul__(self, lhs):
        return self * lhs

    # lets overide count() from Sequence to use binary search
    # as our list is sorted and has unique elements
    def count(self, item):
        # search for index using O(log n) complexity
        # index = bisect_left(self._items, item)
        # found = (index != len(self._items) and self._items[index] == item)
        # return int(found)
        
        # refactor using optimized __contains__
        return int(item in self)
    
    # lets overide index() from Sequence to use binary search
    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items) and self._items[index] == item):
            return index
        raise ValueError(f"{item!r} not found")

    def issubset(self, iterable):
        return self <= SortedFrozenSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedFrozenSet(iterable)

    def intersection(self, iterable):
        return self & SortedFrozenSet(iterable)

    def union(self, iterable):
        return self | SortedFrozenSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedFrozenSet(iterable)

    def difference(self, iterable):
        return self - SortedFrozenSet(iterable)
