class Student:
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.id = Id     # instance variable
        print(self)
    
    def __str__(self):
        return "My name is " + self.name

#=============================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 11)

# print(s1.__str__())
# print(s1)
