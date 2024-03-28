class Vaccine:
        def __init__(self, name, md_in, intrvl):
                self.name = name
                self.md_in = md_in
                self.intrvl = intrvl
#============================================================
class Person:
        def __init__(self, pname, age, ptype="General Citizen"):
                self.pname = pname
                self.age = age
                self.ptype = ptype
                self.vac = ""
                self.firstdose = False
                self.seconddose = False
        def pushVaccine(self, vacN, dose="1st dose"):
                if dose == "1st dose":
                        if self.age >= 25 or self.ptype == "Student":
                                self.vac = vacN # storing object of vaccine
                                self.firstdose = True
                        else:
                                print("Sorry", self.pname, "Minimum age for taking vaccine is wrong")
                        
                else:
                        if self.vac.name != vacN.name:
                                print("Sorry", self.pname, "You Can't Take 2 different Vaccine")
                        elif self.firstdose == True:
                                self.seconddose = True
                                print("2nd dose done for", self.pname)
        def showDetail(self):
                print("Name:", self.pname, "Age:", self.age, "Type:", self.ptype)
                print("Vaccine Name:", self.vac.name)
                if self.seconddose == True:
                        print("First dose given")
                        print("Second dose given")
                elif self.firstdose == True:
                        print("First dose given")
                        print("2nd dose: Please come after", self.vac.intrvl, "days")


# Creating a Vaccine object
vaccine1 = Vaccine("Pfizer", "Moderna", 21)

# Creating a Person object
person1 = Person("John", 30)

# Pushing vaccine for the person
person1.pushVaccine(vaccine1)

# Showing details of the person
person1.showDetail()