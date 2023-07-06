from collections import defaultdict
from collections import Counter
import random
import time

k = 8
t = 5
f = open("C:/Users/Jakov/Desktop/BA2F_Input.txt", "r")
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

    M = max(nd.values())
    for m in nd.keys():
        lmax = [key for key, value in nd.items() if value == M]
    
    random.seed(i + time.time())
    r = random.randint(0, len(lmax) - 1)
    return lmax[r]

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

def randomMotifs(RowList):
    r_motifs = []
    for i in range(len(RowList)):
        random.seed(i + time.time())
        r = random.randint(0, len(RowList[0]) - k)
        r_motifs.append(RowList[i][r : r + k])
    return r_motifs

BestMotifs = randomMotifs(RowList)

for i in range(1000):
    Motifs = randomMotifs(RowList)

    while(True):
        profile = formProfile(Motifs)
        Motifs = []
        for j in range(len(RowList)):
            Motif = profileMostProbablekmer(RowList[j], profile)
            Motifs.append(Motif)
        if(score(Motifs) < score(BestMotifs)):
            BestMotifs = Motifs
        else:
            break

for i in range(len(BestMotifs)):
    print(BestMotifs[i])