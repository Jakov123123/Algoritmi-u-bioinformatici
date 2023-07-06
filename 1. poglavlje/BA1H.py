DNA = input()
Text = input()
HammingMax = int(input())

def Hamming(DNA1, DNA2):
    counter = 0
    for i in range(len(DNA1)):
        if(DNA1[i] != DNA2[i]):
            counter += 1
    return counter

for i in range(len(Text) - len(DNA)):
    if(Hamming(Text[i:i+len(DNA)],DNA)<=HammingMax):
        print(i, end=" ")
    
