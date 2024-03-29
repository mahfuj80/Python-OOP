class Student:
    counter =  0
    def __init__(self, name, Id):
        self.name = name # instance variable
        self.id = Id     # instance variable
        Student.counter += 1 # increment

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.id, 
              "Student count:", Student.counter)
    
#--------------------------------------------------------------

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s3 = Student("Mike", 33)

s1.details()