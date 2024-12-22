class Test:

    def __init__(self):
        print("Init")
        self._my_property = 1

    @property
    def my_property(self):
        return self._my_property
    
    # @my_property.setter
    # def my_property(self, value):
    #     if value < 10:
    #         raise ValueError("Value too low")
    #     self._my_property = value

    def _validate_my_property(self, value):
        if value < 10:
            raise ValueError("Value too low")
        return value

    @my_property.setter
    def my_property(self, value):
        self._my_property = self._validate_my_property(value)
    


class TestChild(Test):

    # @Test.my_property.setter
    # def my_property(self, value):
    #     # self._my_property = value
    #     # super().my_property = value
    #     if value > 20:
    #         raise ValueError("Value too high")
    #     Test.my_property.fset(self, value)

    def _validate_my_property(self, value):
        if value > 20:
            raise ValueError("Value too high")
        return super()._validate_my_property(value)

# t = Test()
# t.my_property = 2
# print(t.my_property)


tc = TestChild()
tc.my_property = 21
print(tc.my_property)
