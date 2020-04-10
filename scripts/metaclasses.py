# Basic implementation of metaclasses
#
# Meta Class
class Meta(type):
    # modify how class is constructed
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {} # blank dictionary
        # loop through all attributes
        for name, value in attrs.items():
            if name.startswith("__"):
                # add proper value
                a[name] = value
            else:
                # change to upper case
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, attrs)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hi from Dog class")

d = Dog()
d.hello()

# Basic class
class Foo:
    def show(self):
        print("Hi")

def add_attribute(self):
    self.z = 9


# Metaclass 
MetaTest = type('MetaTest', (Foo,), {"x":5, "add_attribute": add_attribute})

m = MetaTest()
my = "Hello"
print(m.x)
print(my)
m.show()
t = MetaTest()
t.add_attribute()
# print(t.z)

# print the object
print(MetaTest)
print(type(MetaTest))

