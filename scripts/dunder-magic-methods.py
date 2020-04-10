import inspect
from queue import Queue as q

# Dunder && Magic Methods
#
class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    # add to queue
    def __add__(self, item):
        self.put(item)
    # sub from queue
    def __sub__(self, item):
        self.get()

# printing the queue length
q = Queue()
q + 9
q + 100
q - 1
print(q)

class Person:
    def __init__(self, name):
        self.name = name
    # Dunder methods
    def __repr__(self):
        return f"Person({self.name})"
    # multiplication Dunder operation
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument , must be int")
        self.name = self.name * x
    # call Dunder method
    def __call__(self, y):
        print("Called function", y)
    # Length dunder method
    def __len__(self):
        return len(self.name)
    

p = Person("Aaron")
p * 1
p(4)
print(len(p))
print(p)
print(p.name)

# lists
x = [1,2,3]
y = [4,5]

# print lists
print(x+y)
print(x * 3)
print(len(x))
print(x[0])
print(x[::-1])
print(type(x))
