def func(n, digit):
    lis = []
    while n != 0:
        for d in str(n):
            x = int(d)
            lis.append(x)
        n = n - 1
    return lis.count(digit)


n = int(input())
digit = int(input())
print(func(n,digit))
