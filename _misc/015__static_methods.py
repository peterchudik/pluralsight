class Test:

    @staticmethod
    def my_static_method():
        print("I am static method of Test")
    
    def __init__(self):
        # Test.my_static_method()
        self.my_static_method()


class TestChild(Test):

    @staticmethod
    def my_static_method():
        print("I am static method of TestChild")

t = Test()
tc = TestChild()


