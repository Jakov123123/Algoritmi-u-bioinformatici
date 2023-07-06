f = open("C:/Users/Jakov/Desktop/BA3K_Input.txt", "r")
patterns = f.read().splitlines()
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

def dictBalance(edges):
    #uzimamo sve čvorove (i u listama i u ključevima)
    l = []
    for i in edges.keys():
        l.append(i)
        for k in edges[i]:
            l.append(k)

    #sada ćemo stvoriti dictionary svakog čvora s praznim brojem ulaza i izlaza iz čvora
    dictBalance = {}
    for i in l:
        j = i
        dictBalance[j] = [0, 0]

    #sada ćemo upisati broj ulaza i izlaza za svaki čvor
    for j in dictBalance.keys():
        if(j in edges.keys()):
            dictBalance[j][1] = len(edges[j])
            for k in edges[j]:
                dictBalance[k][0] += 1
    return dictBalance

def isolatedCycles(nodes, dbalance):
    isolates = []
    for node in nodes.keys():
        if(dbalance[node][0] == 1 and dbalance[node][1] == 1):
            w = nodes[node][0]
            path = [w]
            while((dbalance[w][0] == 1 and dbalance[w][1] == 1) and w in nodes.keys()):
                if(w == node):
                    isolates.append(path)
                    isolates = uniqueIsolates(isolates)
                    break
                path.extend([nodes[w][0]])
                w = nodes[w][0]
    for i in isolates:
        i.append(i[0])
    return isolates

def uniqueIsolates(isolates):
    unique_cycles = []
    for cycle in isolates:
        sorted_cycle = sorted(cycle)
        if sorted_cycle not in unique_cycles:
            unique_cycles.append(sorted_cycle)
    return unique_cycles

def maximalNonBranchingPaths(nodes, dbalance):
    paths = []
    for node in nodes.keys():
        if(dbalance[node][0] != 1 or dbalance[node][1] != 1):
            if(dbalance[node][1] > 0):
                for w in nodes[node]:
                    nonBranchingPath = [node, w]
                    while((dbalance[w][0] == 1 and dbalance[w][1] == 1) and w in nodes.keys()):
                        nonBranchingPath.extend([nodes[w][0]])
                        w = nodes[w][0]
                    paths.append(nonBranchingPath)
    for isolate in isolatedCycles(nodes, dbalance):
        paths.append(isolate)
    return paths

edges = CompositionGraph(patterns)
dBalance = dictBalance(edges)
paths = maximalNonBranchingPaths(edges, dBalance)

pr = ""
for p in paths:
    pr += p[0]
    for i in p:
        if(i != p[0]):
            pr += i[-1]
    pr += "\n"
    
fp = open("C:/Users/Jakov/Desktop/BA3K_res.txt", 'w')
fp.write(pr)
fp.close()