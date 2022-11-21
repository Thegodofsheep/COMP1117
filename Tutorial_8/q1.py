def product(n):
    if n == 2:
        return 2
    elif n%2 == 0:
        return n * product(n-2)
    else:
        return product(n-1)


print(product(int(input())))