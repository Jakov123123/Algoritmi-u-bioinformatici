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

def linearSpectrum(peptide):
    aminoMassT = aminoMassTable()
    prefixMass = {
        0: 0
    }
    for i in range(len(peptide)):
        for j in range(20):
            if(list(aminoMassT.keys())[j] == peptide[i]):
                prefixMass[i + 1] = prefixMass[i] + aminoMassT[peptide[i]]
    
    linearSpc = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linearSpc.append(prefixMass[j] - prefixMass[i])
    return sorted(linearSpc)

f = open("C:/Users/Jakov/Desktop/BA4J_Input.txt", "r")
peptide = f.read()

ls = linearSpectrum(peptide)
pr = ""
for i in ls:
    pr += str(i) + " "

fp = open("C:/Users/Jakov/Desktop/BA4J_res.txt", 'w')
fp.write(pr)
fp.close()