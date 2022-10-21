num = int(input())
line = 1
linechar = ("0", "1")

def line1():
    global line 
    posnum1 = 1
    for i in range(0,line):
        if posnum1 == 1:
            posnum1 -= 1
        else:
            posnum1 += 1
        print(linechar[posnum1],end= " ")
    line += 1
    return

def line2():
    global line
    posnum2 = 0
    for i in range(0,line):
        if posnum2 == 0:
            posnum2 += 1
        else:
            posnum2 -= 1
        print(linechar[posnum2],end= " ")
    line += 1
    return

for i in range(0,(num//2+ num%2)):
    line1()
    print()
    if line > num:
        quit()
    else:
        line2()
        print()