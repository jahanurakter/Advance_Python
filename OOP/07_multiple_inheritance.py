#multiple - a class can take multiple parents

class A:
    def display1(self):
        print("This is class A")

class B:
    def display2(self):
        print("This is class B")

class C(A,B):
    def display3(self):
        print("This is class C")

objC = C()
objC.display1()
objC.display2()
objC.display3()