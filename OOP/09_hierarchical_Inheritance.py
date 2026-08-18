class Parent:  # Base class
      def func1(self):
          print("This function is in parent class.")
 
class Child1(Parent): # Derived class1
      def func2(self):
          print("This function is in child 1.")
 
class Child2(Parent): # Derivied class2
      def func3(self):
          print("This function is in child 2.")
  
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
