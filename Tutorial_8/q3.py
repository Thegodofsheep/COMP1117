def func(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    else:
        return func(n-3)*func(n-2)
         
n = int(input())

print(func(n))