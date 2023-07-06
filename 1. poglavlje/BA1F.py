text = input()

def SkewList(text):
    l = [0]
    br = 0
    for i in range(len(text)):
        if(text[i] == "G"):
            br += 1
        elif(text[i] == "C"):
            br -= 1
        l.append(br)
    return l

l = SkewList(text)
m = min(SkewList(text))
for i in range(len(l)):
    if(l[i] == m):
        print(i, end = " ")
        
    
