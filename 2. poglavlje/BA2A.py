k = 3
d = 1
f = open("C:/Users/Jakov/Desktop/BA2A_Input.txt", "r")
patterns = f.read().splitlines()

def allSubsets(l, d):#l je lista indekasa
    if d == 1:
        return [ [x] for x in l ]
    else:
        res = []
        for i in range(len(l)):
            selected = l.copy()[i+1:] #kopiramo jer je referentni tip; drugi dio piše zbog ponavljanja
            smaller_subsets = allSubsets(selected, d-1)
            for subset in smaller_subsets:
                subset.append(l[i]) #nalipimo onaj koji smo fiksirali
            res.extend(smaller_subsets.copy()) #dodavanje na listu
    return res

def addLetters(mutpattern, origpattern, indices): #ova funkcija za dane indekse napravi sve permutacije nad njima
    def mutate(letter, i):
        opattern = origpattern.copy()
        opattern[i] = letter
        if(opattern not in mutpattern):
            mutpattern.append(opattern)
        ind = indices.copy()
        ind.pop(ind.index(i))
        addLetters(mutpattern, opattern, ind)
    for i in indices:
        mutate("A", i)
        mutate("G", i)
        mutate("T", i)
        mutate("C", i)
    return mutpattern

def listToStr(l):
    l2 = []
    for l1 in l:
        st = ""
        for element in l1:
            st += element
        l2.append(st)
    return l2

def ListOfNatNumbersTillN(N):
    l = []
    for i in range(N):
        l.append(i)
    return l

dic = {}

def countRows(RowList):
    for i in range(len(RowList)):
        for j in range(len(RowList[i]) - k + 1):
            mp = []
            for q in allSubsets(ListOfNatNumbersTillN(k), d):
                for p in addLetters([], list(RowList[i][j : j + k]), q):
                    if(p not in mp):
                        mp.append(p)
            for n in listToStr(mp):
                if(i == 0):
                    dic[n] = 1
                if(n in dic.keys() and dic[n] == i):
                    dic[n] = i + 1

countRows(patterns)

M = max(dic.values())

for m in dic.keys():
  max_keys = [key for key, value in dic.items() if value == M] #skraceno dobivanje kljuca maks vrijednosti
#obavezno ovaj M izračunaj prije kao šta je ovako, inače u svakoj iteraciji
#računa maksimum i traje jako dugo.

for i in range(len(max_keys)):
   print(max_keys[i], end = " ")