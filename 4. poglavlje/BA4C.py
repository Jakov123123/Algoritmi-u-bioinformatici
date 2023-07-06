def aminoMassTable():
    aminoMass = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186
    }
    return aminoMass

def cyclicSpectrum(peptide):
    aminoMassT = aminoMassTable()
    prefixMass = {
        0: 0
    }
    for i in range(len(peptide)):
        for j in range(20):
            if(list(aminoMassT.keys())[j] == peptide[i]):
                prefixMass[i + 1] = prefixMass[i] + aminoMassT[peptide[i]]
    
    peptideMass = prefixMass[len(peptide)]
    cyclicSpc = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclicSpc.append(prefixMass[j] - prefixMass[i])
            if(i > 0 and j < len(peptide)):
                cyclicSpc.append(peptideMass - (prefixMass[j] - prefixMass[i]))
    return sorted(cyclicSpc)

f = open("C:/Users/Jakov/Desktop/BA4C_Input.txt", "r")
peptide = f.read()

ls = cyclicSpectrum(peptide)
pr = ""
for i in ls:
    pr += str(i) + " "

fp = open("C:/Users/Jakov/Desktop/BA4C_res.txt", 'w')
fp.write(pr)
fp.close()