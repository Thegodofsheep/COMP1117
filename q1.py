num = int(input())
dig = int(input())
count = 0

if num < 1000 and num > 0:
    if dig <= 10 and dig >= 1:
        for i in range(1, num+1):
#check num between 1 to 99
            if i <= 99:
                check_tens = i//10
                check_ones = i % 10
                if check_tens == dig:
                    count += 1
                if check_ones == dig:
                    count += 1

#check num bigger or eqaul to 100 but less than 1000
            elif i >= 100:
                check_huns = i//100
                check_tens = check_huns % 10
                check_ones = i % 100

                if check_huns == dig:
                    count += 1
                if check_tens == dig:
                    count += 1
                if check_ones == dig:
                    count += 1
    print(count)
else:
    quit()