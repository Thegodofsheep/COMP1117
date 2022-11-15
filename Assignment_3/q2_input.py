x = list(input())
x = filter(None, x)
x = filter(bool, x)
x = filter(len, x)
x = filter(lambda item: item, x)
x = list(filter(None, x))

print(x)