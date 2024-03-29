class ABC:
    def __init__(self, x, y):
        self.x = x
        self.__y = y
    
    def details(self):
        print("X:",self.x, "Y:",self.__y)
    


#----------------------------------------------------------------

a1 = ABC(5, 6)
a2 = ABC(15, 17)

print(a1.x)

a1.details()


class Student:
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)
        self.__method()

    def __method(self):
        print("Private Method Executed")

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)


s1.details()