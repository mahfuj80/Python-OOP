class Student:
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable
    
    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)

    def updt_ID(self, Id): # instance method
        if (Id > 0):
            self.__id = Id
        else:
            print("Invalid ID")


#--------------------------------------------------------------

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

s1.updt_ID(15)

s1.details()
s2.details()