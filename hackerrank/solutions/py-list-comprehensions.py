if __name__ == '__main__':
    x = int (input())
    y = int (input())
    z = int (input())
    n = int (input())
    
    print([ [ i, j,k] for i in range( x + 1) for j in range( y + 1) 
                    for k in range( z+ 1) if( ( i + j + k ) != n )])


from itertools import combinations

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # list comprehension
    xyz = [[a,b,c] for b in range(y+1) for c in range(z+1) 
                   for a in range(x+1) if ((a+b+c)!=n)]

    emptyList = [] # empty list , values will be appended to this list
    
    # loop through xyz appending values to each list comprehension
    for i in combinations(xyz,3):
        for j in i:
            x = sum(j)
            # if value still equals 1 and not in list append
            if x!=n and j not in emptyList:
                emptyList.append(j)
            # in this case N=2 , so if value equals 2 and not in list append
            elif x==n and j in emptyList:
                print("terminated")
            elif n==0:
                print("XYZ")
    # end nested for 


    newList= (sorted(emptyList, key=str))# str as sorting key
    print(newList)