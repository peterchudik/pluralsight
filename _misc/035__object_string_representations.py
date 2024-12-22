class Test:

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __repr__(self):
        # return(f"Test(x={self._x}, y={self._y})")
        return(f"{type(self).__name__}(x={self._x}, y={self._y})")

    def __str__(self):
        return(f"Position x={self._x}, Position y={self._y}")

    def __format__(self, format_spec):
        return("FORMATTED")

class TestChild(Test):
    pass
    

t = Test(10, 20)

print(f"repr : {repr(t)}")
print(f"str : {str(t)}")
print(f"format : {format(t)}")
print(f"format : {t}")
print("format : {}".format(t))

# print(dir(t))

# tc = TestChild(10, 20)

# print(f"repr : {repr(tc)}")
# print(f"str : {str(tc)}")
# print(f"format : {format(tc)}")
