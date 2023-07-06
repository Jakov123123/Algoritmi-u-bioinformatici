pattern = input()

def PatternToNumber(pattern):
    res = 0
    k = len(pattern) - 1
    for i in list(pattern):
        if(i == "C"):
            res += 4**k
        elif(i == "G"):
            res += 2*(4**k)
        elif(i == "T"):
            res += 3*(4**k)
        k -= 1
    return res

print(PatternToNumber(pattern))
