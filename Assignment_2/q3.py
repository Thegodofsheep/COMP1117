#PART 0
from os import WIFCONTINUED


mode = int(input())
if mode != 1 and mode != 2 and mode != 3:
    print("Invalid mode")
    quit()
#################################################################
#PART 1
def mode1(x, y):
    if x <= 0:
        print("Invalid height of candles")
        quit()
    if y <= 0:
        print("Invalid number of candles")
        quit()
        
    for i in range(0,y-1):
        print("[ ", end='')
    print("[ ")

    for i in range (0,x):
        for i in range(0,y-1):
            print("[]", end="")
        print("[]")

if mode == 1:
    height = int(input())
    candles = int(input())
    m1 = mode1(height, candles)
    print(m1)
#################################################################
#PART 2
def mode2(a,b,c,d):
    if a < 3:
        print("Invalid width of the cake")
        quit()
    if b < 3:
        print("Invalid height of the cake")
        quit()

    for i in range(0,a-1):
        print(c, end="")
    print(c)

    for i in range(0,b-2):
        print(c,end="")
        for i in range(0,a-2):
            print(d,end="")
        print(c)

    for i in range(0,a-1):
        print(c, end="")
    print(c)
    
if mode == 2:
    width = int(input())
    height_2 = int(input())
    char = input()
    fill = input()
    m2 = mode2(width,height_2,char,fill)
    print(m2)

#################################################################
#PART 3
def mode3(a,b,c,d,e,f):
    if a < 0:
        print("Invalid height of candles")
        quit()
    if b % 2 != 0 or b < 4:
        print("Invalid width of the cake")
        quit()
    if c < 3:
        print("Invalid height of the cake")
        quit()  
    if f <= 0:
        print("Invalid number of candles")
        quit()

    for i in range(0,f-1):
        print(" [", end='')
    print(" [  ")

    for i in range (0,a):
        print(" ",end="")
        for i in range(0,f-1):
            print("[]", end="")
        print("[] ")

    for i in range(0,b-1):
        print(d, end="")
    print(d)

    for i in range(0,c-2):
        print(d,end="")
        for i in range(0,b-2):
            print(e,end="")
        print(d)

    for i in range(0,b-1):
        print(d, end="")
    print(d)

if mode == 3:
    height_3 = int(input())
    width_3 = int(input())
    height_cake_3 = int(input())
    char_3 = input()
    fill_3 = input()
    candles_3 = int((width_3-2)/2)
    m3 = mode3(height_3,width_3,height_cake_3, char_3, fill_3, candles_3)
    print(m3) 