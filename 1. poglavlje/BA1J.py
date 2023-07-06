k = 6
d = 2
text = "CCACGAATTTATACTGTTATACTGCTGAGTGTGTTATACTGCTGAGTGTGCCGCTATGCTGAGTGTGTGTGTGTGCCCTGAGTGTGTGTGTGTGCCCCACGAATTGTGTGTGCCCTGAGTGTGCTGAGTGTGCTGAGTGTGCTGAGTGTGCTGAGTGTGTTATACTGTTATACTGCCACGAATCTGAGTGTGTTATACTGCCACGAATCCACGAATTGTGTGTGCCCTGAGTGTGCTGAGTGTGTGTGTGTGCCCCACGAATTTATACTGTTATACTGCCGCTATGCTGAGTGTGCTGAGTGTGCCGCTATGCCGCTATGCTGAGTGTGCCGCTATGTGTGTGTGCCTGTGTGTGCCCTGAGTGTGCTGAGTGTGTTATACTGCCGCTATGTGTGTGTGCCCTGAGTGTGTTATACTGTTATACTGCCGCTATGCCGCTATGTGTGTGTGCCTGTGTGTGCCCTGAGTGTGCCACGAATCTGAGTGTGCCACGAATCTGAGTGTGCTGAGTGTGCCGCTATGTGTGTGTGCCCCACGAATCCGCTATGCCACGAATTGTGTGTGCCTTATACTGCCACGAATCTGAGTGTGCTGAGTGTGCCGCTATGCCACGAATTTATACTGCCACGAATCCGCTATGCTGAGTGTGCTGAGTGTGTGTGTGTGCCCCACGAATTGTGTGTGCCCTGAGTGTGTGTGTGTGCCCCACGAATCCGCTATGCTGAGTGTGTGTGTGTGCCTGTGTGTGCCCTGAGTGTGCCGCTATGTGTGTGTGCCCTGAGTGTGTTATACTGCCGCTATGTTATACTGCCGCTATGTTATACTGTTATACTGCCGCTATGCCGCTATGCCACGAATTTATACTGTTATACTGCTGAGTGTGCCGCTATGCCGCTATGTGTGTGTGCCCCACGAATTGTGTGTGCCCCACGAATTGTGTGTGCCCCACGAAT"
def Reverse(text):
    Ctext = ""
    for i in range(len(text)):
        if text[i] == "A":
            Ctext += "T"
        elif text[i] == "T":
            Ctext += "A"
        elif text[i] == "C":
            Ctext += "G"
        elif text[i] == "G":
            Ctext += "C"
    RCtext = ""
    for i in range(len(text)-1,-1,-1):
        RCtext += Ctext[i]
    return RCtext

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

for i in range(len(text) - k + 1):
    mp = []
    for j in all_d_subsets(ListOfNatNumbersTillN(k), d):
        for p in add_letters([], list(text[i : i + k]), j):
            if(p not in mp):
                mp.append(p)
    for n in listToStr(mp):
        if n not in dic.keys():
            dic[n] = 1
            dic[Reverse(n)] = 1
        else:
            dic[n] += 1
            dic[Reverse(n)] += 1

MM = max(dic.values())

for m in dic.keys():
    M = [key for key, value in dic.items() if value == MM] #skraceno dobivanje kljuca maks vrijednosti

for i in range(len(M)):
    print(M[i], end = " ")
    


