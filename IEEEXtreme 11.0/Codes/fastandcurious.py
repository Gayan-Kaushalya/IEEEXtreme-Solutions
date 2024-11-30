from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(u):
    global time
    disc[u] = low[u] = time
    time += 1
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v)
            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges[u].append(v)
                bridges[v].append(u)
                
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def find_bridges_and_nodes_with_only_bridges():
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
    
    result = []
    for i in range(1, N + 1):
        if len(graph[i]) == len(bridges[i]):
            result.append(i)
    
    return result

N, M = map(int, input().split())
graph = defaultdict(list)
bridges = defaultdict(list)

disc = [-1] * (N + 1)
low = [-1] * (N + 1)
parent = [-1] * (N + 1)
visited = [False] * (N + 1)

time = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = find_bridges_and_nodes_with_only_bridges()

for node in result:
    print(node)