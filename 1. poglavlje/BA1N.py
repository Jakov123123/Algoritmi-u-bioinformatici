pattern = input()
d = int(input())

def ListOfNatNumbersTillN(N):
    l = []
    for i in range(N):
        l.append(i)
    return l

def all_d_subsets(l, d):#l je lista indekasa
    if d == 1:
        return [ [x] for x in l ]
    else:
        res = []
        for i in range(len(l)):
            selected = l.copy()[i+1:] #kopiramo jer je referentni tip; drugi dio piše zbog ponavljanja
            smaller_subsets = all_d_subsets(selected, d-1)
            for subset in smaller_subsets:
                subset.append(l[i]) #nalipimo onaj koji smo fiksirali
            res.extend(smaller_subsets.copy()) #dodavanje na listu
    return res

def add_letters(mutpattern, origpattern, indices): #ova funkcija za dane indekse napravi sve permutacije nad njima
    def mutate(letter, i):
        opattern = origpattern.copy()
        opattern[i] = letter
        if(opattern not in mutpattern):
            mutpattern.append(opattern)
        ind = indices.copy()
        ind.pop(ind.index(i))
        add_letters(mutpattern, opattern, ind)
    for i in indices:
        mutate("A", i)
        mutate("C", i)
        mutate("G", i)
        mutate("T", i)
    return mutpattern

def ListToStr(l):
    s = ""
    for letter in l:
        s += letter
    return s

for q in all_d_subsets(ListOfNatNumbersTillN(len(pattern)), d):
    for p in add_letters([], list(pattern), q):
        print(ListToStr(p))
