#PART 0
mode = int(input())
if mode != 1 and mode != 2 and mode != 3:
    print("Invalid mode")
    quit()
#################################################################
#PART 1
height = int(input("h="))
width = int(input("w="))

if height <= 0:
    print("Invalid height of candles")
    quit()
if width <= 0:
    print("Invalid number of candles")
    quit()

for i in range(0,width-1):
    print("[", end='')
print("[ ")

for i in range(0,width):
    print("[]", end="")
    break