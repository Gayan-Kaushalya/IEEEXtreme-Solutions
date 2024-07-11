def solve(a, prev, l, r):
    if prev[r] < l:
        return 0
    
    new_left = prev[r]
    left = new_left + 1
    right = r
    answer = new_left + 1
    
    while left <= right:
        middle = left + (right - left)//2
        if a[middle] > a[new_left]:
            left = middle + 1
            answer = middle
        else:
            right = middle - 1
    
    result = r - new_left + 1
    
    if (result % 2 == 0) and (answer != (new_left + r + 1)//2):
        return result - 1
    else:
        return result

n = int(input())
a = [int(i) for i in input().split()]
p = [-1]

results = []
prev = -1

for i in range(1, n):
    if a[i - 1] < a[i]:
        prev = i - 1
    p.append(prev)

for j in range(int(input())):
    l, r = [int(i) for i in input().split()]
    results.append(solve(a, p, l - 1, r - 1))
    
for x in results:
    print(x)