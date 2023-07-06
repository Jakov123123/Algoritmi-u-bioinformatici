f = open("C:/Users/student/Desktop/BA3B_Input.txt", "r")
patterns = f.read().splitlines()

st = patterns[0]
for p in patterns:
    if(p != patterns[0]):
        st += p[len(p) - 1]

print(st)