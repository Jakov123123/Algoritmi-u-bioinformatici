text = "TTTGGATACTTATCGGCACTGTTTGCGGAAAATGGCTGTTGCAGGTGAGCTAACTATGGATTTGCGTCTTGATGTCAAATGCTTCACATTCTGAGGCATCCTTGCAGATGAGGCGCAACAAGACTACGCAGTTACGCGAACGCTTCTCATGTGTCAGTATGTTGCTGGGACACGTAGACGTGTTCGCGCCCCACAACCTT"
k = 6
f = open("C:/Users/Jakov/Desktop/BA2C_Input.txt", "r")
RowList = f.read().splitlines()

d = {}
Letters = ["A", "C", "G", "T"]

for i in range(len(RowList)):
    lst = [float(x) for x in RowList[i].split()]
    letter = Letters[i]
    d[letter] = lst

nd = {}

#stavljamo vjerojatnosti u dictionary gdje su slova ključevi, a vjerojatnosti za svaku poziciju liste

for i in range(len(text) - k + 1):
    t = text[i : i + k]
    prob = 1
    for j in range(len(t)):
        prob *= d[t[j]][j] #ovdje uzimamo j-to slovo i njegovu vjerojatnost na j-tom mjestu
    nd[t] = prob

maxV = 0
for p in nd.keys():
    if(nd[p] > maxV):
        max = p
        maxV = nd[p]

print(max)