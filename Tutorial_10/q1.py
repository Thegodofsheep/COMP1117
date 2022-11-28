def facto(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return a*facto(a-1)
    

print(facto(int(input())))