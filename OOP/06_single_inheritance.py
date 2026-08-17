class A:
    def display1(e):
        print("This is class A")

class B(A):             #class b er modde class a k rakha hocce
    def display2(end):
        print("This is class B")

# x = B()             
# x.display1()
# x.display2()


class SICIP:
    def display1(num):
        print("Student Name")

class BASIS(SICIP):
    def display2(num):
        print("Student Age")
x= BASIS()
x.display1()
x.display2()