#abstraction j method er age thakbe sei method sob child class e thakte hbe

from abc import ABC, abstractmethod
class student(ABC):
    def add(self,a,b):
        self.x=a
        self.y=b
    @abstractmethod
    def display(self):                          #display method ta abstrat jeta child der modde thakbe
        print(f"This is {self.x} and {self.y}")
class details(student):
    def set(self):
        print("My name")
    def display(self):
        print("Her name")

bu=details()
bu.display()
# jeffy=student()
# jeffy.add(20,35)
# jeffy.display()
