from collections import defaultdict
from collections import Counter
import random
import time

k = 8
t = 5
N = 1000
f = open("C:/Users/Jakov/Desktop/BA2G_Input.txt", "r")
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

def profileRandomlyGeneratedkmer(text, dictionary):
    nd = {}
    for i in range(len(text) - k + 1):
        t = text[i : i + k]
        prob = 1
        for j in range(len(t)):
            prob *= dictionary[t[j]][j] #ovdje uzimamo j-to slovo i njegovu vjerojatnost na j-tom mjestu
        nd[t] = prob
    random.seed(time.time())
    Rmotif = random.choices(list(nd.keys()), list(nd.values()))[0]
    return Rmotif

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

def randomMotifs(RowList, k):
    r_motifs = []
    for i in range(len(RowList)):
        r = random.randint(0, len(RowList[0]) - k)
        r_motifs.append(RowList[i][r : r + k])
    return r_motifs

def GibbsSampler(RowList, k, t, N):
    bestmotifs = randomMotifs(RowList, k)
    for i in range(N):
        n = random.randint(0, t - 1)
        Motifs = bestmotifs.copy()
        tmp = Motifs.copy()
        tmp.pop(n)
        prof = formProfile(tmp)
        Motifs[n] = profileRandomlyGeneratedkmer(RowList[n], prof)
        if(score(Motifs) < score(bestmotifs)):
            bestmotifs = Motifs
    return bestmotifs

bestmotifs = GibbsSampler(RowList, k, t, N)
for i in range(20):
    motifs = GibbsSampler(RowList, k, t, N)
    if score(motifs) < score(bestmotifs):
        bestmotifs = motifs

for i in range(len(bestmotifs)):
    print(bestmotifs[i])