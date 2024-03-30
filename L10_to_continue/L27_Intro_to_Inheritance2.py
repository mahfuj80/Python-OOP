# Single Inheritance Example
class ParentClass:
    def method1(self):
        print("This method1 is in ParentClass Single Inheritance")

class ChildClass(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1 Single Inheritance")

m1 = ChildClass()
m1.method1()

#----------------------------------------------------------------

# Multilevel Inheritance Example
class ParentClass:
    def method1(self):
        print("This method1 is in ParentClass")

class ChildClass1(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1")

class ChildClass2(ChildClass1):
    def method3(self):
        print("This method3 is in ChildClass2")

ch1 = ChildClass2()
ch1.method1()
ch1.method2()
ch1.method3()

#----------------------------------------------------------------

# Hierarchical Inheritance