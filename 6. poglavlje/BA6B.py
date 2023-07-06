f = open("C:/Users/Jakov/Desktop/BA6B_Input.txt", "r")

def SyntenyToList(s):
    l = []
    j = 1
    for i in range(0, len(s)):
        if(s[i] == " " or s[i] == ")"):
            l.append(int(s[j:i]))
            j = i + 1
    return l

def Breakpoints(lsynteny):
    if(lsynteny[0] != 1):
        b = 1
    else:
        b = 0
    for i in range(len(lsynteny) - 1):
        if(lsynteny[i] + 1 != lsynteny[i + 1]):
            b += 1
    return b

print(Breakpoints(SyntenyToList(f.read())))