i = 1
string = input()
split = string.split(",")
max = int(split[0])

while i < len(split):
    if int(split[i]) > max:
        max = int(split[i])
        print(max)
        i += 1
    else:
        i += 1

print(max)
