import itertools

N, M = [int(x) for x in input().split()]

data = []

for n in range(N):
    data.append([int(x) % 3 for x in input().split()])

def evaluate(data):
    score = 0
    for n in range(N):
        a = data[n].count(0)
        b = data[n].count(1)
        c = data[n].count(2)
        score += max(a,b,c)
    return score    

# Try all combinations
best_score = 0
for perm in itertools.product([0,1,2], repeat=M):
    for m in range(M):
        for n in range(N):
            data[n][m] = ((data[n][m] + perm[m]) % 3)
            
    score = evaluate(data)
    
    for m in range(M):
        for n in range(N):
            data[n][m] = ((data[n][m] - perm[m]) % 3)
            
    best_score = max(score, best_score)
    
print(best_score)