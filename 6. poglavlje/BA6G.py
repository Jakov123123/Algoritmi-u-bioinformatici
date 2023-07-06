def cycleToChromosome(cycle):
    cycle = cycle[1:-1].split(" ")
    cycle = [int(x) for x in cycle]
    chr = [i for i in range(1, int(len(cycle)/2) +1)]
    for j in range(0, int(len(cycle)/2)):
        if(cycle[2*j] > cycle[2*j + 1]):
            chr[j] = -chr[j]
    return chr

cycInput = "(1 2 4 3 6 5 7 8 10 9 12 11 14 13 16 15 18 17 19 20 22 21 23 24 25 26 27 28 30 29 32 31 33 34 36 35 37 38 39 40 41 42 43 44 45 46 47 48 50 49 52 51 53 54 56 55 58 57 60 59 61 62 63 64 65 66 68 67 70 69 71 72 74 73 76 75 78 77 80 79 82 81 83 84 86 85 87 88 89 90 92 91 93 94 96 95 98 97 100 99 101 102 104 103 105 106 108 107 110 109 112 111 113 114 116 115 117 118 120 119 122 121 123 124)"

print("(", end="")
for i in cycleToChromosome(cycInput):
    if(i > 0):
        print("+", end="")
    if i == cycleToChromosome(cycInput)[-1]:
        print(i, end="")
    else:
        print(i, end=" ")
print(")")
