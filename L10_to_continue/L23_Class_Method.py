class Student:
    uni_name = "BracU"

    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id, "University",Student.uni_name)

    # def up_uni_name(self, u_name):
    #     self.uni_name = u_name

    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name


s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()
s2.details()
Student.up_uni_name("Brac University")
s1.details()
s2.details()