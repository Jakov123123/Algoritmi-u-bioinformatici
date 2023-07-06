DNA1 = input()
DNA2 = input()
counter = 0

for i in range(len(DNA1)):
    if(DNA1[i] != DNA2[i]):
        counter += 1

print(counter)
