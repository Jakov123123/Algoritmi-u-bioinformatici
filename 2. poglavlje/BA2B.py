k = 6
f = open("C:/Users/Jakov/Desktop/BA2B_Input.txt", "r")
RowList = f.read().splitlines()
            
def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if(p[i] != q[i]):
            dist += 1
    return dist

def minHamm(text, pattern):
    min = len(pattern)
    for i in range(0, len(text) - k + 1):
        hdist = HammingDistance(pattern, text[i : i + k])
        if(hdist < min):
            min = hdist
    return min

def allMutations(k, letters, current_combination, d): #dakle kao argumente uzimamo duljinu, listu slova, trenutnu kombinaciju koju gradimo i rječnik
    if len(current_combination) == k:
        d[current_combination] = 0
    else:
        for letter in letters:
            allMutations(k, letters, current_combination + letter, d)

d = {}
allMutations(k, ["A", "C", "G", "T"], "", d)

def medianString(d, RowList):
    for row in RowList:
        for pattern in d.keys():
            d[pattern] += minHamm(row, pattern)

medianString(d, RowList)
minL = 5*k
for p in d.keys():
    if(d[p] < minL):
        min = p
        minL = d[p]

print(min)