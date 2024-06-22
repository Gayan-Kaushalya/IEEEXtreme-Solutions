r, c = map(int, input().split())

forest = []

for i in range(r):
    forest.append(list(map(int, input().split())))

for i in range(r - 1, -1, -1):
    for j in range(c - 1, -1, -1):
        if i == r - 1 and j == c - 1:
            forest[i][j] = 1
            continue
        
        if i < r - 1 and j < c - 1:
            forest[i][j] = min(forest[i + 1][j], forest[i][j + 1]) - forest[i][j]
            if forest[i][j] <= 0:
                forest[i][j] = 1
                
        if i == r - 1:
            forest[i][j] = forest[i][j + 1] - forest[i][j]
            if forest[i][j] <= 0:
                forest[i][j] = 1
                
        if j == c - 1:
            forest[i][j] = forest[i + 1][j] - forest[i][j]
            if forest[i][j] <= 0:
                forest[i][j] = 1

print(1 if forest[0][0] <= 1 else forest[0][0])