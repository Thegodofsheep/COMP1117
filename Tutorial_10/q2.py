def comb(n,r):
    if n == r:
        return 1
    elif r == 0:
        return 1
    elif r > n:
        return 0
    else:
        return comb(n-1,r) + comb(n-1,r-1)
    
n = int(input())
r = int(input())

print(comb(n,r))