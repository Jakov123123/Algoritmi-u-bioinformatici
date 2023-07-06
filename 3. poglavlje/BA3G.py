f = open("C:/Users/Jakov/Desktop/BA3G_Input.txt", "r")
edges = f.read().splitlines()

def rosalindInputToGraph(edges):
    D = {}
    for edge in edges:
        first, second = edge.split(" -> ")
        second = second.split(",")
        D[first] = second
    return D

def balanceGraph(edges):
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
    
    #sada ćemo izdvojiti one koji nisu uravnoteženi; spojiti ih i provesti prethodni algoritam
    for j in dictBalance.keys():
        if(dictBalance[j][1] < dictBalance[j][0]):
            end = j
        elif(dictBalance[j][1] > dictBalance[j][0]):
            begin = j
    if(end in edges.keys()):
        edges[end].append(begin)
    else:
        edges[end] = [begin]
    return edges, end, begin

def getACycle(graph, possible_starts):
    origin = None
    for start in possible_starts:
        if start in graph:
            origin = start
            break
    if origin is None:
        raise
    cycle = []
    first = origin
    while True:
        if first in graph:
            second = graph[first][0]
            cycle.append([first, second])
            if len(graph[first]) == 1:
                graph.pop(first, None)
            else:
                graph[first] = graph[first][1:]
            if second == origin:
                break
            else:
                first = second
        else:
            break
    return cycle


def start_index(cycle, start):
    s_index = -1
    for i in range(0, len(cycle)):
        if cycle[i][0] == start:
            s_index = i
            break
    return s_index


def eulerianCycle(graph):
    cycles = []
    possible_starts = list(graph.keys())[:1]
    while len(graph) > 0:
        new_cycle = getACycle(graph, possible_starts)
        possible_starts.extend([x[0] for x in new_cycle])
        possible_starts = list(set(possible_starts))
        cycles.append(new_cycle)

    if len(cycles) == 1:
        path = cycles[0]
    else:
        path = cycles[0]
        for i in range(1, len(cycles)):
            next_ = cycles[i]
            s_index = start_index(path, next_[0][0])
            path = path[:s_index] + next_ + path[s_index:]

    firsts = [x[0] for x in path]
    res = "->".join(firsts) + f"->{path[-1][1]}"

    return res

graph = rosalindInputToGraph(edges)
graph, first, second = balanceGraph(graph)

cycle = eulerianCycle(graph)
parts = cycle.split(f"{first}->{second}", maxsplit=1)
if parts[0] == '':
    path = parts[1]
elif parts[1] == '':
    path = parts[0]
else:
    part1 = parts[0] + first
    part1_trimmed = part1.split("->", maxsplit=1)[1]
    part2 = second + parts[1]
    path = part2 + "->" + part1_trimmed

fp = open("C:/Users/Jakov/Desktop/BA3G_res.txt", 'w')
fp.write(path)
fp.close()