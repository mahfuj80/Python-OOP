class A:
    def __init__(self):
        print("__init__ of class A")
    
    def method1(self):
        print("This method1 is in class A")

#================================================================

class B:
    def __init__(self):
        print("__init__ of class B")
    
    def method1(self):
        print("This method1 is in class B")

#================================================================
        
class C(B, A): # Class Order Matters
    def __init__(self):
        print("__init__ of class C")
    
    def method2(self):
        print("This method1 is in class C")

#================================================================
        
c1 = C()

c1.method1()
B.method1(c1)