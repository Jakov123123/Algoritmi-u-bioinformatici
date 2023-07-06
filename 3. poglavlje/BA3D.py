k = int(input())

def PathGraph(text):
    graph = {}
    for i in range(len(text) - k + 1):
        a = text[i : i + k - 1]
        if(text[i : i + k - 1] in graph.keys()):
            graph[text[i : i + k - 1]].append(text[i + 1 : i + k])
            graph[text[i : i + k - 1]].sort()
        else:
            l = []
            l.append(text[i + 1 : i + k])
            graph[text[i : i + k - 1]] = l
    return graph

q = PathGraph("AAGATTCTCTAC")
w = []

for i in range(len(q)):
    w.append(list(q.keys())[i])

w.sort()

def pr(l):
    x = ""
    for i in range(len(l)):
        if(i == 0):
            x += l[i]
        else:
            x += ", " + l[i]
    return x

fp = open("C:/Users/Jakov/Desktop/BA3D_res.txt", 'w')

for i in range(len(q)):
    fp.write(w[i] + " -> " + pr(q[w[i]]) + "\n")

fp.close()