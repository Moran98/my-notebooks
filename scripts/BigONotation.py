# @author Aaron Moraan
# Big-O-Notation
#
# Big-O help compare and classify functions by their speed of convergence.
# When comparing algorithm performance, we are interested in the number of operations that an algorithm performs.
# TIME COMPLEXITY
import timeit
print("============Big-O-Notation============")

# Simple loop 
def timer(n):
    x = 1
    for i in range(n):
        # if n = 5 ----> 1*2*3*4*5
        x = x * (i+1)
    # timer to calc the time taken to carry out
    print(timeit.timeit('output = 10*5'))
    return x

# Simple if/else 
def timer2(n):
    # n = 5 ---> same as above except using recursive
    if n == 0:
        return 1
    else:
        # 5 * timer2({5,4,3,2,1}-1) 
        return n * timer2(n-1)

# Constant Complexity (O(c)) --- c can be any constant number
def const_complex(n):
    # n[1] * n[2] = (5 * 6) = 30
    result = n[1] * n[2]
    print(result)

# Linear Complexity (O(n))
def linear(n):
    count = 0
    # print the list the same number of times as the number of 'n' items in the list
    for i in n:
        count+=1
        print(count,")",i,n)

# Quadratic Complexity (O(n^2))
def quadratic(n):
    # first loop iterates through 'n' items
    for i in n:
        # second loop also iterates through 'n' items
        for j in n:
            print(n, " uWu ", n)

# Cubic Complexity (O(n^3))
def cubic(n):
    # first loop iterates through 'n' items
    for i in n:
        # second loop also iterates through 'n' items
        for j in n:
            # third loop also iterateing through 'n' items
            for k in n:
                print(n, " oWo ", n, ' uWu', n)

# tests
print (timer(6)) # expected result : 720
print (timer2(5)) # expected result : 120
const_complex([4,5,6,8]) # constant complexity
linear(['Hello','World','My','Name','Is', 'Aaron'])
quadratic([4,5,6,8])
cubic(['x','y','xx','xy'])