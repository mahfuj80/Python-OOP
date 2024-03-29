class Student:
    uni_name = "BracU"

    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id, "University:",Student.uni_name)

    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name
    
    @staticmethod
    def check_department(Id):
        if Id[3:5] == "01" : print("CSE")
        elif Id[3:5] == "47" : print("EEE")

#----------------------------------------------------------

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

Student.check_department("15301007")
