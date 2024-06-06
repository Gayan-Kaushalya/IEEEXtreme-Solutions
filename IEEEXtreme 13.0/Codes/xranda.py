mod = 10**9 + 7

n = int(input())
edges = []

for x in range(n-1):
    edges.append(list(map(int, input().split())))
    
edges = sorted(edges, key=lambda x: x[2])  # sort by weight

parents = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

sum = 0

for i in range(n - 1):
    start, end, weight = edges[i]
    
    while parents[start] != start:
        start = parents[start]
        
    while parents[end] != end:
        end = parents[end]
        
    sum += size[start] * size[end] * weight 
    
    if size[start] > size[end]:
        parents[end] = parents[start]
        size[start] += size[end]
        size[end] = size[start]
    else:
        parents[start] = parents[end]
        size[end] += size[start]
        size[start] = size[end]
        
print(sum % mod)