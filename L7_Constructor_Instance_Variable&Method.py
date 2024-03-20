class Car:
        def __init__(self, name, model):
                self.name = name        # instance variable
                self.model_year = model # instance variable
                self.wheel = 4
        def view(self):
                print("The model year of this ",  self.name , "is ", self.model_year)
                print("The wheels of this ",  self.name, "is ", self.wheel)
                
c1 = Car("Bmw", 2016)
c2 = Car("Audi", 2018)

c1.view()
c2.view()
