class Student:
    uni_name = "BracU"

    def __init__(self, name, Id):
        self.name = name # instance variable
        self.__id = Id     # instance variable

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id, "University:",Student.uni_name)

    # def up_uni_name(self, u_name):
    #     self.uni_name = u_name

    @classmethod
    def from_string(cls, info):
        name, Id = info.split('-')
        obj = cls(name, Id)
        return obj


s1 = Student("Bob", 11)
s2 = Student.from_string("Carol-47")

s1.details()
s2.details()
