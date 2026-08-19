#parent class er sob method child class e thakte hbe tahole seta interface

from abc import ABC, abstractmethod

class Greet(ABC):   
    @abstractmethod
    def tell_hello(self):
        pass  # Abstract method

class English(Greet):
    def tell_hello(self):
        return "Hello!"

g = English()
print(g.tell_hello())
