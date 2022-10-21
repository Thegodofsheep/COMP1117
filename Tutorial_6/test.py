mylist = []
num = int(input())
mylist.append(num)
while num != 0:
    num = int(input())
    mylist.append(num)
print(mylist)

for i in mylist:
    print(i)


mySet = readSet()
number = int(input('Find number? ')) 
print(findNo(mySet, number))
