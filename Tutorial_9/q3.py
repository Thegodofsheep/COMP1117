s = input()
def letter_count(s):
    s = s.replace(" ","")
    d = {}
    for i in s:
        d[i] = s.count(i)
    return d
print(letter_count(s))