pattern = "AGGGCG"
f = open("C:/Users/Jakov/Desktop/BA2H_Input.txt", "r")
RowList = f.read().split()
            
def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if(p[i] != q[i]):
            dist += 1
    return dist

def minHamm(text, pattern):
    min = len(pattern)
    for i in range(0, len(text) - len(pattern) + 1):
        hdist = HammingDistance(pattern, text[i : i + len(pattern)])
        if(hdist < min):
            min = hdist
    return min

distance = 0
for row in RowList:
    distance += minHamm(row, pattern)

print(distance)