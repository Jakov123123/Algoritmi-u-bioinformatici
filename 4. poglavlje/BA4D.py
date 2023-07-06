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

def getAllCombinations(mass, allmasses, counter):
    if(mass in counter):
        return counter[mass]
    if(mass < 0):
        return 0
    if(mass == 0):
        return 1

    counter[mass] = 0
    for aMass in allmasses:
        counter[mass] += getAllCombinations(mass - aMass, allmasses, counter)
    return counter[mass]

mass = 1024
allmasses = set(aminoMassTable().values())
counter = {}
res = getAllCombinations(mass, allmasses, counter)
print(res)