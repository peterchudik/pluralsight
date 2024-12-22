class Test:

    class_attribute = 100

    def __init__(self):
        # self.class_attribute += 1
        # self.class_attribute = self.class_attribute + 1
        Test.class_attribute += 1


t1 = Test()
print(f"t1 : {t1.class_attribute}")
print(f"Test : {Test.class_attribute}")

t2 = Test()
print(f"t2 : {t2.class_attribute}")
print(f"Test : {Test.class_attribute}")

t3 = Test()
print(f"t3 : {t3.class_attribute}")
print(f"Test : {Test.class_attribute}")


