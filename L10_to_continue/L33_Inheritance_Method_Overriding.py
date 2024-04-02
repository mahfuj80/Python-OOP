'''Method Overriding Example'''

class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("little Bit Study")
    
    def method2(self):
        print("You will get all of by properties and methods")

#=============================================================

class B(A):
    def __init__(self):
        super().__init__()
        print("__init__ of class B")

    def method1(self):
        super().method1()
        print("Always Party")

#=============================================================

b1 = B()
b1.method1()
