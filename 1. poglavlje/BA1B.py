Text = input()
k = int(input())

def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

def FrequencyList(text, k):
    l = []
    for i in range(len(text) - k + 1):
        q = Count(text, text[i : i + k])
        l.append(q)
    return l 
    
M = max(FrequencyList(Text, k))
F = []

for i in range(len(Text) - k + 1):
    q = Count(Text, Text[i : i + k])
    if(q == M and Text[i : i + k] not in F):
        print(Text[i : i + k])
    F.append(Text[i : i + k])
