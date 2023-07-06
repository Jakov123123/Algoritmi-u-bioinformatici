synteny = "(-117 -10 -121 +74 -114 -40 -14 +23 -103 +112 +72 -111 +127 -133 -56 +17 -25 -94 -9 -108 +97 -130 +60 +19 -119 -49 +36 -64 +62 +86 +140 -131 -67 +124 +101 +122 +115 +102 -59 +134 +95 -33 -99 -66 -39 -84 -22 +18 +96 +26 -30 +12 -73 +58 +38 -136 +21 -24 -123 +98 -92 +118 +82 +55 -81 +7 -126 -110 +89 +78 -107 -65 +3 -53 -83 +80 +6 +113 -31 +71 +35 -50 -13 -76 +57 +42 +47 +15 +138 +1 +34 +37 +87 -139 -8 -20 -137 +16 +93 +44 +129 -85 +91 +4 -61 -32 -11 -109 -100 -27 +104 +5 -116 -125 -45 -77 -128 -88 +48 +79 -46 +54 -75 +69 +2 -43 +29 +63 -51 -70 -132 +90 +120 -135 +68 -28 -52 -105 +41 -106)"
f = open("C:/Users/Jakov/Desktop/BA6A_res.txt", "w")

def SyntenyToList(s):
    l = []
    j = 1
    for i in range(0, len(s)):
        if(s[i] == " " or s[i] == ")"):
            l.append(int(s[j:i]))
            j = i + 1
    return l

def PrintSynteny(l):
    a = "("
    for i in range(len(l) - 1):
        if(l[i] > 0):
            a += "+" + str(l[i]) + " "
        else:
            a += str(l[i]) + " "
    if(l[len(l) - 1] > 0):
        a += "+" + str(l[len(l) - 1])
    else:
        a += str(l[len(l) - 1])
    a += ")\n"
    f.write(a)

def DefaultSynteny(k):
    l = []
    for i in range(k):
        l.append(i + 1)
    return l

d = DefaultSynteny(len(synteny))

def Reversals(lsynteny, num):
    i = num - 1
    newl = []
    newl1 = []
    for k in range(num - 1):
        newl.append(k + 1)
    while(lsynteny[i] != num and -lsynteny[i] != num):
        newl1.append(-lsynteny[i])
        i += 1
    newl1.append(-lsynteny[i])
    newl1.reverse()
    newl = newl + newl1
    for j in range(i + 1, len(lsynteny)):
        newl.append(lsynteny[j])
    PrintSynteny(newl)
    if(newl[num - 1] < 0):
        newl[num - 1] = -newl[num - 1]
        PrintSynteny(newl)
    if(num < len(newl) and newl != d):
        Reversals(newl, num + 1)

Reversals(SyntenyToList(synteny), 1)
f.close()