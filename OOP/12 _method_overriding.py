#2ta class er modde same method thakle child method ta kaj korbe ata overriding hocce

# Defining parent class
class Parent():
    def ABC(self):
        # self.value = "Inside Parent"
        print("This is ABC")
                                    #akta class er modde 2ta method same hole er modde update ta nile seta overloading
    # Parent's show method
    def ABC(self):
        print("This is ?")

# Defining child class
class Child(Parent):

    # Constructor
    def XYZ(self):
        # self.value = "Inside Child"
        print("This is ami")

obj1 = Parent()
obj2 = Child()

obj1.ABC()
obj2.XYZ()
