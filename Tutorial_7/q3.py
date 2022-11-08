def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

n1 = int(input())
n2 = int(input())

s = list(range(n1, n2+1))

print(list(filter(is_even,s)))
