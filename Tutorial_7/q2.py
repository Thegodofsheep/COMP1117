def cal_square(n):
    return n**2

lower = int(input())
upper = int(input())

s = list(range(lower, upper+1))

print(list(map(cal_square,s)))
