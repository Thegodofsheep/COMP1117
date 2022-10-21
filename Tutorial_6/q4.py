myset = set()

def readSet():
    num = int(input())
    myset.add(num)
    while num != 0:
        num = int(input())
        myset.add(num)
    return myset

def findNo(x,y):
    return y in x

mySet = readSet()
number = int(input('Find number? ')) 
print(findNo(mySet, number))

