num = int(input())
dig = int(input())
count = 0

if num < 1000 and num > 0:
    if dig <= 10 and dig >= 1:
        for i in range(1,num+1):
            check_1 = i//10
            check_2 = i%10
            if check_1 == dig:
                count += 1
            if check_2 == dig:
                count += 1
else:
    quit()
print(count)


