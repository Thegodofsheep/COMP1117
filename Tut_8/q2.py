def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        return a + multiply(a,b-1)
    else:
        return b + multiply(a-1,b)



a = int(input())
b = int(input())
print(multiply(a, b))
