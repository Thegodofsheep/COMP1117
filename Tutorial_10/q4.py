def convert_base(n,b):
    if n<= 1:
        return str(n)
    elif n == 0:
        return
    else:
        return str(convert_base(n//b,b)) + str(n%b)

def base_10_16(n,b, digits = "0123456789ABCDEF"):
    if n >= b:
        return base_10_16(n//b, b) + digits[n%b]
    else:
        return digits[n]


n = int(input())
b = int(input())

if b == 10:
    print(n)
elif b > 10:
    print(base_10_16(n,b))
elif b == 2:
    print(convert_base(n,b))
else:
    s = convert_base(n,b)
    if s[0] == "0":
        print(s[1:])

    

