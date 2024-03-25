# Example of Constructor Overloading 
class Student:
        # # Constructor Methods
        # def __init__(self, name, Id):
        #         self.name = name # instance variable
        #         self.id = Id     # instance variable
        
        # # Another Constructor Methods
        # def __init__(self, name, Id, cg):
        #         self.name = name # instance variable
        #         self.id = Id     # instance variable
        #         self.CGPA = cg   # instance variable
        
        # # Another Constructor Methods
        # def __init__(self, *info):
        #         self.name = name # instance variable
        #         self.id = Id     # instance variable
        #         self.CGPA = cg   # instance variable
        

        # Another Constructor Methods
        # def __init__(self, *info):
        #         if len(info) == 3:
        #                 self.name = info[0]   # instance variable
        #                 self.id = info[1]     # instance variable
        #                 self.CGPA = info[2]   # instance variable
        #         elif len(info) == 2:
        #                 self.name = info[0]   # instance variable
        #                 self.id = info[1]     # instance variable
        #         elif len(info) == 1:
        #                 self.name = info[0]   # instance variable
                
        #         print ("A student Object Created")
                

        def __init__(self, **info):
                if len(info) == 3:
                        self.name = info['name']   # instance variable
                        self.id = info['Id']     # instance variable
                        self.CGPA = info['CG']   # instance variable
                elif len(info) == 2:
                        self.name = info['name']   # instance variable
                        self.id = info['Id']     # instance variable
                elif len(info) == 1:
                        self.name = info['name']   # instance variable
                
                print ("A student Object Created")
                

#=====================================================
# s1 = Student("Carol", 33, 3.95)
# s2 = Student("Bob", 11)
# s3 = Student("Mike")
# s4 = Student()
                

s1 = Student(name="Carol", Id=33, CG=4.0)
s1 = Student(name="Carol", Id=33)
s1 = Student(name="Carol")