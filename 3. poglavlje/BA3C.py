f = open("C:/Users/student/Desktop/BA3C_Input.txt", "r")
patterns = f.read().splitlines()

patterns.sort()

k = len(patterns[0])
fp = open("C:/Users/student/Desktop/BA3C_res.txt", 'w')
for pt in patterns:
    st = pt
    for pt1 in patterns:
        if(st[1 : k] == pt1[0 : k - 1]):
            fp.write(st + " -> " + pt1 + "\n")

fp.close()