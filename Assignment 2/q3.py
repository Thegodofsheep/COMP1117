#PART 0
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
if mode == 2:
    width_2 = int(input())
    height_cake_2 = int(input())
    char_2 = input()
    fill_2 = input()

    if width_2 < 3:
        print("Invalid width of the cake")
        quit()
    if height_cake_2 < 3:
        print("Invalid height of the cake")
        quit()

    for i in range(0,width_2-1):
        print(char_2, end="")
    print(char_2)

    for i in range(0,height_cake_2-2):
        print(char_2,end="")
        for i in range(0,width_2-2):
            print(fill_2,end="")
        print(char_2)

    for i in range(0,width_2-1):
        print(char_2, end="")
    print(char_2)
#################################################################
#PART 3
if mode == 3:
    height_3 = int(input())
    width_3 = int(input())
    height_cake_3 = int(input())
    char_3 = input()
    fill_3 = input()
    candles_3 = int((width_3-2)/2)

    if height_3 < 0:
        print("Invalid height of candles")
        quit()
    if width_3 % 2 != 0 or width_3 < 4:
        print("Invalid width of the cake")
        quit()
    if height_cake_3 < 3:
        print("Invalid height of the cake")
        quit()  
    if candles_3 <= 0:
        print("Invalid number of candles")
        quit()

    for i in range(0,candles_3-1):
        print(" [", end='')
    print(" [  ")

    for i in range (0,height_3):
        print(" ",end="")
        for i in range(0,candles_3-1):
            print("[]", end="")
        print("[] ")

    for i in range(0,width_3-1):
        print(char_3, end="")
    print(char_3)

    for i in range(0,height_cake_3-2):
        print(char_3,end="")
        for i in range(0,width_3-2):
            print(fill_3,end="")
        print(char_3)

    for i in range(0,width_3-1):
        print(char_3, end="")
    print(char_3)