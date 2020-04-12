import inspect
from queue import Queue

# Creating Class Consstructor
def make_class(x):
    class Human:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def print_value(self):
            print(x)
    return Human

cls = make_class(10)
# Prints memory location
# <class '__main__.make_class.<locals>.Dog'>
print(cls)
d = cls("Aaron", 21)
print(d.name, d.age)
d.print_value()

# Function inside of for loop
for i in range(10):
    def show():
        print(i*2)
    show()

# Making and executing functions inside of if/else statements
def func(x):
    if x == 1:
        def rv():
            print("X is equal to 1")
    else:
        def rv():
            print("X is not equal to 1")
    return rv

def func2(x):
    if x == "Aaron":
        def add():
            print("Hello Aaron.")
    else:
        def add():
            print("Hello, Stranger.")
    return add

# Calling Functions
new_func = func(1)
new_func()
new_func = func(2)
new_func()
new_func2 = func2("Aaron")
new_func3 = func2("John")
new_func2()
new_func3()

# inspect our functions
# displays memory address
print(id(new_func()))
# print(inspect.getmembers(new_func()))
# inspect and display our source code for specific functions
print(inspect.getsource(new_func))
# inspect and display source code using Queue
# print(inspect.getsource(Queue))