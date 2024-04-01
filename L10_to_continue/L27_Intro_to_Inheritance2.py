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
        print("This method1 is in ParentClass Multilevel Inheritance")

class ChildClass1(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1 Multilevel Inheritance")

class ChildClass2(ChildClass1):
    def method3(self):
        print("This method3 is in ChildClass2 Multilevel Inheritance")

ch1 = ChildClass2()
ch1.method1()
ch1.method2()
ch1.method3()

#----------------------------------------------------------------

# Hierarchical Inheritance

class ParentClass:
    def method1(self):
        print("This method1 is in ParentClass Hierarchical Inheritance")

class ChildClass1(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1 Hierarchical Inheritance")

class ChildClass2(ChildClass1):
    def method3(self):
        print("This method3 is in ChildClass2 Hierarchical Inheritance")

class ChildClass3(ChildClass2):
    def method4(self):
        print("This method4 is in ChildClass3")



ch1 = ChildClass1()
ch2 = ChildClass2()

ch1.method1()
ch2.method1()
#----------------------------------------------------------------


# Multiple inheritance

class ParentClass1:
    def method1(self):
        print("This method1 is in ParentClass1 Multiple Inheritance")

class ParentClass2:
    def method2(self):
        print("This method2 is in ParentClass2 Multiple Inheritance")

class ChildClass(ParentClass1, ParentClass2):
    def method3(self):
        print("This method3 is in ChildClass Multiple Inheritance")

ch1 = ChildClass()
ch1.method1()
ch1.method2()
ch2.method3()

#----------------------------------------------------------------

# Hybrid inheritance

class ParentClass:
    def method1(self):
        print("This method1 is in ParentClass1 Hybrid Inheritance")

class ChildClass1(ParentClass):
    def method2(self):
        print("This method2 is in ChildClass1 Hybrid Inheritance")

class ChildClass2(ChildClass1):
    def method3(self):
        print("This method3 is in ChildClass2 Hybrid Inheritance")

class ChildClass3(ChildClass1):
    def method4(self):
        print("This method4 is in ChildClass3 Hybrid Inheritance")

ch1 = ChildClass3()

ch1.method1()
ch1.method2()

#----------------------------------------------------------------

