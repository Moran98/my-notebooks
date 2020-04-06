if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    newArr = list(set(list(arr))) # make new array and sort it high to low , pos to neg
    ar = len(newArr) # length of newArr assigned to ar
    newArr = sorted(newArr) # sort newArr from neg to pos
    print(newArr[ar-2])# largest = -1, Runner-up = -2
