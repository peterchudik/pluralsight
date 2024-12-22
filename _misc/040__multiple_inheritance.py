class A:
    def func(self):
        print("A.func")

class B(A):
    def func(self):
        print("B.func")
        s = super()
        print(f"super : {s}")
        s.func()
        # print(s.func())
        # super().func()

class C(A):
    def func(self):
        print("C.func")
        super().func()

class D(B, C):
    pass

t = D()
# t.func()

# print(D.__mro__)

print(super(B, t).func)
