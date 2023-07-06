def cycleToChromosome(cycle):
    M = max(cycle)
    m = min(cycle)
    chr = [i for i in range(int((m+1)/2), int(M/2) + 1)]
    for j in range(0, int(len(cycle)/2)):
        if(cycle[2*j] > cycle[2*j + 1]):
            chr[j] = -chr[j]
    return chr

st1 = "(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
st1 = st1.replace("(", "").replace(")", "").split(", ")
# Convert the pairs into a list of numbers
st1 = [int(num) for pair in st1 for num in pair.split(",")]
j = 0
lstBr = []
for i in range(len(st1) - 1):
    if(i % 2 == 0 and st1[i] > st1[i + 1]):
        st1.insert(j, st1[i + 1])
        st1.pop(i + 2)
        lstBr.append(j)
        j = i + 2
lstBr.append(len(st1))
lstl = []
for i in range(len(lstBr) - 1):
    lstl.append(st1[lstBr[i]:lstBr[i + 1]])

for i in lstl:
    print("(", end="")
    for j in cycleToChromosome(i):
        if(j > 0):
            print("+", end="")
        if j == cycleToChromosome(i)[-1]:
            print(j, end="")
        else:
            print(j, end=" ")
    print(")", end="")