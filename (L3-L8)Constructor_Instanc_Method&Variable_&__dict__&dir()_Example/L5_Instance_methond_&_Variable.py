"""Class Object Constructor attributes methods()"""

class Student:
        def __init__(self, name, Id):
                self.name = name # instance variable
                self.id = Id     # instance variable
                # print(self)
                # print("A student object is crated")
        def details(self):  # instance method
                print("Name:", self.name, "ID:", self.id)
                
#--------------------------------------------------------------
# variable = class_name()
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()
