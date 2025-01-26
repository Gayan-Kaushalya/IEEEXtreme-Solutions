intervals = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    intervals.append((a, b))

for t1 in range(-100, 101):
    answerFound = False
    
    for t2 in range(t1, 101):
        valid = True
        for a, b in intervals:
            if not ((a <= t1 <= b) or (a <= t2 <= b)):
                valid = False
                break
        if valid:
            print(t1, t2)
            answerFound = True
            break
    
    if answerFound:
        break
else:
    print(-1)