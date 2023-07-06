n = 14
m = 5
f1 = open("C:/Users/student/Desktop/BA5B_Input_Down.txt", "r")
f2 = open("C:/Users/student/Desktop/BA5B_Input_Right.txt", "r")

down = []
right = []

for l in f1.read().splitlines():
    l1 = l.split(" ")
    d = []
    for i in range(len(l1)):
        d.append(int(l1[i]))
    down.append(d)

for l in f2.read().splitlines():
    l1 = l.split(" ")
    d = []
    for i in range(len(l1)):
        d.append(int(l1[i]))
    right.append(d)

f1.close()
f2.close()

def manhattantourist(n, m, down, right):
    s = []
    for i in range(n + 1):
        s.append((m + 1) * [0])

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]

print(manhattantourist(n, m, down, right))