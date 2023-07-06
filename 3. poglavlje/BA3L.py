f = open("C:/Users/Jakov/Desktop/BA3L_Input.txt", "r")
patterns = f.read().splitlines()
k = 50
d = 200

st = patterns[0][:k]
for p in patterns:
    if(p != patterns[0]):
        st += p[k - 1]
#sada smo nalijepili sve iz prvog člana para, sada moramo one iz drugog pri kraju

for i in range(k + d):
    st += patterns[len(patterns) - (k + d) + i][-1]

fp = open("C:/Users/Jakov/Desktop/BA3L_res.txt", 'w')
fp.write(st)
fp.close()