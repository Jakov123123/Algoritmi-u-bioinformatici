text = input()
k = int(input())

def Permutations(arr, text, k):
    if(k == 0):
        arr.append(text)
        return arr
    Permutations(arr, text + "A", k - 1)
    Permutations(arr, text + "C", k - 1)
    Permutations(arr, text + "G", k - 1)
    Permutations(arr, text + "T", k - 1)
    return arr

def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

p = Permutations([],"", k)
print(p)
for i in p:
    print(Count(text, i), end = " ")