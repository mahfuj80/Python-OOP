class Student:        # Grand Parent class
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable
    
    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)

#================================================================

class CSEStudent(Student):        # Parent class
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs # instance variable

    def cry(self): # instance method
        print("CSE student is crying because of", self.no_of_labs, "lab(s)")

#================================================================
        
class CSEFresher(CSEStudent):        # Child class

    def enroll_CSE110(self):
        print(self.name, "Enrolled in CSE110")
    
#================================================================
        
s1 = CSEStudent("Bob", 11, 3)
s2 = CSEFresher("Carol", 55, 1)

s2.details()
s1.details()
s1.cry()
s2.cry()
s2.enroll_CSE110()