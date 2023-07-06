k = 8

def allMutations(k, letters, current_combination, lst): #dakle kao argumente uzimamo duljinu, listu slova, trenutnu kombinaciju koju gradimo i rječnik
    if len(current_combination) == k:
        lst.append(current_combination)
    else:
        for letter in letters:
            allMutations(k, letters, current_combination + letter, lst)

lst = []
allMutations(k, ["0", "1"], "", lst)
patterns = lst

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

edges = CompositionGraph(patterns)

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

cycle = eulerianCycle(edges)
cycle = cycle.split("->")

st = cycle[0]
for p in cycle:
    if(p != cycle[0]):
        st += p[len(p) - 1]

if(k >= 4):
    print(st[:3-k])
else:
    print(st)