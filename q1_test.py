n = int(input())
dig = int(input())
count = 0

if n < 1000 and n > 0:
    if dig <= 10 and dig >= 1:
        for i in range(1, n + 1):
            num = list(str(i))
            if  i < 10:
                if num[0] == str(dig):
                    count += 1
            elif i < 100:
                if num[0] == str(dig):
                    count += 1
                if num[1] == str(dig):
                    count += 1
            elif i <= 1000:
                if num[0] == str(dig):
                    count += 1
                if num[1] == str(dig):
                    count += 1
                if num[2] == str(dig):
                    count += 1
else:
    quit()
print(count)