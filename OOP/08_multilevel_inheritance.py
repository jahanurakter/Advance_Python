class A:
    def display1(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

class C(B):
    def display3(self):
        print("This is class C")

objC = C()
objC.display1()
objC.display2()
objC.display3()