k = 4
d = 1
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"

def alldSubsets(l, d):
    if d == 1:
        return [[x] for x in l]
    res = []
    for i in range(len(l)):
        selected = l.copy()[i+1:]
        smaller_subsets = alldSubsets(selected, d - 1)
        for subset in smaller_subsets:
            subset.append(l[i])
        res.extend(smaller_subsets.copy())
    return res

def addLetters(indices, mutpattern, origpattern, letters): #ova funkcija za dane indekse napravi sve permutacije nad njima
    def mutate(letter, i):
        opattern = origpattern.copy()
        opattern[i] = letter
        if(opattern not in mutpattern):
            mutpattern.append(opattern)
        ind = indices.copy()
        ind.pop(ind.index(i))
        addLetters(ind, mutpattern, opattern, letters)
    for i in indices:
        for l in letters:
            mutate(l, i)
    return mutpattern

def listToStr(l):
    l2 = []
    for l1 in l:
        st = ""
        for element in l1:
            st += element
        l2.append(st)
    return l2

def listOfNatNumbersTillN(N):
    l = []
    for i in range(N):
        l.append(i)
    return l

dic = {}

for i in range(len(text) - k + 1):
    mp = []
    for j in alldSubsets(listOfNatNumbersTillN(k), d):
        for p in addLetters(j, [], list(text[i : i + k]), ["A", "C", "G", "T"]):
            if(p not in mp):
                mp.append(p)
    for n in listToStr(mp):
        if n not in dic.keys():
            dic[n] = 1
        else:
            dic[n] += 1

mx = max(dic.values())

for m in dic.keys():
    M = [key for key, value in dic.items() if value == mx] #skraceno dobivanje kljuca maks vrijednosti

for i in range(len(M)):
    print(M[i], end = " ")