k = int(input())
text = input()
lst = []

for i in range(len(text) - k + 1):
    lst.append(text[i : i + k])

lst.sort()
fp = open("C:/Users/student/Desktop/BA3A.txt", 'w')
for st in lst:
    fp.write(st + "\n")

fp.close()