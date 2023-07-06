f = open("C:/Users/Jakov/Desktop/BA3E_Input.txt", "r")
patterns = f.read().splitlines()

patterns.sort()
k = len(patterns[0])

def CompositionGraph(patterns):
    graph = {}
    for i in range(len(patterns)):      
        a = patterns[i][0:k-1]
        if(patterns[i][0:k-1] in graph.keys()):
            graph[patterns[i][0:k-1]].append(patterns[i][1:k])
            graph[patterns[i][0:k-1]].sort()
        else:
            l = []
            l.append(patterns[i][1:k])
            graph[patterns[i][0:k-1]] = l
    return graph

q = CompositionGraph(patterns)
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

fp = open("C:/Users/Jakov/Desktop/BA3E_res.txt", 'w')

for i in range(len(q)):
    fp.write(w[i] + " -> " + pr(q[w[i]]) + "\n")

fp.close()