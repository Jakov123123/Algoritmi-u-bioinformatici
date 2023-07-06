def chromosomeToCycle(chromosome):
    chromosome = chromosome[1:-1].split(" ")
    chromosome = [int(x) for x in chromosome]
    nodes = [i for i in range(1, 2*len(chromosome)+1)]
    for j in range(0, len(chromosome)):
        i = chromosome[j]
        if(i < 0):
            temp = nodes[2*j]
            nodes[2*j] = nodes[2*j + 1]
            nodes[2*j + 1] = temp
    return nodes

chrInput = "(-1 +2 -3 -4 -5 -6 +7 -8 -9 +10 -11 +12 +13 +14 +15 -16 +17 +18 -19 -20 +21 +22 +23 -24 -25 -26 +27 +28 +29 +30 -31 +32 +33 +34 +35 +36 +37 -38 +39 +40 -41 -42 -43 +44 +45 +46 -47 +48 +49 +50 +51 +52 +53 -54 -55 -56 -57 +58 -59 +60 -61 +62 +63 +64 +65 +66)"

print("(", end="")
for i in chromosomeToCycle(chrInput):
    if i == chromosomeToCycle(chrInput)[-1]:
        print(i, end="")
    else:
        print(i, end=" ")
print(")")