#decorator

def changecase(func):
    def myinner():
        return func().upper()
        # return func().lower()
    return myinner

@changecase
def myfunction():
    return "Hello jeffy"
print(myfunction())



def decorator(func):
    def wrapper():
        print("Before calling")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hi Maya's Jahan")
greet()