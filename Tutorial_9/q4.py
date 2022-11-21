def check(s):
    sum = 0
    s = s.replace(" ", "")
    last = int(s[-1])
    s = s[:-1]
    s = list(int(d) for d in str(int(s[-1::-1])))
    for i in range(0, len(s), 2):
            s[i] *= 2
            if s[i] >= 10:
                s[i] = s[i]//10 + s[i]%10 
    for i in range(0, len(s)):
        sum += s[i]
    
    cal_dig = 10 - sum%10

    if cal_dig == last:
        return True
    else: 
        return False


if check(input()) == True:
    print("Valid")
else:
    print("Invalid")