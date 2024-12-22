class ChessCoordinate:

    # for interning, we will store all instance in the class attribute = dictionary
    # class attribute (dictionary in this case) will be shared across all instances of this class
    _interned = {}

    # __new__
    # is implicit static method
    # accepts class as first argument
    # cls is class of object to be allocated
    # additionally it accepts all arguments passed to the constructor call, like ChessCoordinate("d", 4)

    # def __new__(cls, *args, **kwargs):
    #     # prints for debugging
    #     # print(f"cls = {cls.__name__}")
    #     # print(f"args = {args!r}")
    #     # print(f"kwargs = {kwargs!r}")

    #     # allocate (construct) new object by callin base class object method __new__
    #     obj = object.__new__(cls)

    #     # prints for debugging
    #     # we cannot yet use repr, as it has not been yet initialized
    #     # print(f"id(obj) = {id(obj)}")

    #     # must return the newly allocated object
    #     return obj

    # practical use of ovveriding__new__is interning technique
    # interning = re-using objects of same value on demand instead of creating new objects
    # interning should be only used for immutable value types
    # python uses it internally for example for int ans str objects

    def __new__(cls, file, rank):
        # normally, validations of attributes would be in init
        # because of interning, it is moved to here
        if len(file) != 1:
            raise ValueError(
                f"{cls.__name__} component file {file!r} "
                f"does not have length one."
            )

        if file not in "abcdefgh":
            raise ValueError(
                f"{cls.__name__} component file {file!r} "
                f"is out of range."
            )

        if rank not in range(1, 9):
            raise ValueError(
                f"{cls.__name__} component rank {rank!r} "
                f"is out of range."
            )

        # interning -> only create new object, if it do not already exists
        key = (rank, file)
        if key not in cls._interned:
            obj = object.__new__(cls)
            obj._file = file
            obj._rank = rank
            cls._interned[key] = obj
        return cls._interned[key]

    # is not creating object, it is just initializing already created object
    # def __init__(self, file, rank):
        # prints for debugging
        # print(f"id(self) = {id(self)}")

        # file a-h
        # rank 1-8
        # if len(file) != 1:
        #     raise ValueError(
        #         f"{type(self).__name__} component file {file!r} "
        #         f"does not have length one."
        #     )

        # if file not in "abcdefgh":
        #     raise ValueError(
        #         f"{type(self).__name__} component file {file!r} "
        #         f"is out of range."
        #     )

        # if rank not in range(1, 9):
        #     raise ValueError(
        #         f"{type(self).__name__} component rank {rank!r} "
        #         f"is out of range."
        #     )

        # self._file = file
        # self._rank = rank

        # pass

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return f"{type(self).__name__}(file = {self.file}, rank = {self.rank})"
        
    def __str__(self):
        return f"{self.file}{self.rank}"

def starting_board():
    return {
        # should use better keys than just numberring
        # white
        '1' : ChessCoordinate('a', 1),
        '2' : ChessCoordinate('b', 1),
        '3' : ChessCoordinate('c', 1),
        '4' : ChessCoordinate('d', 1),
        '5' : ChessCoordinate('e', 1),
        '6' : ChessCoordinate('f', 1),
        '7' : ChessCoordinate('g', 1),
        '8' : ChessCoordinate('h', 1),
        '9' : ChessCoordinate('a', 2),
        '10': ChessCoordinate('b', 2),
        '11': ChessCoordinate('c', 2),
        '12': ChessCoordinate('d', 2),
        '13': ChessCoordinate('e', 2),
        '14': ChessCoordinate('f', 2),
        '15': ChessCoordinate('g', 2),
        '16': ChessCoordinate('h', 2),
        # black
        '17': ChessCoordinate('a', 8),
        '18': ChessCoordinate('b', 8),
        '19': ChessCoordinate('c', 8),
        '20': ChessCoordinate('d', 8),
        '21': ChessCoordinate('e', 8),
        '22': ChessCoordinate('f', 8),
        '23': ChessCoordinate('g', 8),
        '24': ChessCoordinate('h', 8),
        '25': ChessCoordinate('a', 7),
        '26': ChessCoordinate('b', 7),
        '27': ChessCoordinate('c', 7),
        '28': ChessCoordinate('d', 7),
        '29': ChessCoordinate('e', 7),
        '30': ChessCoordinate('f', 7),
        '31': ChessCoordinate('g', 7),
        '32': ChessCoordinate('h', 7),
    }

def main():
    # white_queen = ChessCoordinate("d", 4)
    # print(f"{white_queen!r}") # repr
    # print(f"{white_queen!s}") # str
    # print(white_queen) # str

    # for tracing memory usage
    import tracemalloc
    tracemalloc.start()
    boards = [starting_board() for _ in range(10000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    peak_kb = peak / 1024
    print(f"{peak_kb:.0f} kB")

if __name__ == "__main__":
    main()


