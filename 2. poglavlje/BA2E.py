from collections import defaultdict
from collections import Counter

k = 12
t = 25
f = open("C:/Users/Jakov/Desktop/BA2E_Input.txt", "r")
RowList = f.read().splitlines()

def formProfile(pattern_matrix):
    Letters = ["A", "C", "G", "T"]
    d = defaultdict(lambda: [])
    for l in Letters:
        for j in range(len(pattern_matrix[0])):
            d[l].append(1/(len(pattern_matrix)+4))
    for i in range(len(pattern_matrix)):
        for j in range(len(pattern_matrix[0])):
            d[pattern_matrix[i][j]][j] += 1/(len(pattern_matrix)+4)
    return d

def profileMostProbablekmer(text, dictionary):
    nd = {}
    for i in range(len(text) - k + 1):
        t = text[i : i + k]
        prob = 1
        for j in range(len(t)):
            prob *= dictionary[t[j]][j] #ovdje uzimamo j-to slovo i njegovu vjerojatnost na j-tom mjestu
        nd[t] = prob

    maxV = nd[list(nd.keys())[0]]
    max = list(nd.keys())[0]
    for p in nd.keys():
        if(nd[p] > maxV):
            max = p
            maxV = nd[p]
    return max

def score(motifs):
    sc = 0
    for j in range(len(motifs[0])):
        letter_list = []
        for i in range(len(motifs)):
            letter_list.append(motifs[i][j])
        string_counts = Counter(letter_list)
        max_string = max(string_counts, key=string_counts.get)
        for l in letter_list:
            if l != max_string:
                sc += 1
    return sc

BestMotifs = []

for row in RowList:
    BestMotifs.append(row[:k])

first_row = RowList[0]

for i in range(len(first_row) - k + 1):
    dic = {}
    dic["motif1"] = first_row[i : i + k]
    for j in range(2, t + 1):
        motifs = []
        for m in range(1, j):
            motifs.append(dic["motif" + str(m)])
        pro = formProfile(motifs)
        dic["motif" + str(j)] = profileMostProbablekmer(RowList[j - 1], pro)
    Motifs = []
    for motif in list(dic.keys()):
        Motifs.append(dic[motif])
    if(score(Motifs) < score(BestMotifs)):
        BestMotifs = Motifs

for i in range(len(BestMotifs)):
    print(BestMotifs[i])