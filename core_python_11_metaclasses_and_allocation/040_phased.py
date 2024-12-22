class PhasedMeta(type):
    
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        obj._pre_init(*args, **kwargs)
        obj.__init__(*args, **kwargs)
        obj._post_init(*args, **kwargs)

class PhasedInit(metaclass=PhasedMeta):

    def _pre_init(self):
        print("Pre-Initialization")

    def __init__(self):
        print("Initialization")

    def _post_init(self):
        print("Post-Initialization")

class SubPhasedInit(PhasedInit):

    def __init__(self):
        super().__init__()
        print("Sub-Initialization")

if __name__ == "__main__":
    p = SubPhasedInit()
    print(p)
