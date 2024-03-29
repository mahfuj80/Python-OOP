class Student:
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable
    
    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)

    def set_ID(self, Id): # instance method
        if (Id > 0):
            self.__id = Id
        else:
            print("Invalid ID")
    
    def get_ID(self):
        return self.__id
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    


#--------------------------------------------------------------

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

s1.set_ID(55)
print(s1.get_ID())
s1.set_name("Mike")
print(s1.get_name())
s1.details()
s2.details()