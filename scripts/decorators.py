# Decorators 
#
# Hanldes arguments within function calls using decorators.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        # start timer
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time : ", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(1000000):
        pass

@timer
def test2():
    time.sleep(2)

def func(f):
    # unpack operator
    def wrapper(*args, **kwargs):
        # start timer
        start = time.time()
        rv=f(*args, **kwargs)
        # total time taken to execute
        total = time.time() - start
        # rv used to return at end of wrapper
        print("Time : ", total)
        return rv

    return wrapper

# Print function 2 taking 2 arguments with sleeper of 1 second
@func
def func2(x, y):
    time.sleep(1)
    print(x, y)

# Print function 3 with sleeper of 1 second
@func
def func3():
    time.sleep(1)
    print("I am func 3")

@func
def func4(x,y):
    sum = x * y
    print(sum)
    return sum

test()
test2()
func2(5,6)
func3()
func4(3,3)


# x = func2(5, 6)
# print(x)
