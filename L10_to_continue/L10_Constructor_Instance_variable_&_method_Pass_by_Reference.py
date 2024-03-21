class Cat:
        def __init__(self, color, action):
                self.color = color
                self.action = action
        
        def view(self):
                print(self.color,"Cat iss", self.action)

        
        def compare(self, ct):
                if self.action == ct.action:
                        print("Both cats are Doing Same Action:", self.action)
                else:
                        print("They Are in Different Action:", self.action , "&" , ct.action) 

# =================================================================

# c1 = Cat.objects.all()
c1 = Cat("White", "jumping")
c2 = Cat("Brown", "jumping")

c1.view()
c2.view()

c1.compare(c2)