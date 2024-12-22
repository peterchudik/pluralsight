class Test:

    @classmethod
    def my_class_method(cls):
        print(f"I am method of class {cls}")

    @classmethod
    def my_named_constructor(cls, init_value, *args, **kwargs):
        return cls(init_value, *args, **kwargs)
    
    def __init__(self, init_value, *args, **kwargs):
        self.init_value = init_value


class TestChild(Test):
    # pass

    def __init__(self, init_value, *, another_init_value, **kwargs):
        # self.init_value = init_value
        super().__init__(init_value)
        self.another_init_value = another_init_value
        # self.another_init_value = args[0]

# t = Test()
# t.my_class_method()
# print(t)

t1 = Test.my_named_constructor(0)
print(t1)
print(t1.init_value)

# tc = TestChild()
# tc.my_class_method()

tc = TestChild.my_named_constructor(0, another_init_value = 1)
print(tc)
print(tc.init_value)
print(tc.another_init_value)

