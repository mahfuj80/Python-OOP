class Student:
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable
    
    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)

#================================================================

class CSEStudent(Student):
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs # instance variable

    def cry(self): # instance method
        print("CSE student is crying because of", self.no_of_labs)

#================================================================

class BBAStudent(Student):
    def party(self): # instance method
        print("All day party")

#================================================================

s1 = CSEStudent("Bob", 11, 3) 
s2 = BBAStudent("Carol", 36)
s1.cry()
s1.details()
print("-----------S1 Help-----------\n")
print(help(s1))
print("-----------S2 Help-----------\n")
print(help(s2))