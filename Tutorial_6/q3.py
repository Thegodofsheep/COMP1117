mylist = []

def readList():
    num = int(input())
    mylist.append(num)
    while num != 0:
        num = int(input())
        mylist.append(num)
    print(mylist)
    return mylist

def calSum(x):
    x = 0
    global mylist
    for i in mylist:
        x = x + i
    return x

myList = readList() 
sum = calSum(myList) 
print(sum)