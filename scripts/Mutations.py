def mutate(string, position, character):
    # assign the input string to 'l'
    l = list(string)
    # take the position passed and search for it in 'l'
    l[position] = character
    # use join to convert to string
    string = ''.join(l)
    # return the string
    return string

    # string = string[:position] + character + string[6:]
    # return string

def mutate2(string, position, character):
    string = string[:position] + character + string[6:]
    return string

if __name__ == '__main__':
    s = input("Enter a word to mutate : ")
    print("Enter a NUMBER seperated with the CHAR to replace with : ")
    i, c = input().split()
    x = mutate(s, int(i), c)
    print("First mutate method : ",x)
    y = mutate2(s, int(i), c)
    print("Second mutate method : ",y)