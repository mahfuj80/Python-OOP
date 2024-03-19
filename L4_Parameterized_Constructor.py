"""Class Object Constructor attributes methods()"""

class Student:
        def __init__(self, name, Id):
                self.name = name # stance variable
                self.id = Id     # stance variable
                # print(self)
                # print("A student object is crated")

#--------------------------------------------------------------
# variable = class_name()
s1 = Student("Badhon", 1)
s2 = Student("Bob", 2)

print(s2.id)
s1.id = 42
print(s1.id)

# print("s1",s1)
# print("s2",s2)