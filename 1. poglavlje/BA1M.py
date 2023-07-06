index = int(input())
k = int(input())

def Reverse(text):
    Rtext = ""
    for i in range(len(text)-1,-1,-1):
        Rtext += text[i]
    return Rtext

def NumberToPattern(index, k):
    pat = ""
    while(index > 0):
        rem = index%4
        if(rem == 0):
            pat += "A"
        elif(rem == 1):
            pat += "C"
        elif(rem == 2):
            pat += "G"
        elif(rem == 3):
            pat += "T"
        index = index//4
    if(len(pat) == k):
        return pat
    else:
        for i in range(k - len(pat)):
            pat += "A"
        return pat
        

print(Reverse(NumberToPattern(index, k)))
